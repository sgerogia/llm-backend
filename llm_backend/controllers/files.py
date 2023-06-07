import connexion

def listFiles():
    # Return the result as JSON
    return {
        "object": "list",
        "data": [
            {
                "id": "ada",
                "object": "file",
                "bytes": 123,
                "created_at": 1610878670,
                "filename": "foo.txt",
                "purpose": "prompt",
                "status": "ready",
            },
        ],
    }, 200


def createFile():
    # Get all the fields
    fields = connexion.request.form
    files = connexion.request.files

    # Access a specific field
    purpose = fields.get('purpose')

    # Access a specific file
    file = files.get('file')

    # Do stuff

    # Return the result as JSON
    return {
        "object": "file",
        "id": "ada",
        "bytes": 123,
        "created_at": 1610878670,
        "filename": "foo.txt",
        "purpose": "prompt",
        "status": "ready",
    }, 200


def deleteFile(fileId):
    # Return the result as JSON
    return {
        "id": "ada",
        "object": "file",
        "deleted": True,
    }, 200


def retrieveFile(fileId):
    # Return the result as JSON
    return {
        "object": "file",
        "id": "ada",
        "bytes": 123,
        "created_at": 1610878670,
        "filename": "foo.txt",
        "purpose": "prompt",
        "status": "ready",
    }, 200


def downloadFile(fileId):
    # Return the result as JSON
    return {
        "object": "file",
        "id": "ada",
        "bytes": 123,
        "created_at": 1610878670,
        "filename": "foo.txt",
        "purpose": "prompt",
        "status": "ready",
    }, 200
