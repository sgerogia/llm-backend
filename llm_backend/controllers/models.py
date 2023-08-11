import logging
import os.path
import time
import uuid
from logging import Logger
from typing import List

import openai
from llama_cpp import Llama

from llm_backend.constants import MODEL_LLAMA, MODEL_OPENAI, PARAM_LLAMA_MODEL, PARAM_OPENAI_KEY
from llm_backend.models.models import Model, ModelPermission
from . import logger


class ModelsController:
    """Base class for model handling controllers.
    Defines an internal logger and the interface for fetching models."""

    _logger: Logger = None

    def __init__(self, log: Logger = None):
        """Create a new instance of the controller initialising the logger.

        :param log the logger to use, defaults to `logging.getLogger('server')`
        """
        self._logger = log if log is not None else logging.getLogger('server')

    def fetchModels(self) -> List[Model]:
        """Fetch a list of models.
        Descendants should override this method and implement the logic to generate the response."""
        pass


    def getModel(self, id: str) -> Model:
        """Fetch a model given its id, or None if not found.
        Descendants should override this method and implement the logic to generate the response."""
        pass


class OpenaiModelsController(ModelsController):
    """Models controller that uses the OpenAI API.
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

    def fetchModels(self) -> List[Model]:
        logger.debug('Fetching models from OpenAI')
        res = openai.Model.list()
        if res is not None:
            return res['data']

    def getModel(self, id: str) -> Model:
        return openai.Model.retrieve(id)


class LlamaModelsController(ModelsController):
    """Models controller that uses a local Llama-compatible model."""

    _llama_model: Model = None

    def __init__(self, log: Logger = None, model_file_path: str = None):
        """Create a new instance of the controller and set the path of the model.

        :param log the logger to use
        :param model_file_path location of the Llama-compatible model file
        """
        super().__init__(log=log)

        if model_file_path is None or not os.path.exists(model_file_path) or not os.path.isfile(model_file_path):
            self._logger.error('Llama file path is not defined or is not a file!')
            raise ValueError('Llama file path is not defined or is not a file')
        else:
            self._logger.info(f'Creating Llama model from file {model_file_path}')
            self._model_name = os.path.basename(model_file_path)
            llm = Llama(
                model_path=model_file_path,
            )
            if llm is None:
                self._logger.error(f'{model_file_path} is not a valid Llama model')
                raise ValueError(f'{model_file_path} is not a valid Llama model')
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

    def fetchModels(self) -> List[Model]:
        logger.debug('Fetching models from Llama')
        return [self._llama_model]

    def getModel(self, id: str) -> Model:
        return self._llama_model if id == MODEL_LLAMA else None


# The cached chat controller instances
_model_controllers: dict = {}


def init(params: dict, log: Logger = None) -> dict:
    global _model_controllers

    try:
        _model_controllers[MODEL_OPENAI] = OpenaiModelsController(
            log=log,
            openai_key=params.get(PARAM_OPENAI_KEY))
    except ValueError:
        if log is not None:
            log.warning("OpenAI models controller not initialised")

    try:
        _model_controllers[MODEL_LLAMA] = LlamaModelsController(
            log=log,
            model_file_path=params.get(PARAM_LLAMA_MODEL),
        )
    except ValueError:
        if log is not None:
            log.warning("Llama models controller not initialised")

    return _model_controllers


def listModels():
    global _model_controllers

    logger.debug('listModels')

    models: List[Model] = []

    for cnt in _model_controllers.values():
        models = models + [model for model in cnt.fetchModels()]

    return {
        "object": "list",
        "data": models,
    }, 200


def retrieveModel(model):
    logger.debug(f"retrieveModel: {model}")

    _model: Model = None

    for cnt in _model_controllers.values():
        try:
            # a controller might throw an error if the model is not found
            _model = cnt.getModel(id=model)
        except:  # noqa: E722 intentional except clause
            pass
        if _model is not None:
            return _model, 200

    # if we got here, it is unknown
    return f"Model {model} not found", 404


def deleteModel(model_id):
    return {
        "message": "Not implemented",
    }, 501
