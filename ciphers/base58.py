"""
Base58 encoding and decoding (Bitcoin alphabet)

Base58 is Base64 without the look-alike characters 0, O, I, l and without + and /.
Each leading zero byte is written as a leading "1" so that it survives the round trip.

https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58
"""

B58_CHARSET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> bytes:
    """
    Encode bytes as Base58.

    >>> base58_encode(b"")
    b''
    >>> base58_encode(b"\\x00\\x01")
    b'12'
    >>> base58_encode(b"\\x00\\x00")
    b'11'
    >>> base58_encode(b"Hello World!")
    b'2NEpo7TZRRrLZSi2U'
    >>> base58_encode("abc")
    Traceback (most recent call last):
      ...
    TypeError: a bytes-like object is required, not 'str'
    """
    if not isinstance(data, bytes):
        msg = f"a bytes-like object is required, not '{data.__class__.__name__}'"
        raise TypeError(msg)

    # Leading zero bytes add nothing to the integer value, so count them separately
    leading_zeros = len(data) - len(data.lstrip(b"\x00"))
    number = int.from_bytes(data, "big")

    digits = []
    while number:
        number, remainder = divmod(number, 58)
        digits.append(B58_CHARSET[remainder])

    return (B58_CHARSET[0] * leading_zeros + "".join(reversed(digits))).encode()


def base58_decode(encoded_data: str | bytes) -> bytes:
    """
    Decode Base58 (given as a string or bytes) back to bytes.

    >>> base58_decode("")
    b''
    >>> base58_decode("12")
    b'\\x00\\x01'
    >>> base58_decode(b"2NEpo7TZRRrLZSi2U")
    b'Hello World!'
    >>> base58_decode(base58_encode(b"\\x00\\x00\\xff"))
    b'\\x00\\x00\\xff'
    >>> base58_decode("0OIl")
    Traceback (most recent call last):
      ...
    ValueError: Invalid Base58 character: '0'
    >>> base58_decode(b"\\xff")
    Traceback (most recent call last):
      ...
    ValueError: Base58 encoded data should only contain ASCII characters
    >>> base58_decode(123)
    Traceback (most recent call last):
      ...
    TypeError: argument should be a bytes-like object or ASCII string, not 'int'
    """
    if not isinstance(encoded_data, (str, bytes)):
        msg = (
            "argument should be a bytes-like object or ASCII string, "
            f"not '{encoded_data.__class__.__name__}'"
        )
        raise TypeError(msg)

    # Accept bytes too, so the output of base58_encode can be decoded directly
    if isinstance(encoded_data, bytes):
        try:
            encoded_data = encoded_data.decode("ascii")
        except UnicodeDecodeError:
            msg = "Base58 encoded data should only contain ASCII characters"
            raise ValueError(msg) from None

    number = 0
    for char in encoded_data:
        if char not in B58_CHARSET:
            msg = f"Invalid Base58 character: {char!r}"
            raise ValueError(msg)
        number = number * 58 + B58_CHARSET.index(char)

    # Each leading "1" stands for one zero byte that the integer cannot hold
    leading_ones = len(encoded_data) - len(encoded_data.lstrip(B58_CHARSET[0]))
    body = number.to_bytes((number.bit_length() + 7) // 8, "big")
    return b"\x00" * leading_ones + body


if __name__ == "__main__":
    import doctest

    doctest.testmod()
