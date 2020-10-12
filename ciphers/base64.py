B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data: bytes) -> str:
    """Encodes data according to RFC4648.

    The data is first transformed to binary and appended with binary digits so that its
    length becomes a multiple of 6, then each 6 binary digits will match a character in
    the B64_CHARSET string. The number of appended binary digits would later determine
    how many "=" sign should be added, the padding.
    For every 2 binary digits added, a "=" sign is added in the output.
    We can add any binary digits to make it a multiple of 6, for instance, consider the
    following example:
    "AA" -> 0010100100101001 -> 001010 010010 1001
    As can be seen above, 2 more binary digits should be added, so there's 4
    possibilities here: 00, 01, 10 or 11.
    That being said, Base64 encoding can be used in Steganography to hide data in these
    appended digits.

    >>> base64_encode(b"This pull request is part of Hacktoberfest20!")
    'VGhpcyBwdWxsIHJlcXVlc3QgaXMgcGFydCBvZiBIYWNrdG9iZXJmZXN0MjAh'
    >>> base64_encode(b"https://tools.ietf.org/html/rfc4648")
    'aHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzQ2NDg='
    >>> base64_encode(b"A")
    'QQ=='
    """
    binary_stream = "".join(bin(char)[2:].zfill(8) for char in data)

    padding_needed = len(binary_stream) % 6 != 0

    if padding_needed:
        # The padding that will be added later
        padding = "=" * ((6 - len(binary_stream) % 6) // 2)

        # Append binary_stream with arbitrary binary digits (0's by default) to make its
        # length a multiple of 6.
        binary_stream += "0" * (6 - len(binary_stream) % 6)

    # Encode every 6 binary digits to their corresponding Base64 character
    encoded_data = "".join(
        B64_CHARSET[int(binary_stream[index : index + 6], 2)]
        for index in range(0, len(binary_stream), 6)
    )

    if padding_needed:
        return encoded_data + padding
    else:
        return encoded_data


def base64_decode(encoded_data: str) -> bytes:
    """Decodes data according to RFC4648.

    This does the reverse operation of base64_encode.
    We first transform the encoded data back to a binary stream, take off the
    previously appended binary digits according to the padding, at this point we
    would have a binary stream whose length is multiple of 8, the last step is
    to convert every 8 bits to a byte.

    >>> base64_decode("VGhpcyBwdWxsIHJlcXVlc3QgaXMgcGFydCBvZiBIYWNrdG9iZXJmZXN0MjAh")
    b'This pull request is part of Hacktoberfest20!'
    >>> base64_decode("aHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzQ2NDg=")
    b'https://tools.ietf.org/html/rfc4648'
    >>> base64_decode("QQ==")
    b'A'
    """
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
    assert len(encoded_data) % 4 == 0 and padding < 3, "Incorrect padding."

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
