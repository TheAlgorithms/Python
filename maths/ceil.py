"""
https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
"""


def ceil(x: float) -> int:
    """
    Return the ceiling of x as an Integral.

    :param x: the number
    :return: the smallest integer >= x.

    >>> import math
    >>> all(ceil(n) == math.ceil(n) for n
    ...     in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True
    """
    return int(x) if x - int(x) <= 0 else int(x) + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
