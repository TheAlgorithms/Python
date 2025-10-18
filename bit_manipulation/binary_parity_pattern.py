"""
=======================================
⚖️ Binary Parity Pattern
=======================================

Generates a binary pattern where each bit represents 
the parity (even/odd) of the cumulative sum of bits 
in the original binary representation.

Example:
    13 (1101) → cumulative sums [1,2,3,4]
    parity pattern = 1010
"""

def binary_parity_pattern(number: int) -> str:
    """
    Generate parity pattern of cumulative binary sums.

    >>> binary_parity_pattern(13)
    '0b1010'
    >>> binary_parity_pattern(7)
    '0b111'
    >>> binary_parity_pattern(4)
    '0b10'
    """
    if number < 0:
        number = abs(number)

    binary = bin(number)[2:]
    parity_pattern = ""
    cum_sum = 0

    for bit in binary:
        cum_sum += int(bit)
        parity_pattern += str(cum_sum % 2)

    return "0b" + parity_pattern


if __name__ == "__main__":
    import doctest
    doctest.testmod()
