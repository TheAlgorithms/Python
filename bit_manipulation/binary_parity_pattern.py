"""
binary_parity_pattern.py
========================

Generates a binary parity pattern based on the cumulative sum of bits
in the binary representation of an integer.

Reference:
https://en.wikipedia.org/wiki/Parity_(mathematics)
"""


def binary_parity_pattern(number: int) -> str:
    """
    Return a binary parity pattern string for a given integer.

    >>> binary_parity_pattern(13)
    '0b1010'
    >>> binary_parity_pattern(7)
    '0b111'
    >>> binary_parity_pattern(4)
    '0b10'
    >>> binary_parity_pattern(0)
    '0b0'
    """
    if number < 0:
        raise ValueError("Number must be non-negative")

    binary_str = bin(number)[2:]
    cum_sum = 0
    pattern = []

    for bit in binary_str:
        cum_sum += int(bit)
        pattern.append(str(cum_sum % 2))

    result = "0b" + "".join(pattern)
    return result if result != "0b" else "0b0"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
