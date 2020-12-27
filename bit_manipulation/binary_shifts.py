from binary_twos_complement import twos_complement


def logical_left_shift(a: int, b: int) -> str:
    """
    Take in 2 positive integers.
    'a' is the integer to be logically left shifted 'b' times.
    i.e. (a << b)
    Return the shifted binary representation.

    >>> logical_left_shift(0, 1)
    '0b00'
    >>> logical_left_shift(1, 1)
    '0b10'
    >>> logical_left_shift(1, 5)
    '0b100000'
    >>> logical_left_shift(17, 2)
    '0b1000100'
    >>> logical_left_shift(1983, 4)
    '0b111101111110000'
    >>> logical_left_shift(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: both inputs must be positive integers
    """
    if a < 0 or b < 0:
        raise ValueError("both inputs must be positive integers")

    binary_a = str(bin(a))
    binary_a += '0' * b
    return binary_a


def logical_right_shift(a: int, b: int) -> str:
    """
    Take in positive 2 integers.
    'a' is the integer to be logically right shifted 'b' times.
    i.e. (a >> b)
    Return the shifted binary representation.

    >>> logical_right_shift(0, 1)
    '0b0'
    >>> logical_right_shift(1, 1)
    '0b0'
    >>> logical_right_shift(1, 5)
    '0b0'
    >>> logical_right_shift(17, 2)
    '0b100'
    >>> logical_right_shift(1983, 4)
    '0b1111011'
    >>> logical_right_shift(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: both inputs must be positive integers
    """
    if a < 0 or b < 0:
        raise ValueError("both inputs must be positive integers")

    binary_a = str(bin(a))[2:]
    if b >= len(binary_a):
        return '0b0'
    shifted_binary_a = binary_a[:len(binary_a) - b]
    return '0b' + shifted_binary_a


def arithmetic_right_shift(a: int, b: int) -> str:
    """
    Take in 2 integers.
    'a' is the integer to be arithmetically right shifted 'b' times.
    Return the shifted binary representation.

    >>> arithmetic_right_shift(0, 1)
    '0b00'
    >>> arithmetic_right_shift(1, 1)
    '0b00'
    >>> arithmetic_right_shift(-1, 1)
    '0b11'
    >>> arithmetic_right_shift(17, 2)
    '0b000100'
    >>> arithmetic_right_shift(-17, 2)
    '0b111011'
    >>> arithmetic_right_shift(-1983, 4)
    '0b111110000100'
    """
    if a >= 0:
        binary_a = '0' + str(bin(a)).strip('-')[2:]
    else:
        binary_a = twos_complement(a)[2:]

    if b >= len(binary_a):
        return '0b' + binary_a[0] * len(binary_a)
    return '0b' + binary_a[0] * b + binary_a[:len(binary_a) - b]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
