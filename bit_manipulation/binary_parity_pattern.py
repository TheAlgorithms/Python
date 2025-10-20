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
    '0b1001'
    >>> binary_parity_pattern(7)
    '0b101'
    >>> binary_parity_pattern(4)
    '0b111'
    >>> binary_parity_pattern(0)
    '0b0'
    """
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return "0b0"
    
    binary_str = bin(number)[2:]
    cum_sum = 0
    pattern = []

    for bit in binary_str:
        cum_sum += int(bit)
        pattern.append(str(cum_sum % 2))

    result = ''.join(pattern).lstrip('0')
    return '0b' + (result if result else '0')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
