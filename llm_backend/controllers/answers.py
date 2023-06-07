import connexion
import json
import logging

from . import logger


def createAnswer():
    # Get the JSON from the request
    answerReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createAnswer: ' + json.dumps(answerReq))

    model = answerReq['model']
    question = answerReq['question']
    examples = answerReq['examples']
    examples_context = answerReq['examples_context']
    documents = answerReq.get('documents', None)
    file = answerReq.get('file', None)
    search_model = answerReq.get('search_model', None)
    max_rerank = answerReq.get('max_rerank', None)
    temperature = answerReq.get('temperature', None)
    logprobs = answerReq.get('logprobs', None)
    max_tokens = answerReq.get('max_tokens', None)
    stop = answerReq.get('stop', None)
    n = answerReq.get('n', None)
    logit_bias = answerReq.get('logit_bias', None)
    return_metadata = answerReq.get('return_metadata', None)
    return_prompt = answerReq.get('return_prompt', None)
    expand = answerReq.get('expand', None)
    user = answerReq.get('user', None)

    # Do stuff

    return {
        "object": "result",
        "model": "ada",
        "search_model": "ada",
        "completion": "cmpl-123",
        "answers": ["Hello, World!"],
        "selected_documents": [
            {
                "object": "document",
                "text": "Hello, World!",
            },
        ],
    }, 200

