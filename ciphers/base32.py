import base64


def base32_encode(string: str) -> bytes:
    """
    Encodes a given string to base32, returning a bytes-like object
    >>> base32_encode("Hello World!")
    b'JBSWY3DPEBLW64TMMQQQ===='
    >>> base32_encode("123456")
    b'GEZDGNBVGY======'
    >>> base32_encode("some long complex string")
    b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY='
    """

    # encoded the input (we need a bytes like object)
    # then, b32encoded the bytes-like object
    return base64.b32encode(string.encode("utf-8"))


def base32_decode(encoded_bytes: bytes) -> str:
    """
    Decodes a given bytes-like object to a string, returning a string
    >>> base32_decode(b'JBSWY3DPEBLW64TMMQQQ====')
    'Hello World!'
    >>> base32_decode(b'GEZDGNBVGY======')
    '123456'
    >>> base32_decode(b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY=')
    'some long complex string'
    """

    # decode the bytes from base32
    # then, decode the bytes-like object to return as a string
    return base64.b32decode(encoded_bytes).decode("utf-8")


if __name__ == "__main__":
    test = "Hello World!"
    encoded = base32_encode(test)
    print(encoded)

    decoded = base32_decode(encoded)
    print(decoded)
