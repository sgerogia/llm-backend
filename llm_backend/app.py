import connexion

from llm_backend.controllers.chat import init as init_chat_controller
from llm_backend.controllers.models import init as init_models_controller


def create_app(logger, params: dict):

    # Create the Connexion application instance
    connex_app = connexion.App('server', specification_dir='./openapi/')

    logger.info('Loading API definition')
    # Load the API definition
    connex_app.add_api('llm_backend.yaml')

    # Get the underlying Flask app instance
    app = connex_app.app

    # Initialise controllers
    init_chat_controller(
        log=logger,
        params=params,
    )
    init_models_controller(
        log=logger,
        params=params,
    )

    logger.info('Created Flask app')
    return app
