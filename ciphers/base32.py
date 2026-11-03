"""
Base32 encoding and decoding

https://en.wikipedia.org/wiki/Base32
"""

B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_encode(data: bytes) -> bytes:
    """
    >>> base32_encode(b"")
    b''
    >>> base32_encode(b"Hello World!")
    b'JBSWY3DPEBLW64TMMQQQ===='
    >>> base32_encode(b"123456")
    b'GEZDGNBVGY======'
    >>> base32_encode(b"some long complex string")
    b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY='
    >>> base32_encode("héllo".encode())
    b'NDB2S3DMN4======'
    """
    if not data:
        return b""
    binary_data = "".join(bin(byte)[2:].zfill(8) for byte in data)
    if (remainder := len(binary_data) % 5) != 0:
        binary_data = binary_data + "0" * (5 - remainder)
    b32_chunks = [binary_data[i : i + 5] for i in range(0, len(binary_data), 5)]
    b32_result = "".join(B32_CHARSET[int(chunk, 2)] for chunk in b32_chunks)
    pad_len = (8 - (len(b32_result) % 8)) % 8
    return (b32_result + "=" * pad_len).encode("ascii")


def base32_decode(data: bytes) -> bytes:
    """
    >>> base32_decode(b"")
    b''
    >>> base32_decode(b'JBSWY3DPEBLW64TMMQQQ====')
    b'Hello World!'
    >>> base32_decode(b'GEZDGNBVGY======')
    b'123456'
    >>> base32_decode(b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY=')
    b'some long complex string'
    >>> base32_decode(b'NDB2S3DMN4======').decode()
    'héllo'
    """
    if not data:
        return b""
    s = data.decode("ascii").strip("=")
    binary_chunks = "".join(bin(B32_CHARSET.index(c))[2:].zfill(5) for c in s)
    num_bytes = len(binary_chunks) // 8
    return bytes(int(binary_chunks[i : i + 8], 2) for i in range(0, num_bytes * 8, 8))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
