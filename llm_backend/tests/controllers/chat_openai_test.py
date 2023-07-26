def test_createChatCompletion_simple(set_logger, openai_client):
    # arrange
    completionReq = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using plain text."},
            {"role": "user", "content": "Just say 'Hello!' No other words are needed."},
        ],
        "stream": False,
    }

    # act
    res = openai_client.post('/v1/chat/completions', json=completionReq, buffered=True)

    # assert
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    assert res.json['object'] == 'chat.completion'
    choices = res.json['choices']
    assert 'Hello!' in choices[0]['message']['content']
    assert res.json['object'] == 'chat.completion'


def test_createChatCompletion_stream(set_logger, openai_client):
    # arrange
    completionReq = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using plain text."},
            {"role": "user", "content": "Just say 'Hello!' No other words are needed."},
        ],
        "stream": True,
    }

    # act
    res = openai_client.post('/v1/chat/completions', json=completionReq, buffered=True)

    # assert
    assert res.status_code == 200
    assert 'text/event-stream' in res.headers['Content-Type']
    length = len(res.response)
    assert length > 0
    # pseudo-iteration of responses
    for index in range(length-1):
        assert b'"choices": [{"index": 0, "finish_reason": null, "message": null, "delta": {"content": "", "role": "assistant"}}], "usage": ""}\n\n' in res.response[0]
        assert b'"choices": [{"index": 0, "finish_reason": null, "message": null, "delta": {"content": "Hello", "role": null}}], "usage": ""}\n\n' in res.response[1]
        assert b'"choices": [{"index": 0, "finish_reason": null, "message": null, "delta": {"content": "!", "role": null}}], "usage": ""}\n\n' in res.response[2]
        assert b'"choices": [{"index": 0, "finish_reason": "stop", "message": null, "delta": {"content": null, "role": null}}], "usage": ""}\n\n' in res.response[3]
    assert b'data: [DONE]\n\n' == res.response[length-1]