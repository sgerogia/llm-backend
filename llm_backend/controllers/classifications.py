import connexion
import json
import logging

from . import logger


def createClassification():
    # Get the JSON from the request
    classReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createClassification: ' + json.dumps(classReq))

    model = classReq["model"]
    query = classReq["query"]
    user = classReq["user"]
    examples = classReq.get("examples", [])
    file = classReq.get("file", None)
    labels = classReq.get("labels", None)
    temperature = classReq.get("temperature", 0.0)
    max_examples = classReq.get("max_examples", 200)
    logit_bias = classReq.get("logit_bias", None)
    return_prompt = classReq.get("return_prompt", False)
    return_metadata = classReq.get("return_metadata", False)
    expand = classReq.get("expand", None)
    user = classReq.get("user", None)

    # Do stuff

    # Return the result as JSON
    return {
        "object": "classification",
        "model": "ada",
        "data": [
            {
                "index": 0,
                "object": "text",
                "classification": "positive"
            }
        ],
        "usage": {
            "prompt_tokens": 5,
            "completion_tokens": 3,
            "total_tokens": 8,
        },
    }, 200