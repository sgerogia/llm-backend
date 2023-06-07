import connexion
import json
import logging

from . import logger


def createCompletion():
    # Get the JSON from the request
    completionReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createCompletion: ' + json.dumps(completionReq))

    model = completionReq['model']
    prompt = completionReq.get('prompt', None)
    suffix = completionReq.get('suffix', None)
    max_tokens = completionReq.get('max_tokens', None)
    temperature = completionReq.get('temperature', None)
    top_p = completionReq.get('top_p', None)
    n = completionReq.get('n', None)
    stream = completionReq.get('stream', None)
    logprobs = completionReq.get('logprobs', None)
    echo = completionReq.get('echo', None)
    stop = completionReq.get('stop', None)
    presence_penalty = completionReq.get('presence_penalty', None)
    frequency_penalty = completionReq.get('frequency_penalty', None)
    best_of = completionReq.get('best_of', None)
    logit_bias = completionReq.get('logit_bias', None)
    user = completionReq.get('user', None)

    # Do stuff

    # Return the result as JSON
    return {
        "id": "1",
        "object": "text_completion",
        "created": 1610878670,
        "model": "davinci:2020-05-03",
        "choices": [
            {
                "text": "Hello, World!",
                "index": 0,
                "finish_reason": "length",
            }
        ],
        "usage": {
            "prompt_tokens": 5,
            "completion_tokens": 3,
            "total_tokens": 8,
        },
    }, 200
