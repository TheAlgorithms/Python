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
    encoded = inp.encode("utf-8")  # encoded the input (we need a bytes like object)
    b16encoded = base64.b16encode(encoded)  # b16encoded the encoded string
    return b16encoded


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
    encoded = base64.b16decode(b16encoded)  #b16decoded the input
    return encoded.decode("utf-8")  # decoded the bytes like object to a string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
