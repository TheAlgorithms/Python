B58_CHARSET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> bytes:
    """
    Encodes data using the Base58 encoding scheme (Bitcoin-style).

    Base58 is a binary-to-text encoding scheme used to represent large integers
    as alphanumeric text. It omits characters that are easily confused:
    ``0`` (zero), ``O`` (capital o), ``I`` (capital i), and ``l`` (lowercase L).

    Args:
        data: The bytes to encode.

    Returns:
        The Base58-encoded bytes.

    Examples:
        >>> base58_encode(b"")
        b''
        >>> base58_encode(b"\\x00\\x01")
        b'12'
        >>> base58_encode(b"Hello World!")
        b'2NEpo7TZRRrLZSi2U'
        >>> base58_encode(b"A")
        b'28'
    """
    # Make sure the supplied data is a bytes-like object
    if not isinstance(data, bytes):
        msg = f"a bytes-like object is required, not '{data.__class__.__name__}'"
        raise TypeError(msg)

    # Convert bytes to a big integer
    num = int.from_bytes(data, "big")

    # Count leading zero bytes (each becomes a leading '1' in Base58)
    leading_zeros = len(data) - len(data.lstrip(b"\x00"))

    # Encode the number using base-58 division
    encoded = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encoded = B58_CHARSET[rem] + encoded

    return b"1" * leading_zeros + encoded.encode()


def base58_decode(encoded: str) -> bytes:
    """
    Decodes Base58-encoded data back to bytes.

    This is the inverse of :func:`base58_encode`. Leading ``1`` characters are
    converted back to leading zero bytes.

    Args:
        encoded: The Base58-encoded string.

    Returns:
        The decoded bytes.

    Examples:
        >>> base58_decode(b"")
        b''
        >>> base58_decode(b"12")
        b'\\x00\\x01'
        >>> base58_decode(b"2NEpo7TZRRrLZSi2U")
        b'Hello World!'
        >>> base58_decode(b"28")
        b'A'
    """
    # Make sure encoded_data is either a string or a bytes-like object
    if not isinstance(encoded, bytes) and not isinstance(encoded, str):
        msg = (
            "argument should be a bytes-like object or ASCII string, "
            f"not '{encoded.__class__.__name__}'"
        )
        raise TypeError(msg)

    # In case encoded_data is a bytes-like object, convert it to a string
    if isinstance(encoded, bytes):
        try:
            encoded = encoded.decode("ascii")
        except UnicodeDecodeError:
            raise ValueError("base58 encoded data should only contain ASCII characters")

    # Check if the encoded string contains non base58 characters
    if not all(char in B58_CHARSET for char in encoded):
        raise ValueError("Invalid base58 character(s) found.")

    # Count leading '1' characters (each becomes a leading zero byte)
    leading_ones = len(encoded) - len(encoded.lstrip("1"))

    # Convert from Base58 to a big integer
    num = 0
    for char in encoded:
        num = num * 58 + B58_CHARSET.index(char)

    # Convert the integer to bytes
    decoded = num.to_bytes((num.bit_length() + 7) // 8, "big") if num > 0 else b""

    return b"\x00" * leading_ones + decoded


if __name__ == "__main__":
    import doctest

    doctest.testmod()
