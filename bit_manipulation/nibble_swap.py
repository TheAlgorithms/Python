def nibble_swap(byte: int) -> int:
    """
    Swap the high and low nibbles of an 8-bit byte.

    :param byte: The input byte as an integer (0 to 255).
    :return: The result of swapping the high and low nibbles as an integer.

    >>> bin(nibble_swap(0b11011001))
    '0b10011101'
    >>> bin(nibble_swap(0b00001111))
    '0b11110000'
    """
    if byte < 0 or byte > 255:
        raise ValueError("Input byte must be in the range 0 to 255")

    high_nibble = (
        byte & 0xF0
    ) >> 4  # Extract the high nibble (bits 4-7) and shift it to the right
    low_nibble = (
        byte & 0x0F
    ) << 4  # Extract the low nibble (bits 0-3) and shift it to the left
    return high_nibble | low_nibble  # Combine the high and low nibbles


if __name__ == "__main__":
    import doctest

    doctest.testmod()
