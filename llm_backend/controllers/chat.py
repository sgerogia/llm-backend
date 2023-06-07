import json
import logging

import connexion
import openai
from flask import Response, stream_with_context

from . import logger


def createChatCompletion():
    # Get the JSON from the request
    completionReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        req = json.dumps(completionReq)
        logger.debug(f"createChatCompletion: {req}")

    # top_p = completionReq.get('top_p', 1)
    # n = completionReq.get('n', 1)
    # stream = completionReq.get('stream', False)
    # stop = completionReq.get('stop', [])
    # max_tokens = completionReq.get('max_tokens', 48000)
    # presence_penalty = completionReq.get('presence_penalty', 0)
    # frequency_penalty = completionReq.get('frequency_penalty', 0)
    # logit_bias = completionReq.get('logit_bias', {})
    # user = completionReq.get('user', '')

    stream = completionReq.get('stream', False)

    # Call the API
    compl = openai.ChatCompletion.create(
        model=completionReq['model'],
        messages=completionReq['messages'],
        stream=stream,
        temperature=completionReq.get('temperature', 1),
    )

    if stream:
        return streamChat(compl)
    else:
        res = Response(json.dumps(compl), 200)
        res.headers['Content-Type'] = 'application/json'
        return res


def streamChat(compl):
    def iterate():
        for chunk in compl:
            s = json.dumps(chunk)
            yield f"data: {s}\n\n"
        yield f"data: [DONE]\n\n"
        
    return Response(stream_with_context(iterate()), mimetype="text/event-stream")