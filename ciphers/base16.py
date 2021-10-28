import base64


def encode_to_b16(inp: str) -> bytes:
    """
    Encodes a given utf-8 string into base-16.

    >>> encode_to_b16('Hello World!')
    b'48656C6C6F20576F726C6421'
    >>> encode_to_b16('HELLO WORLD!')
    b'48454C4C4F20574F524C4421'
    >>> encode_to_b16('')
    b''
    """
    # encode the input into a bytes-like object and then encode b16encode that
    return base64.b16encode(inp.encode("utf-8"))


def decode_from_b16(b16encoded: bytes) -> str:
    """
    Decodes from base-16 to a utf-8 string.

    >>> decode_from_b16(b'48656C6C6F20576F726C6421')
    'Hello World!'
    >>> decode_from_b16(b'48454C4C4F20574F524C4421')
    'HELLO WORLD!'
    >>> decode_from_b16(b'')
    ''
    """
    # b16decode the input into bytes and decode that into a human readable string
    return base64.b16decode(b16encoded).decode("utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
