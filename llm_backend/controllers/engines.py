import connexion
import json
import logging

from . import logger


def listEngines():
    # Return the result as JSON
    return {
        "object": "list",
        "data": [
            {
                "id": "ada",
                "object": "engine",
                "owner": "openai",
                "ready": True,
                "created": 1610878670,
            },
        ],
    }, 200


def retrieveEngine(engineId):
    return {
        "id": "ada",
        "object": "engine",
        "owner": "openai",
        "ready": True,
        "created": 1610878670,
    }, 200


def createSearch(engineId):
    # Get the JSON from the request
    searchReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createSearch: ' + json.dumps(searchReq))

    query = searchReq['query']
    documents = searchReq.get("documents", None)
    file = searchReq.get("file", None)
    max_rerank = searchReq.get("max_rerank", None)
    return_metadata = searchReq.get("return_metadata", None)
    user = searchReq.get("user", None)

    # Do stuff

    return {
        "object": "result",
        "model": "ada",
        "data": [
            {
                "object": "document",
                "document": 12,
                "score": 0.8,
            }
        ],
    }, 200
