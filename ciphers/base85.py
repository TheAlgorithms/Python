import base64


def base85_encode(string: str) -> bytes:
    """
    Encodes a given string to base85, returning a bytes-like object
    >>> base85_encode("Hello World!")
    b'87cURD]i,"Ebo80'
    >>> base85_encode("123456")
    b'0etOA2)Y'
    >>> base85_encode("some long complex string")
    b"F)Po,+Dbt6B-:]&D/a<&GT_'LEbTE("
    """

    # encode the input (we need a bytes like object)
    # then, a85encode the encoded string
    return base64.a85encode(string.encode("utf-8"))


def base85_decode(encoded_bytes: bytes) -> str:
    """
    Decodes a given bytes-like object to a string, returning a string
    >>> base85_decode(b'87cURD]i,"Ebo80')
    'Hello World!'
    >>> base85_decode(b'0etOA2)Y')
    '123456'
    >>> base85_decode(b"F)Po,+Dbt6B-:]&D/a<&GT_'LEbTE(")
    'some long complex string'
    """
    # decode the bytes from base85
    # then, decode the bytes-like object to return as a string
    return base64.a85decode(encoded_bytes).decode("utf-8")


if __name__ == "__main__":
    test = "Hello World!"
    encoded = base85_encode(test)
    print(encoded)

    decoded = base85_decode(encoded)
    print(decoded)
