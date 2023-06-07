import logging
import os

from pythonjsonlogger import jsonlogger

from llm_backend import app


def create_logger():
    logger = logging.getLogger(__name__)

    formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger = create_logger()
flask_app = app.create_app(logger)

if __name__ == "__main__":
    logger.info('Starting server')
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
