BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58_encode(data: bytes) -> str:
    """Encodes data in Base58.

    Args:
        data (bytes): Data to be encoded.

    Returns:
        str: Base58 encoded string.
    """
    num = int.from_bytes(data, "big")
    encoded = ""
    while num > 0:
        num, rem = divmod(num, 58)
        encoded = BASE58_ALPHABET[rem] + encoded

    # Add '1' for each leading 0 byte
    n = 0
    for byte in data:
        if byte == 0:
            n += 1
        else:
            break
    return "1" * n + encoded


def base58_decode(s: str) -> bytes:
    """Decodes Base58 encoded string back to bytes.

    Args:
        s (str): Base58 encoded string.

    Returns:
        bytes: Decoded data.

    Raises:
        ValueError: If the string contains invalid Base58 characters.
    """
    num = 0
    for char in s:
        if char not in BASE58_ALPHABET:
            error_message = f"Invalid character '{char}' in Base58 string"
            raise ValueError(error_message)
        num *= 58
        num += BASE58_ALPHABET.index(char)

    # Convert the number to bytes
    combined = num.to_bytes((num.bit_length() + 7) // 8, "big")

    # Add leading zeros
    num_leading_zeros = len(s) - len(s.lstrip("1"))
    return b"\x00" * num_leading_zeros + combined


if __name__ == "__main__":
    import doctest

    doctest.testmod()
