# Information on 2's complement: https://en.wikipedia.org/wiki/Two%27s_complement


def twos_complement(number: int) -> str:
    """
    Take in a negative integer 'number'.
    Return the two's complement representation of 'number'.
    Two's complement is a method for representing negative integers in binary.
    It allows simple hardware implementation of arithmetic operations on both
    positive and negative numbers.
    Algorithm:
    1. For a negative number, determine how many bits are needed
    2. Calculate the two's complement: abs(number) is subtracted from 2^(bits needed)
    3. Convert result to binary and pad with leading zeros if needed
    Why it works: Two's complement = (NOT of positive part) + 1
    For example, -5: 5 is 0b0101, NOT is 0b1010, adding 1 gives 0b1011
    Example: -5 in 4-bit two's complement
    - Original positive: 5 = 0b0101
    - Invert bits: 0b1010 (this is one's complement)
    - Add 1: 0b1010 + 1 = 0b1011 (this is two's complement, represents -5)
    >>> twos_complement(0)
    '0b0'
    >>> twos_complement(-1)
    '0b11'
    >>> twos_complement(-5)
    '0b1011'
    >>> twos_complement(-17)
    '0b101111'
    >>> twos_complement(-207)
    '0b100110001'
    >>> twos_complement(1)
    Traceback (most recent call last):
        ...
    ValueError: input must be a negative integer
    """
    if number > 0:
        raise ValueError("input must be a negative integer")
    binary_number_length = len(bin(number)[3:])
    twos_complement_number = bin(abs(number) - (1 << binary_number_length))[3:]
    twos_complement_number = (
        (
            "1"
            + "0" * (binary_number_length - len(twos_complement_number))
            + twos_complement_number
        )
        if number < 0
        else "0"
    )
    return "0b" + twos_complement_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
