"""
This script demonstrates the implementation of the
sum of squares of the first n natural numbers.

The function takes an integer n as input and returns the sum of squares
from 1 to n using the formula n(n + 1)(2n + 1) / 6.

This formula computes the sum efficiently
without the need for iteration.

https://www.cuemath.com/algebra/sum-of-squares/
"""


def sum_of_squares(num_of_terms: int) -> int:
    """
    Implements the sum of squares formulafor the first n natural numbers.

    Parameters:
        num_of_terms (int): A positive integer representing the limit of the series

    Returns:
        sum_squares (int): The sum of squares of the first n natural numbers.

    Examples:
    >>> sum_of_squares(5)
    55

    >>> sum_of_squares(10)
    385
    """
    return num_of_terms * (num_of_terms + 1) * (2 * num_of_terms + 1) // 6


if __name__ == "__main__":
    import doctest

    doctest.testmod()
