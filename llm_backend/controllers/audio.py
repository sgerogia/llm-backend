import connexion
import json
import logging

from . import logger


def createTranscription():
    # Get the JSON from the request
    trReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createTranscription: ' + json.dumps(trReq))

    file = trReq['file']
    model = trReq['model']
    prompt = trReq.get('prompt', '')
    response_format = trReq.get('response_format', 'json')
    temperature = trReq.get("temperature", 0)
    language = trReq.get("language", "en")

    # Do stuff

    # Return the result as JSON
    return {
        "text": "Hello world!",
    }, 200


def createTranslation():
    # Get the JSON from the request
    trReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createTranslation: ' + trReq)

    file = trReq['file']
    model = trReq['model']
    prompt = trReq.get('prompt', '')
    response_format = trReq.get('response_format', 'json')
    temperature = trReq.get("temperature", 0)

    # Do stuff

    # Return the result as JSON
    return {
        "text": "Hello world!",
    }, 200
