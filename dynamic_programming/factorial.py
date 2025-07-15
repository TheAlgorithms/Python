# Factorial of a number using memoization

from functools import lru_cache


@lru_cache
def factorial(num, _memo=None):
    """
    Returns the factorial of a non-negative integer using memoization.

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Number should not be negative.
    >>> [factorial(i) for i in range(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    if _memo is None:
        _memo = {}

    if num < 0:
        raise ValueError("Number should not be negative.")

    if num in _memo:
        return _memo[num]

    if num in (0, 1):
        _memo[num] = 1
    else:
        _memo[num] = num * factorial(num - 1, _memo)

    return _memo[num]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
