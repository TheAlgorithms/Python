"""
== Hexagonal Number ==
The nth hexagonal number hn is the number of distinct dots
in a pattern of dots consisting of the outlines of regular
hexagons with sides up to n dots, when the hexagons are
overlaid so that they share one vertex.

https://en.wikipedia.org/wiki/Hexagonal_number
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)


def hexagonal(number: int) -> int:
    """
    :param number: nth hexagonal number to calculate
    :return: the nth hexagonal number
    Note: A hexagonal number is only defined for positive integers
    >>> hexagonal(4)
    28
    >>> hexagonal(11)
    231
    >>> hexagonal(22)
    946
    >>> hexagonal(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer
    >>> hexagonal(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer
    >>> hexagonal(11.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=11.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        raise ValueError("Input must be a positive integer")
    return number * (2 * number - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
