from logging import Logger

import os
import time
import uuid
from llama_cpp import Llama, ChatCompletionMessage
from typing import List

from llm_backend.constants import MODEL_LLAMA, MODEL_CONTEXT_SIZE
from llm_backend.models.models import Model, ModelPermission

# singleton instance
_instance: 'LlamaModelService' = None


class LlamaModelService:
    """A singleton wrapper around a local Llama model."""

    _logger: Logger = None
    _llama_model: Model = None
    _model_name: str = None
    _llama: Llama = None

    def __init__(self, log: Logger = None, model_file_path: str = None, ctx_size: int = MODEL_CONTEXT_SIZE):
        """Create a new instance of the service and set the path of the model.

        :param log the logger to use
        :param model_file_path location of the Llama-compatible model file
        :param ctx_size the context size to use
        :raises ValueError if the model file path is not defined or is not a file
        """

        if _instance is not None:
            return _instance

        self._logger = log

        if model_file_path is None or not os.path.exists(model_file_path) or not os.path.isfile(model_file_path):
            self._logger.error('Llama file path is not defined or is not a file!')
            raise ValueError('Llama file path is not defined or is not a file')
        else:
            self._logger.info(f'Creating Llama model from file {model_file_path} with context size {ctx_size}')
            self._model_name = os.path.basename(model_file_path)
            self._llama = Llama(
                model_path=model_file_path,
                n_ctx=ctx_size,
                # FIXME: The following can crash the process on a machine without GPU
                # n_gpu_layers=1,
            )
            if self._llama is None:
                self._logger.error(f'{model_file_path} is not a valid Llama model')
                raise ValueError(f'{model_file_path} is not a valid Llama model')
        self._model_name = os.path.basename(model_file_path)
        self._llama_model = Model(
            object="model",
            id=MODEL_LLAMA,
            owned_by="My Org",
            parent=None,
            permission=[
                ModelPermission(
                    object="model_permission",
                    created=time.time(),
                    id="modelperm-" + str(uuid.uuid4()),
                    is_blocking=False,
                    allow_view=True,
                    allow_logprobs=True,
                    allow_sampling=True,
                    allow_create_engine=False,
                    allow_fine_tuning=False,
                    allow_search_indices=False,
                    organization="*",
                    group=None,
                )
            ],
            created=time.time(),
            root=None,
        )

    def get_model(self) -> Model:
        """Get the Llama model."""
        return self._llama_model

    def create_chat_completion(self, messages: List[ChatCompletionMessage], stream: bool, temperature: float):
        """Create a new chat completion from the messages.

        :param messages the messages to use for the prompt
        :param stream whether to stream the response
        :param temperature the temperature to use
        :return the response
        """
        return self._llama.create_chat_completion(
            messages=messages,
            stream=stream,
            temperature=temperature,
        )

    def get_model_name(self) -> str:
        """Get the name of the model."""
        return self._model_name
