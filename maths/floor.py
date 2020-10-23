def floor(x) -> int:
    """
    Return the floor of x as an Integral.

    :param x: the number
    :return: the largest integer <= x.

    >>> import math
    >>> all(floor(n) == math.floor(n) for n
    ...     in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True
    """
    return (
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
