import connexion
import json
import logging

from . import logger


def createFineTune():
    # Get the JSON from the request
    ftReq = connexion.request.json
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('createFineTune: ' + json.dumps(ftReq))

    training_file = ftReq['training_file']
    validation_file = ftReq.get('validation_file', None)
    model = ftReq.get('model', None)
    n_epochs = ftReq.get('n_epochs', None)
    batch_size = ftReq.get('batch_size', None)
    learning_rate_multiplier = ftReq.get('learning_rate_multiplier', None)
    prompt_loss_weight = ftReq.get('prompt_loss_weight', None)
    compute_classification_metrics = ftReq.get('compute_classification_metrics', None)
    classification_n_classes = ftReq.get('classification_n_classes', None)
    classification_positive_class = ftReq.get('classification_positive_class', None)
    classification_betas = ftReq.get('classification_betas', None)
    suffix = ftReq.get('suffix', None)

    # Do stuff

    return {
        "id": "1234",
        "object": "finetune",
        "created_at": 1610878670,
        "updated_at": 1610878670,
        "model": "ada",
        "fine_tuned_model": "ada-ft",
        "organization_id": "openai",
        "status": "running",
        "hyperparams": {
            "n_epochs": 3,
        },
        "training_files": [
            {
                "object": "file",
                "id": "ada",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
        "validation_files": [
            {
                "object": "file",
                "id": "ada",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
        "result_files": [
            {
                "object": "file",
                "id": "ada",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
        "events": [
            {
                "object": "event",
                "created_at": 1610878670,
                "level": "info",
                "message": "foo",
            },
        ],
    }, 200


def listFineTunes():
    return [
        {
            "id": "1234",
            "object": "finetune",
            "created_at": 1610878670,
            "updated_at": 1610878670,
            "model": "ada",
            "fine_tuned_model": "ada-ft",
            "organization_id": "openai",
            "status": "running",
            "hyperparams": {
                "n_epochs": 3,
            },
            "training_files": [
                {
                    "object": "file",
                    "id": "ada",
                    "bytes": 123,
                    "created_at": 1610878670,
                    "filename": "foo.txt",
                    "purpose": "prompt",
                    "status": "ready",
                },
            ],
            "validation_files": [
                {
                    "object": "file",
                    "id": "ada",
                    "bytes": 123,
                    "created_at": 1610878670,
                    "filename": "foo.txt",
                    "purpose": "prompt",
                    "status": "ready",
                },
            ],
            "result_files": [
                {
                    "object": "file",
                    "id": "ada",
                    "bytes": 123,
                    "created_at": 1610878670,
                    "filename": "foo.txt",
                    "purpose": "prompt",
                    "status": "ready",
                },
            ],
            "events": [
                {
                    "object": "event",
                    "created_at": 1610878670,
                    "level": "info",
                    "message": "foo",
                },
            ],
        },
    ], 200


def retrieveFineTune(ftId):
    return {
            "id": "1234",
            "object": "finetune",
            "created_at": 1610878670,
            "updated_at": 1610878670,
            "model": "ada",
            "fine_tuned_model": "ada-ft",
            "organization_id": "openai",
            "status": "running",
            "hyperparams": {
                "n_epochs": 3,
            },
            "training_files": [
                {
                    "object": "file",
                    "id": "ada",
                    "bytes": 123,
                    "created_at": 1610878670,
                    "filename": "foo.txt",
                    "purpose": "prompt",
                    "status": "ready",
                },
            ],
            "validation_files": [
                {
                    "object": "file",
                    "id": "ada",
                    "bytes": 123,
                    "created_at": 1610878670,
                    "filename": "foo.txt",
                    "purpose": "prompt",
                    "status": "ready",
                },
            ],
            "result_files": [
                {
                    "object": "file",
                    "id": "ada",
                    "bytes": 123,
                    "created_at": 1610878670,
                    "filename": "foo.txt",
                    "purpose": "prompt",
                    "status": "ready",
                },
            ],
            "events": [
                {
                    "object": "event",
                    "created_at": 1610878670,
                    "level": "info",
                    "message": "foo",
                },
            ],
        }, 200

def cancelFineTune(ftId):
    return {
        "id": "1234",
        "object": "finetune",
        "created_at": 1610878670,
        "updated_at": 1610878670,
        "model": "ada",
        "fine_tuned_model": "ada-ft",
        "organization_id": "openai",
        "status": "running",
        "hyperparams": {
            "n_epochs": 3,
        },
        "training_files": [
            {
                "object": "file",
                "id": "ada",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
        "validation_files": [
            {
                "object": "file",
                "id": "ada",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
        "result_files": [
            {
                "object": "file",
                "id": "ada",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
        "events": [
            {
                "object": "event",
                "created_at": 1610878670,
                "level": "info",
                "message": "foo",
            },
        ],
    }, 200


def listFineTuneEvents(ftId, stream):
    return {
        "object": "finetune",
        "data": [
            {
                "object": "event",
                "created_at": 1610878670,
                "level": "info",
                "message": "foo",
            },
        ],
    }, 200
