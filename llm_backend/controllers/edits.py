import connexion
import json
import logging

from . import logger


def createEdit():
    # Get the JSON from the request
    completionReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createEdit: ' + json.dumps(completionReq))

    model = completionReq["model"]
    input = completionReq.get("input", None)
    instruction = completionReq["instruction"]
    n = completionReq.get("n", 1)
    temperature = completionReq.get("temperature", 1)
    top_p = completionReq.get("top_p", 1)

    # Do stuff

    # Return the result as JSON
    return {
        "object": "edit",
        "created": 1610878670,
        "choices": [
            {
                "text": "Hello world!",
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
