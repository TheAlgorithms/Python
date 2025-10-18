"""
All divisors of a number.

This module provides a function to compute all positive divisors of an integer.

Reference:
https://en.wikipedia.org/wiki/Divisor

Examples
--------
>>> all_divisors(1)
[1]
>>> all_divisors(28)
[1, 2, 4, 7, 14, 28]
>>> all_divisors(-6)
[1, 2, 3, 6]
>>> all_divisors(16)
[1, 2, 4, 8, 16]
"""

from math import isqrt


def all_divisors(n: int) -> list[int]:
    """
    Return a sorted list of all positive divisors of n.

    Parameters
    ----------
    n : int
        Integer for which to compute positive divisors. If n == 0 a ValueError
        is raised because the set of divisors of 0 is not finite.

    Returns
    -------
    List[int]
        Sorted list of positive divisors of abs(n).

    Raises
    ------
    ValueError
        If n == 0.

    Complexity
    ----------
    Runs in O(sqrt(n)) time.

    Doctests
    --------
    >>> all_divisors(1)
    [1]
    >>> all_divisors(28)
    [1, 2, 4, 7, 14, 28]
    >>> all_divisors(-6)
    [1, 2, 3, 6]
    >>> all_divisors(36)
    [1, 2, 3, 4, 6, 9, 12, 18, 36]
    """
    if n == 0:
        raise ValueError("Divisors of 0 are not defined (infinite).")

    n_abs = abs(n)
    divisors: list[int] = []

    for i in range(1, isqrt(n_abs) + 1):
        if n_abs % i == 0:
            divisors.append(i)
            j = n_abs // i
            if j != i:
                divisors.append(j)

    return sorted(divisors)


if __name__ == "_main_":
    import doctest

    doctest.testmod()
