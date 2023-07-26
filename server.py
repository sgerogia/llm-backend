import logging
import os

from pythonjsonlogger import jsonlogger

from llm_backend import app
from llm_backend.constants import ENV_LOG_LEVEL, ENV_OPENAI_API_KEY, ENV_LLAMA_MODEL_FILE, ENV_LLAMA_CONTEXT_SIZE


def create_logger():
    l = logging.getLogger(__name__)

    formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    level = os.environ.get(ENV_LOG_LEVEL, 'INFO').upper()
    l.setLevel(level)
    l.addHandler(handler)

    return l


logger = create_logger()


def _load_params() -> dict:
    logger.info("Loading environment variables")
    params = {
        app.PARAM_OPENAI_KEY: os.environ.get(ENV_OPENAI_API_KEY),
        app.PARAM_LLAMA_MODEL: os.environ.get(ENV_LLAMA_MODEL_FILE),
        app.PARAM_LLAMA_CONTEXT_SIZE: os.environ.get(ENV_LLAMA_CONTEXT_SIZE),
    }

    return params


flask_app = app.create_app(logger, _load_params())


if __name__ == "__main__":
    logger.info('Starting server')
    with flask_app.app_context():
        for rule in flask_app.url_map.iter_rules():
            print(f"Endpoint: {rule.endpoint}, Methods: {', '.join(rule.methods)}")
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
