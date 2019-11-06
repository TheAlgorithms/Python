def ceil(x) -> int:
    """
    Return the ceiling of x as an Integral.

    :param x: the number
    :return: the smallest integer >= x.

    >>> import math
    >>> all(ceil(n) == math.ceil(n) for n in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True
    """
    return x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
