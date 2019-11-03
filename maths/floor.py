def floor(x) -> int:
    """
    Return the floor of x as an Integral.

    :param x: the number
    :return: the largest integer <= x.

    >>> import math
    >>> floor(1) == math.floor(1)
    True
    >>> floor(-1) == math.floor(-1)
    True
    >>> floor(0) == math.floor(0)
    True
    >>> floor(-0) == math.floor(-0)
    True
    >>> floor(1.1) == math.floor(1.1)
    True
    >>> floor(-1.1) == math.floor(-1.1)
    True
    >>> floor(-1.0) == math.floor(-1.0)
    True
    """
    return x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
