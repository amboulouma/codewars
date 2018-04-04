from base64 import b64encode, b64decode


def to_base_64(a):
    return b64encode(a).rstrip('=')


def from_base_64(s):
    missing_padding = 4 - len(s) % 4
    if missing_padding:
        s += b'=' * missing_padding
    return b64decode(s)