"""
== Raise base to the power of exponent using recursion ==
    Input -->
        Enter the base: 3
        Enter the exponent: 4
    Output  -->
        3 to the power of 4 is 81
    Input -->
        Enter the base: 2
        Enter the exponent: 0
    Output -->
        2 to the power of 0 is 1
"""


def power(base: int, exponent: int) -> float:
    """
    Calculate the power of a base raised to an exponent.

    Args:
    base (int): Base number 
    exponent (int): Exponent to apply to base number

    Returns:
    A float is returned that is the base number to the power of the exponent number

    Examples:
    >>> power(3, 4)
    81
    >>> power(2, 0)
    1
    >>> all(power(base, exponent) == pow(base, exponent)
    ...     for base in range(-10, 10) for exponent in range(10))
    True
    >>> power('a', 1)
    'a'
    >>> power('a', 2)
    Traceback (most recent call last):
        ...
    TypeError: can't multiply sequence by non-int of type 'str'
    >>> power('a', 'b')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'int'
    >>> power(2, -1)
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded
    """
    return base * power(base, (exponent - 1)) if exponent else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
