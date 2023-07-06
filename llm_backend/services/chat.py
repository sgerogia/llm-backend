import openai

from .models import ChatCompletionRequest


class ChatCompletionService:
    """Interface for chat completion service"""
    def create_completion(self, chat_request: ChatCompletionRequest):
        pass



class OpenAIChatCompletionService(ChatCompletionService):
    """Chat completion service using OpenAI API"""

    def create_completion(self, chat_request: ChatCompletionRequest):
        return openai.ChatCompletion.create(
            model=chat_request.model,
            messages=chat_request.messages,
            stream=chat_request.stream,
            temperature=chat_request.temperature,
        )