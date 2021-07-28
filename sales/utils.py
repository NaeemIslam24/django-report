import uuid


def genarae_code():
    code = str(uuid.uuid4())[0:12]

    return code
