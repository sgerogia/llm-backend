import logging
import os

import pytest

from llm_backend import app
from llm_backend.constants import ENV_OPENAI_API_KEY, ENV_LLAMA_MODEL_FILE, PARAM_OPENAI_KEY, PARAM_LLAMA_MODEL, \
    PARAM_LLAMA_CONTEXT_SIZE


@pytest.fixture()
def openai_params():
    key = os.environ.get(ENV_OPENAI_API_KEY)
    if key is None:
        raise ValueError(f"{ENV_OPENAI_API_KEY} env. variable is missing.")

    params = {
        PARAM_OPENAI_KEY: key,
    }
    return params


@pytest.fixture()
def llama_params():
    model_path = os.environ.get(ENV_LLAMA_MODEL_FILE)
    if model_path is None:
        raise ValueError(f"{ENV_LLAMA_MODEL_FILE} env. variable is missing.")

    params = {
        PARAM_LLAMA_MODEL: model_path,
        PARAM_LLAMA_CONTEXT_SIZE: 2048,
    }
    return params


@pytest.fixture
def llama_client(llama_params):
    flask_app = app.create_app(
        logger=logging.getLogger('server'),
        params=llama_params
    )
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


@pytest.fixture
def openai_client(openai_params):
    flask_app = app.create_app(
        logger=logging.getLogger('server'),
        params=openai_params
    )
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


@pytest.fixture
def set_logger():
    logger = logging.getLogger('server')
    handler = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

