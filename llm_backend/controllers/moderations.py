import connexion
import json
import logging

from . import logger


def createModeration():
    # Get the JSON from the request
    modReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("createModeration: " + json.dumps(modReq))

    input = modReq["input"]
    model = modReq.get("model", None)

    # Do stuff

    # Return the result as JSON
    return {
        "id": "1234",
        "model": "ada",
        "results": [
            {
                "flagged": True,
                "categories": {
                    "hate": True,
                    "hate/threatening": True,
                    "self-harm": False,
                    "sexual": False,
                    "sexual/minors": False,
                    "violence": False,
                    "violence/graphic": False,
                },
                "category_scores": {
                    "hate": 0.8,
                    "hate/threatening": 0.9,
                    "self-harm": 0.1,
                    "sexual": 0.2,
                    "sexual/minors": 0.2,
                    "violence": 0.14,
                    "violence/graphic": 0.1,
                },
            }
        ],
    }, 200
