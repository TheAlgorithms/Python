import base64


def base85_encode(string: str) -> bytes:
    """
    >>> base85_encode("")
    b''
    >>> base85_encode("12345")
    b'0etOA2#'
    >>> base85_encode("base 85")
    b'@UX=h+?24'
    """
    # encoded the input to a bytes-like object and then a85encode that
    return base64.a85encode(string.encode("utf-8"))


def base85_decode(a85encoded: bytes) -> str:
    """
    >>> base85_decode(b"")
    ''
    >>> base85_decode(b"0etOA2#")
    '12345'
    >>> base85_decode(b"@UX=h+?24")
    'base 85'
    """
    # a85decode the input into bytes and decode that into a human readable string
    return base64.a85decode(a85encoded).decode("utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
