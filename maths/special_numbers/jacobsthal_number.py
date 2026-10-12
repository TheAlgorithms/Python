"""
Jacobsthal numbers

The Jacobsthal sequence starts with 0 and 1, and every later term is the
previous term plus twice the term before it:

    J(0) = 0
    J(1) = 1
    J(n) = J(n - 1) + 2 * J(n - 2)

The first terms are 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, ...

They also have the closed form J(n) = (2 ** n - (-1) ** n) / 3, which is used
below to cross-check the iterative result.

Source:
    https://en.wikipedia.org/wiki/Jacobsthal_number
    https://oeis.org/A001045
"""


def jacobsthal_number(n: int) -> int:
    """
    Return the nth Jacobsthal number, counting from J(0) = 0.

    :param n: index of the Jacobsthal number, must be a non-negative integer
    :return: the nth Jacobsthal number

    >>> jacobsthal_number(0)
    0
    >>> jacobsthal_number(1)
    1
    >>> jacobsthal_number(5)
    11
    >>> jacobsthal_number(10)
    341
    >>> jacobsthal_number(64)
    6148914691236517205
    >>> all(
    ...     jacobsthal_number(i) == (2**i - (-1) ** i) // 3 for i in range(100)
    ... )
    True
    >>> jacobsthal_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer, got -1
    >>> jacobsthal_number(2.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer, got 2.5
    >>> jacobsthal_number("3")
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer, got '3'
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        msg = f"n must be a non-negative integer, got {n!r}"
        raise ValueError(msg)

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, current + 2 * previous
    return previous


def jacobsthal_sequence(length: int) -> list[int]:
    """
    Return the first `length` Jacobsthal numbers as a list.

    :param length: how many terms to return, must be a non-negative integer
    :return: list of the first `length` Jacobsthal numbers

    >>> jacobsthal_sequence(0)
    []
    >>> jacobsthal_sequence(1)
    [0]
    >>> jacobsthal_sequence(11)
    [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341]
    >>> jacobsthal_sequence(-3)
    Traceback (most recent call last):
        ...
    ValueError: length must be a non-negative integer, got -3
    >>> jacobsthal_sequence(4.0)
    Traceback (most recent call last):
        ...
    ValueError: length must be a non-negative integer, got 4.0
    """
    if not isinstance(length, int) or isinstance(length, bool) or length < 0:
        msg = f"length must be a non-negative integer, got {length!r}"
        raise ValueError(msg)

    sequence = []
    previous, current = 0, 1
    for _ in range(length):
        sequence.append(previous)
        previous, current = current, current + 2 * previous
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
