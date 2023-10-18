"""
A triangular number or triangle number counts objects arranged in an
equilateral triangle. This module provides a function to generate
first `n` triangular numbers.

For more information about triangular numbers, refer to:
https://en.wikipedia.org/wiki/Triangular_number
"""


def generate_triangular_numbers(count: int) -> list[int]:
    """
    Generate the first `count` number of triangular numbers starting with 1

    Args:
        count (int): The number of triangular numbers to generate.

    Returns:
        list: A list of the first `count` number of triangular numbers.

    Examples:
    >>> generate_triangular_numbers(3)
    [1, 3, 6]
    >>> generate_triangular_numbers(5)
    [1, 3, 6, 10, 15]
    """
    if count < 0:
        raise ValueError("param `count` must be non-negative")

    triangular_numbers: list[int] = []
    current_sum = 0

    for i in range(1, count + 1):
        current_sum += i
        triangular_numbers.append(current_sum)

    return triangular_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
