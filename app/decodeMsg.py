import base64


def decodeData(message):

    data_bytes = message.encode("utf-8")

    message_bytes = base64.b64decode(data_bytes)
    message = message_bytes.decode("utf-8")

    return message