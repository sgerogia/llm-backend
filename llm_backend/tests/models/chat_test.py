import json

import pytest

from llm_backend.models.chat import ChatCompletionResponse
from llm_backend.models.constants import CHAT_COMPLETION


def test_parse_chatcompletionrequest():
    # arrange
    data = """{
        "id": "chatcmpl-7WMs0ChahNI8f38rrso9g64RGxoOG", 
        "object": "chat.completion", 
        "created": 1687948764, 
        "model": "gpt-3.5-turbo-0613", 
        "choices": [
            {"index": 0, "message": {"role": "user", "content": "Just say Hello"}, "finish_reason": null},
            {"index": 1, "message": {"role": "assistant", "content": "Hello!"}, "finish_reason": "stop"}
        ], 
        "usage": {"prompt_tokens": 42, "completion_tokens": 2, "total_tokens": 44}}
        """

    # act
    json_str = json.loads(data)
    res = ChatCompletionResponse.from_json(json_str)

    # assert
    # fields are populated
    assert res.streaming == False
    assert res.model == 'gpt-3.5-turbo-0613'
    assert res.id == 'chatcmpl-7WMs0ChahNI8f38rrso9g64RGxoOG'
    assert res.object == CHAT_COMPLETION
    assert res.created == 1687948764
    assert res.usage.prompt_tokens == 42
    assert res.usage.completion_tokens == 2
    assert res.usage.total_tokens == 44
    # direct list access
    assert len(res._choices) == 2
    assert res._choices[0].index == 0
    assert res._choices[0].finish_reason is None
    assert res._choices[0].message.role == 'user'
    assert res._choices[0].message.content == 'Just say Hello'
    # iterator access
    i = 0
    for choice in res:
        if i == 0:
            assert choice.index == 0
            assert choice.finish_reason is None
            assert choice.message.role == 'user'
            assert choice.message.content == 'Just say Hello'
        elif i == 1:
            assert choice.index == 1
            assert choice.finish_reason == 'stop'
            assert choice.message.role == 'assistant'
            assert choice.message.content == 'Hello!'
        else:
            assert False
        i += 1
    # iterate_strings raises ValueError
    with pytest.raises(ValueError):
        res.iterate_strings()


def test_parse_chatcompletionrequest_stream_datachunk():
    # arrange
    data = """data: {"id": "chatcmpl-7WMsZuQEgubixa1EOzIo6IPHyvbZA", "object": "chat.completion.chunk", "created": 1687948799, "model": "gpt-3.5-turbo-0613", "choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}, "finish_reason": null}]}

data: {"id": "chatcmpl-7WMsZuQEgubixa1EOzIo6IPHyvbZA", "object": "chat.completion.chunk", "created": 1687948799, "model": "gpt-3.5-turbo-0613", "choices": [{"index": 0, "delta": {"content": "Hello"}, "finish_reason": null}]}

data: {"id": "chatcmpl-7WMsZuQEgubixa1EOzIo6IPHyvbZA", "object": "chat.completion.chunk", "created": 1687948799, "model": "gpt-3.5-turbo-0613", "choices": [{"index": 0, "delta": {"content": "!"}, "finish_reason": null}]}

data: {"id": "chatcmpl-7WMsZuQEgubixa1EOzIo6IPHyvbZA", "object": "chat.completion.chunk", "created": 1687948799, "model": "gpt-3.5-turbo-0613", "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}

data: [DONE]

"""
    iterator = iter(data.split('\n\n'))

    # act
    res = ChatCompletionResponse.from_string_iterator(iterator)

    # assert
    # fields are not populated
    assert res.streaming == True
    assert res.id is None
    assert res.object is None
    assert res.created is None
    assert res.model is None
    assert res.usage is None
    # object iterator
    i = 0
    for item in res:
        if i == 0:
            # fields are now populated
            assert res.id == 'chatcmpl-7WMsZuQEgubixa1EOzIo6IPHyvbZA'
            assert res.object == 'chat.completion.chunk'
            assert res.created == 1687948799
            assert res.model == 'gpt-3.5-turbo-0613'
            # item fields
            assert item.id == 'chatcmpl-7WMsZuQEgubixa1EOzIo6IPHyvbZA'
            assert item.object == 'chat.completion.chunk'
            assert item.created == 1687948799
            assert item.model == 'gpt-3.5-turbo-0613'
            # choice fields
            assert item._choices[0].index == 0
            assert item._choices[0].finish_reason is None
            assert item._choices[0].message is None
            assert item._choices[0].delta.role == 'assistant'
            assert item._choices[0].delta.content == ''
        elif i == 1:
            assert item._choices[0].index == 0
            assert item._choices[0].finish_reason is None
            assert item._choices[0].message is None
            assert item._choices[0].delta.role is None
            assert item._choices[0].delta.content == 'Hello'
        elif i == 2:
            assert item._choices[0].index == 0
            assert item._choices[0].finish_reason is None
            assert item._choices[0].message is None
            assert item._choices[0].delta.role is None
            assert item._choices[0].delta.content == '!'
        elif i == 3:
            assert item._choices[0].index == 0
            assert item._choices[0].finish_reason == 'stop'
            assert item._choices[0].message is None
            assert item._choices[0].delta.role is None
            assert item._choices[0].delta.content is None
        else:
            pytest.fail('Should not have reached here')
        i += 1