import json
import logging
import os

import connexion
import openai
from flask import Response, stream_with_context

from llm_backend.models.chat import ChatCompletionRequest, ChatCompletionResponse, ChatUsage, Chat
from . import logger


class ChatCompletionController:
    """Base class for chat completion controllers.
    Defines an internal logger and the interface for creating a new chat completion.
    Descendants should override the createInstance and createChatCompletion methods."""

    _logger = None

    def __init__(self):
        """Create a new instance of the controller initialising the logger."""
        self._logger = logging.getLogger('server')

    def createChatCompletion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """Create a new chat completion.
        Descendants should override this method and implement the logic to generate the response."""
        pass


class OpenaiChatCompletionController(ChatCompletionController):
    """Chat completion controller that uses the OpenAI API."""

    def __init__(self):
        super().__init__()
        """Create a new instance of the controller and set the global OpenAI key."""
        key = os.environ.get('OPENAI_API_KEY')
        if key is None:
            self._logger.warn('OPENAI API key is not defined!')
        else:
            self._logger.info('Setting OPENAI API key')
            openai.api_key = key

    def createChatCompletion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        compl = openai.ChatCompletion.create(
            model=request.model,
            messages=request.messages,
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


# The cached chat controller instance
chat_completion_controller = None


def createChatCompletion():
    global chat_completion_controller

    if chat_completion_controller is None:
        type = os.environ.get('CHAT_CONTROLLER', 'openai')
        if type == 'openai':
            chat_completion_controller = OpenaiChatCompletionController()
        else:
            raise ValueError(f'Unknown chat controller type: {type}')

    # Get the JSON from the request
    completionReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        req = json.dumps(completionReq)
        logger.debug(f"createChatCompletion: {req}")

    req = ChatCompletionRequest.from_json(completionReq)

    # Call the controller
    compl = chat_completion_controller.createChatCompletion(req)

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