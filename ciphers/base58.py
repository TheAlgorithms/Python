"""Base58 Encoding and Decoding.

Base58 is a binary-to-text encoding scheme used in cryptocurrencies such as Bitcoin.
It is designed to be human-friendly by omitting visually ambiguous characters:
0 (zero), O (capital o), I (capital i), and l (lower case L), as well as
non-alphanumeric characters like + and / found in Base64.

Reference:
https://en.bitcoin.it/wiki/Base58Check_encoding
"""

B58_CHARSET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    """Encodes bytes into a Base58 string using the canonical Bitcoin alphabet.

    Leading zero bytes (b'\\x00') are encoded as leading '1's.

    >>> base58_encode(b"Hello World")
    'JxF12TrwUP45BMd'
    >>> base58_encode(b"\\x00\\x01")
    '12'
    >>> base58_encode(b"\\x00\\x00\\x00")
    '111'
    >>> base58_encode(b"")
    ''
    >>> base58_encode(b"The quick brown fox jumps over the lazy dog.")
    'USm3fpXnKG5EUBx2ndxBDMPVciP5hGey2Jh4NDv6gmeo1LkMeiKrLJUUBk6Z'
    >>> base58_encode("invalid")
    Traceback (most recent call last):
      ...
    TypeError: a bytes-like object is required, not 'str'
    """
    if not isinstance(data, (bytes, bytearray)):
        msg = f"a bytes-like object is required, not '{data.__class__.__name__}'"
        raise TypeError(msg)

    if not data:
        return ""

    leading_zeros = 0
    for byte in data:
        if byte == 0:
            leading_zeros += 1
        else:
            break

    num = int.from_bytes(data, byteorder="big")
    encoded_chars: list[str] = []
    while num > 0:
        num, remainder = divmod(num, 58)
        encoded_chars.append(B58_CHARSET[remainder])

    return B58_CHARSET[0] * leading_zeros + "".join(reversed(encoded_chars))


def base58_decode(encoded_data: str) -> bytes:
    """Decodes a Base58 encoded string back into bytes.

    Leading '1's are decoded into leading zero bytes (b'\\x00').

    >>> base58_decode("JxF12TrwUP45BMd")
    b'Hello World'
    >>> base58_decode("12")
    b'\\x00\\x01'
    >>> base58_decode("111")
    b'\\x00\\x00\\x00'
    >>> base58_decode("")
    b''
    >>> base58_decode("USm3fpXnKG5EUBx2ndxBDMPVciP5hGey2Jh4NDv6gmeo1LkMeiKrLJUUBk6Z")
    b'The quick brown fox jumps over the lazy dog.'
    >>> base58_decode(12345)
    Traceback (most recent call last):
      ...
    TypeError: argument should be a string, not 'int'
    >>> base58_decode("0OIl")
    Traceback (most recent call last):
      ...
    ValueError: Non-base58 character found: '0'
    """
    if not isinstance(encoded_data, str):
        msg = f"argument should be a string, not '{encoded_data.__class__.__name__}'"
        raise TypeError(msg)

    if not encoded_data:
        return b""

    leading_ones = 0
    for char in encoded_data:
        if char == B58_CHARSET[0]:
            leading_ones += 1
        else:
            break

    num = 0
    for char in encoded_data:
        idx = B58_CHARSET.find(char)
        if idx == -1:
            msg = f"Non-base58 character found: '{char}'"
            raise ValueError(msg)
        num = num * 58 + idx

    if num == 0:
        return b"\x00" * leading_ones

    byte_length = (num.bit_length() + 7) // 8
    res = num.to_bytes(byte_length, byteorder="big")
    return b"\x00" * leading_ones + res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
