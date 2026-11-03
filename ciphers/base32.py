"""
Base32 encoding and decoding

https://en.wikipedia.org/wiki/Base32
https://www.rfc-editor.org/rfc/rfc4648.html#section-6
"""

B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_encode(data: bytes) -> bytes:
    """
    Encode bytes into Base32 bytes per RFC 4648.

    >>> base32_encode(b"")
    b''
    >>> base32_encode(b"Hello World!")
    b'JBSWY3DPEBLW64TMMQQQ===='
    >>> base32_encode(b"123456")
    b'GEZDGNBVGY======'
    >>> base32_encode(b"some long complex string")
    b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY='
    >>> base32_encode(b"\\xff\\xfe\\x01")
    b'777AC==='
    >>> import base64
    >>> all(
    ...     base32_encode(bytes([i])) == base64.b32encode(bytes([i]))
    ...     for i in range(256)
    ... )
    True
    """
    if not isinstance(data, (bytes, bytearray)):
        msg = f"data must be bytes or bytearray, not {type(data).__name__}"
        raise TypeError(msg)

    if not data:
        return b""

    binary_data = "".join(bin(byte)[2:].zfill(8) for byte in data)
    pad_len = (5 - len(binary_data) % 5) % 5
    binary_data += "0" * pad_len
    b32_chunks = [binary_data[i : i + 5] for i in range(0, len(binary_data), 5)]
    b32_result = "".join(B32_CHARSET[int(chunk, 2)] for chunk in b32_chunks)
    pad_chars = (8 - len(b32_result) % 8) % 8
    return (b32_result + "=" * pad_chars).encode("ascii")


def base32_decode(data: bytes) -> bytes:
    """
    Decode Base32 bytes back into raw bytes.

    >>> base32_decode(b"")
    b''
    >>> base32_decode(b'JBSWY3DPEBLW64TMMQQQ====')
    b'Hello World!'
    >>> base32_decode(b'GEZDGNBVGY======')
    b'123456'
    >>> base32_decode(b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY=')
    b'some long complex string'
    >>> base32_decode(b'777AC===')
    b'\\xff\\xfe\\x01'
    >>> import base64
    >>> all(
    ...     base32_decode(base64.b32encode(bytes([i]))) == bytes([i])
    ...     for i in range(256)
    ... )
    True
    """
    if not isinstance(data, (bytes, bytearray)):
        msg = f"data must be bytes or bytearray, not {type(data).__name__}"
        raise TypeError(msg)

    cleaned = data.decode("ascii").rstrip("=")
    if not cleaned:
        return b""

    binary_chunks = "".join(
        bin(B32_CHARSET.index(char))[2:].zfill(5) for char in cleaned
    )
    num_bytes = len(binary_chunks) // 8
    return bytes(int(binary_chunks[i * 8 : (i + 1) * 8], 2) for i in range(num_bytes))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
