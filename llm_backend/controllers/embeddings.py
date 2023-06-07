import connexion
import json
import logging

from . import logger


def createEmbedding():
    # Get the JSON from the request
    embReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createEmbedding: ' + json.dumps(embReq))

    model = embReq['model']
    input = embReq['input']
    user = embReq.get('user', None)

    # Do stuff

    # Return the result as JSON
    return {
        "object": "embedding",
        "model": "ada",
        "data": [
            {
                "index": 0,
                "object": "text",
                "embedding": [12, 23]
            }
        ],
        "usage": {
            "prompt_tokens": 5,
            "completion_tokens": 3,
            "total_tokens": 8,
        },
    }, 200