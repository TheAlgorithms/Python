"""Convert a Decimal Number to a Binary Number."""


def decimal_to_binary(num):
    """Convert a Decimal Number to a Binary Number."""

    """
        Convert a Integer Decimal Number to a Binary Number as str.
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(2)
        '10'
        >>> decimal_to_binary(7)
        '111'
        >>> decimal_to_binary(35)
        '100011'
        >>> # negatives work too
        >>> decimal_to_binary(-2)
        '-10'
        >>> # floats are acceptable if equivalent to an int
        >>> decimal_to_binary(2)
        '10'
        >>> # other floats will error
        >>> decimal_to_binary(16.16) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError
        >>> # strings will error as well
        >>> decimal_to_binary('0xfffff') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError
        >>> # results are the same when compared to Python's default bin function
        >>> decimal_to_binary(-256) == bin(-256)
        True
    """
    assert type(num) in (int, float) and num == int(num)

    if num == 0:
        return 0

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
