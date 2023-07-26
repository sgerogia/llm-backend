import llm_backend.controllers.chat as chat
from llm_backend.constants import MODEL_LLAMA, MODEL_OPENAI


def test_initController_empty(openai_params, set_logger):
    # arrange
    chat._chat_completion_controller = None

    # act
    chat.init(
        log=set_logger,
        params=openai_params,
    )

    # assert
    assert isinstance(chat._chat_completion_controllers[MODEL_OPENAI], chat.OpenaiChatCompletionController)


def test_initController_openai(openai_params, set_logger):
    # arrange
    chat._chat_completion_controller = None

    # act
    chat.init(
        log=set_logger,
        params=openai_params,
    )

    # assert
    assert isinstance(chat._chat_completion_controllers[MODEL_OPENAI], chat.OpenaiChatCompletionController)


def test_initController_llama(set_logger, llama_params):
    # arrange
    chat._chat_completion_controller = None

    # act
    chat.init(
        log=set_logger,
        params=llama_params,
    )

    # assert
    assert isinstance(chat._chat_completion_controllers[MODEL_LLAMA], chat.LlamaChatCompletionController)

