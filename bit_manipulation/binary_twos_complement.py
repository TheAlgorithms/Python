def twos_complement(a: int) -> str:
    """
    Take in a negative integer 'a'.
    Return the two's complement representation of 'a'.

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
    if a > 0:
        raise ValueError("input must be a negative integer")
    binary_a_length = len(bin(a)[3:])
    twos_complement_a = bin(abs(a) - (1 << binary_a_length))[3:]
    twos_complement_a = ('1' + '0' * (binary_a_length - len(twos_complement_a)) +
                         twos_complement_a) if a < 0 else '0'
    return '0b' + twos_complement_a


if __name__ == "__main__":
    import doctest

    doctest.testmod()
