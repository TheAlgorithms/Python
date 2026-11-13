"""
Base85 (Ascii85) encoding and decoding

https://en.wikipedia.org/wiki/Ascii85
"""


def ascii85_encode(data: bytes) -> bytes:
    """
    Encode bytes into Ascii85 (Base85) bytes.

    >>> ascii85_encode(b"")
    b''
    >>> ascii85_encode(b"12345")
    b'0etOA2#'
    >>> ascii85_encode(b"base 85")
    b'@UX=h+?24'
    >>> ascii85_encode(b"\\xff\\xfe\\xfd")
    b's8Mr'
    >>> import base64
    >>> all(
    ...     ascii85_encode(bytes([i])) == base64.a85encode(bytes([i]))
    ...     for i in range(256)
    ... )
    True
    """
    if not data:
        return b""
    result = bytearray()
    for i in range(0, len(data), 4):
        chunk = data[i : i + 4]
        pad = 4 - len(chunk)
        chunk_padded = chunk + b"\x00" * pad
        val = int.from_bytes(chunk_padded, "big")
        chars = bytearray(5)
        for j in range(4, -1, -1):
            chars[j] = (val % 85) + 33
            val //= 85
        if pad:
            result.extend(chars[: 5 - pad])
        else:
            result.extend(chars)
    return bytes(result)


def ascii85_decode(data: bytes) -> bytes:
    """
    Decode Ascii85 (Base85) bytes back to original bytes.

    >>> ascii85_decode(b"")
    b''
    >>> ascii85_decode(b"0etOA2#")
    b'12345'
    >>> ascii85_decode(b"@UX=h+?24")
    b'base 85'
    >>> ascii85_decode(b"s8Mr")
    b'\\xff\\xfe\\xfd'
    >>> ascii85_decode(b"!")
    Traceback (most recent call last):
        ...
    ValueError: Invalid Ascii85 length
    >>> ascii85_decode(b"~~")
    Traceback (most recent call last):
        ...
    ValueError: Character '~' out of Ascii85 range
    """
    if not data:
        return b""
    rem = len(data) % 5
    pad = (5 - rem) % 5
    if rem == 1:
        raise ValueError("Invalid Ascii85 length")
    padded = data + b"u" * pad
    result = bytearray()
    for i in range(0, len(padded), 5):
        chunk = padded[i : i + 5]
        val = 0
        for b in chunk:
            if not (33 <= b <= 117):
                msg = f"Character {chr(b)!r} out of Ascii85 range"
                raise ValueError(msg)
            val = val * 85 + (b - 33)
        if val > 0xFFFFFFFF:
            raise ValueError("Ascii85 chunk value overflow")
        result.extend(val.to_bytes(4, "big"))
    if pad:
        return bytes(result[:-pad])
    return bytes(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
