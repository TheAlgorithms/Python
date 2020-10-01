
def count_setbits(a: int) -> int:
    """
    Take in 1 integer, return a number that is
    the number of 1's in binary representation of that number.

    >>> count_setbits(25)
    3
    >>> count_setbits(36)
    2
    >>> count_setbits(16)
    1
    >>> count_setbits(58)
    4
    >>> count_setbits(4294967295)
    32
    >>> count_setbits(0)
    0
    >>> count_setbits(-10)
    Traceback (most recent call last):
        ...
    ValueError: Input value must be a positive integer
    >>> count_setbits(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    >>> count_setbits("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0:
        raise ValueError("Input value must be a positive integer")
    elif isinstance(a, float):
        raise TypeError("Input value must be a 'int' type")
    return bin(a).count("1")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
