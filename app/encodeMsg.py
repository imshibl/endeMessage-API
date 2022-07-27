import base64


def encodeData(message):
    msg_bytes = message.encode("utf-8")

    base64_bytes = base64.b64encode(msg_bytes)
    base64_msg = base64_bytes.decode("utf-8")

    return base64_msg

# aGVsbG8=