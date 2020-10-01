# Factorial of a number using memoization

from functools import lru_cache


@lru_cache
def factorial(num: int) -> int:
    """
    >>> factorial(7)
    5040
    >>> factorial(-1)
    Traceback (most recent call last):
      ...
    ValueError: Number should not be negative.
    >>> [factorial(i) for i in range(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    if num < 0:
        raise ValueError("Number should not be negative.")

    return 1 if num in (0, 1) else num * factorial(num - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
