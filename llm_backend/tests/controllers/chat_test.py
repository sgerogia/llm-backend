def test_createChatCompletion_simple(set_openai_key, set_logger, client):
    # arrange
    completionReq = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using markdown."},
            {"role": "user", "content": "Just say 'Hello!'"},
        ],
        "stream": False,
    }

    # act
    res = client.post('/v1/chat/completions', json=completionReq, buffered=True)

    # assert
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    assert res.json['object'] == 'chat.completion'
    choices = res.json['choices']
    assert choices[0]['message']['content'] == 'Hello!'


def test_createChatCompletion_stream(set_openai_key, set_logger, client):
    # arrange
    completionReq = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user\'s instructions carefully. Respond using markdown."},
            {"role": "user", "content": "Just say 'Hello!'"},
        ],
        "stream": True,
    }

    # act
    res = client.post('/v1/chat/completions', json=completionReq, buffered=True)

    # assert
    assert res.status_code == 200
    assert 'text/event-stream' in res.headers['Content-Type']
    assert len(res.response) > 0
    assert b'chat.completion.chunk' in res.response[0]
    assert b'"role": "assistant"' in res.response[0]
