B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data: bytes) -> bytes:
    """Encodes data according to RFC4648.

    The data is first transformed to binary and appended with binary digits so that its
    length becomes a multiple of 6, then each 6 binary digits will match a character in
    the B64_CHARSET string. The number of appended binary digits would later determine
    how many "=" signs should be added, the padding.
    For every 2 binary digits added, a "=" sign is added in the output.
    We can add any binary digits to make it a multiple of 6, for instance, consider the
    following example:
    "AA" -> 0010100100101001 -> 001010 010010 1001
    As can be seen above, 2 more binary digits should be added, so there's 4
    possibilities here: 00, 01, 10 or 11.
    That being said, Base64 encoding can be used in Steganography to hide data in these
    appended digits.

    >>> from base64 import b64encode
    >>> a = b"This pull request is part of Hacktoberfest20!"
    >>> b = b"https://tools.ietf.org/html/rfc4648"
    >>> c = b"A"
    >>> base64_encode(a) == b64encode(a)
    True
    >>> base64_encode(b) == b64encode(b)
    True
    >>> base64_encode(c) == b64encode(c)
    True
    >>> base64_encode("abc")
    Traceback (most recent call last):
      ...
    TypeError: a bytes-like object is required, not 'str'
    """
    # Make sure the supplied data is a bytes-like object
    if not isinstance(data, bytes):
        msg = f"a bytes-like object is required, not '{data.__class__.__name__}'"
        raise TypeError(msg)

    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)

    padding_needed = len(binary_stream) % 6 != 0

    if padding_needed:
        # The padding that will be added later
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)

        # Append binary_stream with arbitrary binary digits (0's by default) to make its
        # length a multiple of 6.
        binary_stream += "0" * (6 - len(binary_stream) % 6)
    else:
        padding = b""

    # Encode every 6 binary digits to their corresponding Base64 character
    return (
        "".join(
            B64_CHARSET[int(binary_stream[index : index + 6], 2)]
            for index in range(0, len(binary_stream), 6)
        ).encode()
        + padding
    )


def base64_decode(encoded_data: str) -> bytes:
    """Decodes data according to RFC4648.

    This does the reverse operation of base64_encode.
    We first transform the encoded data back to a binary stream, take off the
    previously appended binary digits according to the padding, at this point we
    would have a binary stream whose length is multiple of 8, the last step is
    to convert every 8 bits to a byte.

    >>> from base64 import b64decode
    >>> a = "VGhpcyBwdWxsIHJlcXVlc3QgaXMgcGFydCBvZiBIYWNrdG9iZXJmZXN0MjAh"
    >>> b = "aHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzQ2NDg="
    >>> c = "QQ=="
    >>> base64_decode(a) == b64decode(a)
    True
    >>> base64_decode(b) == b64decode(b)
    True
    >>> base64_decode(c) == b64decode(c)
    True
    >>> base64_decode("abc")
    Traceback (most recent call last):
      ...
    AssertionError: Incorrect padding
    """
    # Make sure encoded_data is either a string or a bytes-like object
    if not isinstance(encoded_data, bytes) and not isinstance(encoded_data, str):
        msg = (
            "argument should be a bytes-like object or ASCII string, "
            f"not '{encoded_data.__class__.__name__}'"
        )
        raise TypeError(msg)

    # In case encoded_data is a bytes-like object, make sure it contains only
    # ASCII characters so we convert it to a string object
    if isinstance(encoded_data, bytes):
        try:
            encoded_data = encoded_data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("base64 encoded data should only contain ASCII characters")

    padding = encoded_data.count("=")

    # Check if the encoded string contains non base64 characters
    if padding:
        assert all(
            char in B64_CHARSET for char in encoded_data[:-padding]
        ), "Invalid base64 character(s) found."
    else:
        assert all(
            char in B64_CHARSET for char in encoded_data
        ), "Invalid base64 character(s) found."

    # Check the padding
    assert len(encoded_data) % 4 == 0 and padding < 3, "Incorrect padding"

    if padding:
        # Remove padding if there is one
        encoded_data = encoded_data[:-padding]

        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )[: -padding * 2]
    else:
        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )

    data = [
        int(binary_stream[index : index + 8], 2)
        for index in range(0, len(binary_stream), 8)
    ]

    return bytes(data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
