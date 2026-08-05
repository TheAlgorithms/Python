"""
Rare numbers are special non-palindromic numbers N such that both N + rev(N)
and N - rev(N) are perfect squares, where rev(N) is the reverse of the digits
of N.

This module provides functions to check and generate rare numbers in a given
range. Rare numbers are useful in number theory and pattern-based algorithm
analysis.

For more information about rare numbers, refer to:
[https://www.geeksforgeeks.org/dsa/rare-numbers/](https://www.geeksforgeeks.org/dsa/rare-numbers/)
"""

import math


def rare_numbers(start: int, end: int) -> list[int]:
    """
    Find all rare numbers between the given start and end range (inclusive).

    A rare number N satisfies both:
    1. N + rev(N) is a perfect square.
    2. N - rev(N) is a perfect square.
    where rev(N) is the reverse of the digits of N,
    and N must not be a palindrome.

    Args:
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).

    Returns:
        list[int]: A list of rare numbers within the specified range.

    Raises:
        ValueError: If start or end is negative, or start > end.

    Examples:
    >>> rare_numbers(-1, 100)
    Traceback (most recent call last):
        ...
    ValueError: Range limits must be non-negative and start <= end
    >>> rare_numbers(1, 100)
    []
    >>> rare_numbers(1, 1000)
    [65]
    """
    if start < 0 or end < 0 or start > end:
        raise ValueError("Range limits must be non-negative and start <= end")

    rares = []
    for n in range(start, end + 1):
        rev_n = _reverse_number(n)
        if n == rev_n:
            continue  # skip palindromes
     if n - rev_n > 0 and _is_perfect_square(n + rev_n) and _is_perfect_square(n - rev_n):
            rares.append(n)
    return rares


def _reverse_number(num: int) -> int:
    """
    Reverse the digits of a given integer.

    Args:
        num (int): The integer to reverse.

    Returns:
        int: The reversed integer.

    Examples:
    >>> _reverse_number(123)
    321
    >>> _reverse_number(400)
    4
    """
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev


def _is_perfect_square(n: int) -> bool:
    """
    Check if a number is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.

    Examples:
    >>> _is_perfect_square(16)
    True
    >>> _is_perfect_square(20)
    False
    """
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
