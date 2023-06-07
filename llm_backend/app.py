import os

import connexion
import openai


def create_app(logger):

    key = os.environ.get('OPENAI_API_KEY')
    if key is None:
        logger.warn('OPENAI API key is not defined!')
    else:
        logger.info('Setting OPENAI API key')
        openai.api_key = key

    # Create the Connexion application instance
    connex_app = connexion.App('server', specification_dir='./openapi/')

    logger.info('Loading API definition')
    # Load the API definition
    connex_app.add_api('llm_backend.yaml')

    # Get the underlying Flask app instance
    app = connex_app.app

    logger.info('Created Flask app')
    return app
