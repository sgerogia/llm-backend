import os.path

from llm_backend.constants import CHAT_PREFIX_ASSISTANT, CHAT_PREFIX_USER, PARAM_LLAMA_MODEL


def test_createChatCompletion_simple(set_logger, llama_client, llama_params):
    # arrange
    completionReq = {
        "model": "llama",
        "messages": [
            {"role": "system", "content": f'A chat between a curious human ("{CHAT_PREFIX_USER}") and an artificial intelligence assistant ("{CHAT_PREFIX_ASSISTANT}"). The assistant gives helpful, brief, and polite answers to the human\'s questions. When given instructions, the assistant follows them precisely.'},
            {"role": "user", "content": "Just respond with the word 'Hello!'. No other words needed for now."},
        ],
        "stream": False,
        "temperature": 0.1,
    }
    expected_model_name = os.path.basename(llama_params[PARAM_LLAMA_MODEL])

    # act
    res = llama_client.post('/v1/chat/completions', json=completionReq, buffered=True)

    # assert
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    assert res.json['object'] == 'chat.completion'
    choices = res.json['choices']
    assert 'Hello!' in choices[0]['message']['content']
    assert res.json['object'] == 'chat.completion'
    assert res.json['model'] == expected_model_name


def test_createChatCompletion_stream(set_logger, llama_client, llama_params):
    # arrange
    completionReq = {
        "model": "llama",
        "messages": [
            {"role": "system", "content": f'A chat between a curious human ("{CHAT_PREFIX_USER}") and an artificial intelligence assistant ("{CHAT_PREFIX_ASSISTANT}"). The assistant gives helpful, brief, and polite answers to the human\'s questions. When given instructions, the assistant follows them precisely.'},
            {"role": "user", "content": "Just say 'Hello!'. No other words needed."},
        ],
        "stream": True,
        "temperature": 0.1,
    }
    expected_model_name = os.path.basename(llama_params[PARAM_LLAMA_MODEL])

    # act
    res = llama_client.post('/v1/chat/completions', json=completionReq, buffered=True)

    # assert
    assert res.status_code == 200
    assert 'text/event-stream' in res.headers['Content-Type']
    length = len(res.response)
    assert length > 0
    # pseudo-iteration of responses
    # can't be 100% certain of the actual response due to quantization (in particular) and different models (in general)
    for index in range(length-1):
        assert b'"object": "chat.completion.chunk"' in res.response[index]
        assert (b'"model": "' + bytes(expected_model_name, 'utf-8') + b'"') in res.response[index]
    assert b'data: [DONE]\n\n' == res.response[length-1]