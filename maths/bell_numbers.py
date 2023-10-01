"""
Bell numbers represent the number of ways to partition a set into non-empty subsets. This module provides functions to calculate Bell numbers for sets of integers. In other words, the first (n + 1) Bell numbers.

For more information about Bell numbers, refer to:
https://en.wikipedia.org/wiki/Bell_number

Example:
To calculate the Bell numbers for sets of lengths from 0 to 5:

>>> import bell_numbers
>>> bell_numbers.bell_numbers(5)
[1, 1, 2, 5, 15, 52]
"""


def bell_numbers(n: int) -> list[int]:
    """
    Calculate Bell numbers for the sets of lengths from 0 to n. In other words, calculate first (n + 1) Bell numbers.

    Args:
        n (int): The maximum length of the sets for which Bell numbers are calculated.

    Returns:
        list: A list of Bell numbers for sets of lengths from 0 to n.

    Examples:
    >>> bell_numbers(0)
    [1]
    >>> bell_numbers(1)
    [1, 1]
    >>> bell_numbers(5)
    [1, 1, 2, 5, 15, 52]
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    bell = [0] * (n + 1)
    bell[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            bell[i] += _binomial_coefficient(i - 1, j) * bell[j]

    return bell


def _binomial_coefficient(n: int, k: int) -> int:
    """
    Calculate the binomial coefficient C(n, k) using dynamic programming.

    Args:
        n (int): Total number of elements.
        k (int): Number of elements to choose.

    Returns:
        int: The binomial coefficient C(n, k).

    Examples:
    >>> _binomial_coefficient(5, 2)
    10
    >>> _binomial_coefficient(6, 3)
    20
    """
    if k == 0 or k == n:
        return 1

    if k > n - k:
        k = n - k

    coefficient = 1
    for i in range(k):
        coefficient *= n - i
        coefficient //= i + 1

    return coefficient


if __name__ == "__main__":
    import doctest

    doctest.testmod()
