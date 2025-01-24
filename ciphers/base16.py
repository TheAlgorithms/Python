def base16_encode(data: bytes) -> str:
    """
    Encodes the given bytes into base16.

    >>> base16_encode(b'Hello World!')
    '48656C6C6F20576F726C6421'
    >>> base16_encode(b'HELLO WORLD!')
    '48454C4C4F20574F524C4421'
    >>> base16_encode(b'')
    ''
    """
    # Turn the data into a list of integers (where each integer is a byte),
    # Then turn each byte into its hexadecimal representation, make sure
    # it is uppercase, and then join everything together and return it.
    return "".join([hex(byte)[2:].zfill(2).upper() for byte in list(data)])


def base16_decode(data: str) -> bytes:
    """
    Decodes the given base16 encoded data into bytes.

    >>> base16_decode('48656C6C6F20576F726C6421')
    b'Hello World!'
    >>> base16_decode('48454C4C4F20574F524C4421')
    b'HELLO WORLD!'
    >>> base16_decode('')
    b''
    >>> base16_decode('486')
    Traceback (most recent call last):
      ...
    ValueError: Base16 encoded data is invalid:
    Data does not have an even number of hex digits.
    >>> base16_decode('48656c6c6f20576f726c6421')
    Traceback (most recent call last):
      ...
    ValueError: Base16 encoded data is invalid:
    Data is not uppercase hex or it contains invalid characters.
    >>> base16_decode('This is not base64 encoded data.')
    Traceback (most recent call last):
      ...
    ValueError: Base16 encoded data is invalid:
    Data is not uppercase hex or it contains invalid characters.
    """
    # Check data validity, following RFC3548
    # https://www.ietf.org/rfc/rfc3548.txt
    if (len(data) % 2) != 0:
        raise ValueError(
            """Base16 encoded data is invalid:
Data does not have an even number of hex digits."""
        )
    # Check the character set - the standard base16 alphabet
    # is uppercase according to RFC3548 section 6
    if not set(data) <= set("0123456789ABCDEF"):
        raise ValueError(
            """Base16 encoded data is invalid:
Data is not uppercase hex or it contains invalid characters."""
        )
    # For every two hexadecimal digits (= a byte), turn it into an integer.
    # Then, string the result together into bytes, and return it.
    return bytes(int(data[i] + data[i + 1], 16) for i in range(0, len(data), 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
