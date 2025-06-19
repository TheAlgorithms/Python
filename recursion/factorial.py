"""
Fibonacci
https://en.wikipedia.org/wiki/Fibonacci_number
"""


def factorial(number: int) -> int:
    """
    Compute the factorial of a non-negative integer using recursion.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(10)
    3628800
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer.
    """
    if number < 0:
        raise ValueError("Input must be a non-negative integer.")
    if number == 0:
        return 1
    return number * factorial(number - 1)
