def ceil(x) -> int:
    """
    Return the ceiling of x as an Integral.

    :param x: the number
    :return: the smallest integer >= x.

    >>> import math
    >>> ceil(1) == math.ceil(1)
    True
    >>> ceil(-1) == math.ceil(-1)
    True
    >>> ceil(0) == math.ceil(0)
    True
    >>> ceil(-0) == math.ceil(-0)
    True
    >>> ceil(1.1) == math.ceil(1.1)
    True
    >>> ceil(-1.1) == math.ceil(-1.1)
    True
    >>> ceil(-1.0) == math.ceil(-1.0)
    True
    """
    return x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
