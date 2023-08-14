from logging import Logger

import connexion
import json
import logging
import openai
import os
from flask import Response, stream_with_context
from llama_cpp import Llama, ChatCompletionMessage

from llm_backend.constants import MODEL_OPENAI, MODEL_LLAMA, MODEL_CONTEXT_SIZE, PARAM_LLAMA_MODEL, \
    PARAM_LLAMA_CONTEXT_SIZE, PARAM_OPENAI_KEY
from llm_backend.models.chat import ChatCompletionRequest, ChatCompletionResponse, ChatUsage, Chat
from . import logger


class ChatCompletionController:
    """Base class for chat completion controllers.
    Defines an internal logger and the interface for creating a new chat completion.
    Descendants should override the createInstance and createChatCompletion methods."""

    _logger: Logger = None

    def __init__(self, log: Logger = None):
        """Create a new instance of the controller initialising the logger.

        :param log the logger to use, defaults to `logging.getLogger('server')`
        """
        self._logger = log if log is not None else logging.getLogger('server')

    def createChatCompletion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """Create a new chat completion.
        Descendants should override this method and implement the logic to generate the response."""
        pass


class OpenaiChatCompletionController(ChatCompletionController):
    """Chat completion controller that uses the OpenAI API.
    Requires a valid OpenAI key.
    """

    def __init__(self, log: Logger = None, openai_key: str = None):
        """Create a new instance of the controller and set the global OpenAI key.

        :param log the logger to use, defaults to `logging.getLogger('server')`
        :param openai_key the OpenAI API key
        """
        super().__init__(log=log)

        if openai_key is None:
            self._logger.error('OPENAI API key is not defined!')
            raise ValueError('OPENAI API key is not defined!')
        else:
            self._logger.info('Setting OPENAI API key')
            openai.api_key = openai_key

    def createChatCompletion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        compl = openai.ChatCompletion.create(
            model=request.model,
            messages=[msg.to_json() for msg in request.messages],
            stream=request.stream,
            temperature=request.temperature,
        )

        resp: ChatCompletionResponse = None
        if request.stream:
            resp = ChatCompletionResponse(
                streaming=True,
                _event_iterator=compl
            )
        else:
            resp = ChatCompletionResponse(
                streaming=False,

                id=compl['id'],
                created=compl['created'],
                model=compl['model'],
                object=compl['object'],
                usage=ChatUsage(
                    prompt_tokens=compl['usage']['prompt_tokens'],
                    completion_tokens=compl['usage']['completion_tokens'],
                    total_tokens=compl['usage']['total_tokens'],
                ),
                _choices=[Chat.from_json(choice) for choice in compl['choices']],
            )
        return resp


class LlamaChatCompletionController(ChatCompletionController):
    """Chat completion controller that uses a local Llama-compatible model.
    Internally it uses the Llama-Python bindings library."""

    _llm: Llama = None
    _ctx_size: int = 0
    _model_name: str = None

    def __init__(self, log: Logger = None, model_file_path: str = None, ctx_size: int = MODEL_CONTEXT_SIZE):
        """Create a new instance of the controller and set the path of the model.

        :param log the logger to use
        :param model_file_path location of the Llama-compatible model file
        :param context size, defaults to `MODEL_CONTEXT_SIZE`
        """
        super().__init__(log=log)

        if model_file_path is None or not os.path.exists(model_file_path) or not os.path.isfile(model_file_path):
            self._logger.error('Llama file path is not defined or is not a file!')
            raise ValueError('Llama file path is not defined or is not a file')
        else:
            self._ctx_size = ctx_size if ctx_size is not None else MODEL_CONTEXT_SIZE
            self._logger.info(f'Creating Llama model from file {model_file_path} with context size {self._ctx_size}')
            self._model_name = os.path.basename(model_file_path)
            self._llm = Llama(
                model_path=model_file_path,
                n_ctx=self._ctx_size,
                use_mlock=True,
                # FIXME: The following can crash the process on a machine without GPU
                n_gpu_layers=4,
            )


    def createChatCompletion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """Create a new chat completion from the request.
        The method assembles a prompt from the messages in the request and then calls the Llama model.
        The response is then converted to a ChatCompletionResponse object and returned.

        The controller calls `Llama.create_completion` rather than `create_chat_completion`. This is because
        the former allows better control over the prompt shape, namely the system prompt at the beginning.
        """

        messages = [ChatCompletionMessage(role=msg.role, content=msg.content) for msg in request.messages]

        compl = self._llm.create_chat_completion(
            messages=messages,
            stream=request.stream,
            temperature=request.temperature,
        )

        resp: ChatCompletionResponse = None
        if request.stream:
            resp = ChatCompletionResponse(
                streaming=True,
                _event_iterator=compl,
                model=self._model_name
            )
        else:
            resp = ChatCompletionResponse(
                streaming=False,

                id=compl['id'],
                created=compl['created'],
                model=self._model_name,
                object=compl['object'],
                usage=ChatUsage(
                    prompt_tokens=compl['usage']['prompt_tokens'],
                    completion_tokens=compl['usage']['completion_tokens'],
                    total_tokens=compl['usage']['total_tokens'],
                ),
                _choices=[Chat.from_json(choice) for choice in compl['choices']],
            )
        return resp


# The cached chat controller instances
_chat_completion_controllers: dict = {}


def init(
        params: dict,
        log: Logger = None):
    global _chat_completion_controllers

    try:
        _chat_completion_controllers[MODEL_OPENAI] = OpenaiChatCompletionController(
            log=log,
            openai_key=params.get(PARAM_OPENAI_KEY))
    except ValueError:
        if log is not None:
            log.warning("OpenAI chat controller not initialised")

    try:
        _chat_completion_controllers[MODEL_LLAMA] = LlamaChatCompletionController(
            log=log,
            model_file_path=params.get(PARAM_LLAMA_MODEL),
            ctx_size=params.get(PARAM_LLAMA_CONTEXT_SIZE)
        )
    except ValueError:
        if log is not None:
            log.warning("Llama chat controller not initialised")


def createChatCompletion():
    global _chat_completion_controllers

    # Get the JSON from the request
    completionReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        req = json.dumps(completionReq)
        logger.debug(f"createChatCompletion: {req}")

    req = ChatCompletionRequest.from_json(completionReq)

    # Find the right controller and call
    controller: ChatCompletionController = None
    if req.model == MODEL_LLAMA:
        controller = _chat_completion_controllers.get(MODEL_LLAMA)
    else:
        controller = _chat_completion_controllers.get(MODEL_OPENAI)

    if controller is None:
        return Response(f"Unknown or unsupported model: {req.model}", 500)

    compl = controller.createChatCompletion(req)

    if req.stream:
        return streamChat(compl)
    else:
        res = Response(json.dumps(compl.to_json()), 200)
        res.headers['Content-Type'] = 'application/json'
        return res


def streamChat(compl):
    def iterate():
        for chat in compl:
            s = json.dumps(chat.to_json())
            yield f"data: {s}\n\n"
        yield f"data: [DONE]\n\n"
        
    return Response(stream_with_context(iterate()), mimetype="text/event-stream")