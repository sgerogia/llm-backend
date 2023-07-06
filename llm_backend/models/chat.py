import json
from dataclasses import dataclass
from typing import List, Iterator, Union

from .constants import CHAT_CHUNK_START, CHAT_STREAM_END


@dataclass
class ChatCompletionRequest:
    """Dataclass for chat completion request"""
    model: str
    messages: List[str]
    stream: bool
    temperature: float

    @classmethod
    def from_json(cls, data):
        """Create a ChatCompletionRequest from a JSON object.
        The object must have the following fields:
        - model: str
        - messages: list of str
        - stream: bool (optional, default False)
        - temperature: float (optional, default 1)
        """

        # top_p = completionReq.get('top_p', 1)
        # n = completionReq.get('n', 1)
        # stream = completionReq.get('stream', False)
        # stop = completionReq.get('stop', [])
        # max_tokens = completionReq.get('max_tokens', 48000)
        # presence_penalty = completionReq.get('presence_penalty', 0)
        # frequency_penalty = completionReq.get('frequency_penalty', 0)
        # logit_bias = completionReq.get('logit_bias', {})
        # user = completionReq.get('user', '')

        return cls(
            model=data['model'],
            messages=data['messages'],
            stream=data.get('stream', False),
            temperature=data.get('temperature', 1),
        )


@dataclass
class Delta:
    """A Delta is a single change in a chat. It has an optional role and a content."""
    content: str
    role: str = None

    @classmethod
    def from_json(cls, data):
        """Create a Delta from a JSON object or JSON string.
        The object must have the following fields:
        - content: str
        - role: str (optional)
        """
        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)

        return cls(
            content=json_data.get('content', None),
            role=json_data.get('role', None),
        )

    def to_json(self):
        """Convert the delta to a JSON object."""
        return {
            "content": self.content,
            "role": self.role,
        }


@dataclass
class Message:
    """A message is a single utterance in a chat. It has a role and a content."""
    role: str
    content: str

    @classmethod
    def from_json(cls, data):
        """Create a Message from a JSON object or JSON string.
        The object must have the following fields:
        - role: str
        - content: str
        """
        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        return cls(
            role=json_data['role'],
            content=json_data['content'],
        )

    def to_json(self):
        """Convert the message to a JSON object."""
        return {
            "role": self.role,
            "content": self.content,
        }


@dataclass
class Chat:
    """
    A Chat is an individual conversation item in a sequence between a user and an assistant.
    It has an index, a role, and a content.
    The content is a Delta or a Message object.
    The final chat in a sequence is marked with a 'finish_reason'.
    """
    index: int
    finish_reason: str = None
    message: Message = None
    delta: Delta = None

    @classmethod
    def from_json(cls, data):
        """Create a Chat from a JSON object or a JSON string.
        The object must have the following fields:
        - index: int
        - finish_reason: str (optional)
        - message: Message (optional, if delta defines)
        - delta: Delta (optional, if message defined)
        """
        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        message = json_data.get('message', None)
        delta = json_data.get('delta', None)
        msg = None
        dlt = None
        if message is None and delta is None:
            raise ValueError("Either 'message' or 'delta' must be defined.")
        elif message is not None:
            msg = Message.from_json(message)
        else:
            dlt = Delta.from_json(delta)

        return cls(
            index=json_data['index'],
            finish_reason=json_data.get('finish_reason', None),
            message=msg,
            delta=dlt,
        )

    def to_json(self):
        """Convert the Chat to a JSON object."""
        return {
            "index": self.index,
            "finish_reason": self.finish_reason,
            "message": self.message.to_json() if self.message else None,
            "delta": self.delta.to_json() if self.delta else None,
        }


@dataclass
class ChatUsage:
    """ChatUsage contains the usage statistics for a chat completion request."""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    @classmethod
    def from_json(cls, data):
        """Create a ChatUsage from a JSON object.
        The object must have the following fields:
        - prompt_tokens: int
        - completion_tokens: int
        - total_tokens: int
        """
        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        return cls(
            prompt_tokens=json_data['prompt_tokens'],
            completion_tokens=json_data['completion_tokens'],
            total_tokens=json_data['total_tokens'],
        )

    def to_json(self):
        return {
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
        }


class ChatCompletionResponseIterator:
    """ChatCompletionResponseIterator is wrapper over a List[Chat].
    It yields Chat objects.
    """

    def __init__(self, wrapped_list: List[Chat]):
        self._data = wrapped_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            element = self._data[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration


@dataclass
class ChatCompletionResponse:
    """ChatCompletionResponse contains the response from the chat completion API.
    The object is an Iterator over Chat objects.

    It can be initialised as a single object or as a stream of events.

        1) A single, non-streamed response, "all-in-one" object (streaming=False)
        In this case the following fields are populated: id, object, created, model.
        Field object has value CHAT_COMPLETION.
        The iterator returns items from an internal pre-filled list of Chat objects.

        2) A stream of chat events (streaming=True)
        Field object has value CHAT_COMPLETION_CHUNK.
        * The following fields are lazily populated, on iteration: id, object, created, model.
        * You can receive the events as strings (method iterate_strings) or Chat objects (normal iterator).
        * The strings from the iterate_strings method have a format of 'data: {...}\n\n'.
        * The stream of events (strings or ChatCompletionResponse objects) is not pre-filled, but fetched in a buffered manner.
    """
    streaming: bool

    id: str = None
    object: str = None
    created: int = None
    model: str = None
    usage: ChatUsage = None

    _choices: List[Chat] = None

    _event_iterator: Iterator[str] = None

    @classmethod
    def from_string_iterator(cls, iterator: Iterator[str]):
        """Create a ChatCompletionResponse from a string iterator.
        Sets the streaming flag to True and makes the Chat items available via the iterator.
        """
        return cls(
            streaming=True,
            _event_iterator=iterator
        )

    @classmethod
    def from_json(cls, data):
        """Create a ChatCompletionResponse from a JSON object or a JSON string.
        This method populates an object with the following fields (i.e. they are not empty/nil):
        - usage: ChatUsage
        - streaming: (ignored, always False)
        - id: str
        - object: str
        - created: int
        - model: str
        - choices: list of Chat
        """
        json_data = data
        if isinstance(data, str):
            json_data = json.loads(data)
        usage = None
        if json_data.get('usage', None) is not None:
            usage = ChatUsage.from_json(json_data['usage'])
        choices = [Chat.from_json(choice) for choice in json_data['choices']]
        return cls(
            usage=usage,
            streaming=False,
            id=json_data['id'],
            object=json_data['object'],
            created=json_data['created'],
            model=json_data['model'],
            _choices=choices,
        )

    def to_json(self):
        """Convert the object to a JSON string.
        Raises ValueError if the object is a streaming response."""
        if self.streaming:
            raise ValueError("to_json() can only be called on a non-streaming response.")

        return {
            "id": self.id,
            "object": self.object,
            "created": self.created,
            "model": self.model,
            "choices": [choice.to_json() for choice in self._choices],
            "usage": self.usage.to_json() if self.usage is not None else '',
        }

    def __iter__(self) -> Union[Iterator['Chat'], Iterator['ChatCompletionResponse']]:
        """Return an iterator over Chat objects or ChatCompletionResponse objects, depending on the value of `streaming`.
        If `streaming` is True, the iterator returns ChatCompletionResponse objects.
        If `streaming` is False, the iterator returns Chat objects.
        """
        if self.streaming:
            return self
        else:
            return ChatCompletionResponseIterator(self._choices)

    def __next__(self):
        if not self.streaming:
            raise ValueError("next() can only be called on a streaming response.")

        data = next(self._event_iterator)
        if isinstance(data, str):
            # remove 'data: ' prefix if needed
            if data.startswith(CHAT_CHUNK_START):
                data = data[len(CHAT_CHUNK_START):]
            if data.rstrip() == CHAT_STREAM_END:
                raise StopIteration
            data = json.loads(data)

        resp = ChatCompletionResponse.from_json(data)

        # if initialising lazily, populate the fields
        if self.id is None:
            self.id = resp.id
            self.object = resp.object
            self.created = resp.created
            self.model = resp.model

        # return the first choice
        return resp

    def iterate_strings(self) -> Iterator[str]:
        """Iterate over the events as strings.
        Returns a ValueError if the response is not a stream (streaming == False).
        """
        if not self.streaming:
            raise ValueError("iterate_strings can only be called on a streaming response.")
        return self._event_iterator
