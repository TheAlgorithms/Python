import base64


def base16_encode(inp: str) -> bytes:
    """
    Encodes a given utf-8 string into base-16.

    >>> base16_encode('Hello World!')
    b'48656C6C6F20576F726C6421'
    >>> base16_encode('HELLO WORLD!')
    b'48454C4C4F20574F524C4421'
    >>> base16_encode('')
    b''
    """
    # encode the input into a bytes-like object and then encode b16encode that
    return base64.b16encode(inp.encode("utf-8"))


def base16_decode(b16encoded: bytes) -> str:
    """
    Decodes from base-16 to a utf-8 string.

    >>> base16_decode(b'48656C6C6F20576F726C6421')
    'Hello World!'
    >>> base16_decode(b'48454C4C4F20574F524C4421')
    'HELLO WORLD!'
    >>> base16_decode(b'')
    ''
    """
    # b16decode the input into bytes and decode that into a human readable string
    return base64.b16decode(b16encoded).decode("utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
