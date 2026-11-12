"""
Base32 encoding and decoding

https://en.wikipedia.org/wiki/Base32
"""

B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_encode(data: bytes) -> bytes:
    """
    >>> base32_encode(b"Hello World!")
    b'JBSWY3DPEBLW64TMMQQQ===='
    >>> base32_encode(b"123456")
    b'GEZDGNBVGY======'
    >>> base32_encode(b"some long complex string")
    b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY='
    >>> list(base32_encode(bytes([104, 233, 108, 108, 111])))
    [78, 68, 85, 87, 89, 51, 68, 80, 65, 61, 61, 61, 61, 61, 61, 61]
    >>> list(base32_encode(bytes([255, 254, 1])))
    [55, 55, 55, 65, 67, 61, 61, 61]
    """
    binary_data = "".join(bin(byte)[2:].zfill(8) for byte in data)
    binary_data = binary_data.ljust(5 * ((len(binary_data) // 5) + 1), "0")
    b32_chunks = map("".join, zip(*[iter(binary_data)] * 5))
    b32_result = "".join(B32_CHARSET[int(chunk, 2)] for chunk in b32_chunks)
    return bytes(b32_result.ljust(8 * ((len(b32_result) // 8) + 1), "="), "utf-8")


def base32_decode(data: bytes) -> bytes:
    """
    >>> base32_decode(b'JBSWY3DPEBLW64TMMQQQ====')
    b'Hello World!'
    >>> base32_decode(b'GEZDGNBVGY======')
    b'123456'
    >>> base32_decode(b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY=')
    b'some long complex string'
    >>> list(base32_decode(b'NDUWY3DPA======='))
    [104, 233, 108, 108, 111]
    >>> list(base32_decode(b'777AC==='))
    [255, 254, 1]
    """
    binary_chunks = "".join(
        bin(B32_CHARSET.index(_d))[2:].zfill(5)
        for _d in data.decode("ascii").strip("=")
    )
    binary_data = list(map("".join, zip(*[iter(binary_chunks)] * 8)))
    return bytes(int(_d, 2) for _d in binary_data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
