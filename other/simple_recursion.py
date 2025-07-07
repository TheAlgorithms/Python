"""
Simple Recursion Examples.

This module contains a few basic examples of recursion for beginners.

Functions:
- factorial(n): Calculate factorial of n.
- fibonacci(n): Calculate nth Fibonacci number.
- sum_of_digits(n): Calculate sum of digits of n.

Each function has doctests to verify correct behavior.
"""


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.

    Examples:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): Non-negative integer index.

    Returns:
        int: nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(7)
    13
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of digits of a non-negative integer n using recursion.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Sum of digits of n.

    Raises:
        ValueError: If n is negative.

    Examples:
    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(0)
    0
    >>> sum_of_digits(999)
    27
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
