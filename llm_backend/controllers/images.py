import connexion
import json
import logging

from . import logger


def createImage():
    # Get the JSON from the request
    imgReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("createImage: " + json.dumps(imgReq))

    prompt = imgReq["prompt"]
    n = imgReq.get("n", None)
    size = imgReq.get("size", None)
    response_format = imgReq.get("response_format", None)
    user = imgReq.get("user", None)

    # Do stuff

    # Return the result as JSON
    return {
        "created": 1610878670,
        "data": [
            {
                "url": "https://www.foo.com/img.jpeg",
            }
        ],
    }, 200


def createImageEdit():
    # Get the JSON from the request
    imgReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("createImageEdit: " + json.dumps(imgReq))

    image = imgReq["image"]
    mask = imgReq.get("mask", None)
    prompt = imgReq["prompt"]
    n = imgReq.get("n", None)
    size = imgReq.get("size", None)
    response_format = imgReq.get("response_format", None)
    user = imgReq.get("user", None)

    # Do stuff

    # Return the result as JSON
    return {
        "created": 1610878670,
        "data": [
            {
                "url": "https://www.foo.com/img.jpeg",
            }
        ],
    }, 200


def createImageVariation():
    # Get the JSON from the request
    imgReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("createImageVariation: " + json.dumps(imgReq))

    image = imgReq["image"]
    n = imgReq.get("n", None)
    size = imgReq.get("size", None)
    response_format = imgReq.get("response_format", None)
    user = imgReq.get("user", None)

    # Do stuff

    # Return the result as JSON
    return {
        "created": 1610878670,
        "data": [
            {
                "url": "https://www.foo.com/img.jpeg",
            }
        ],
    }, 200
