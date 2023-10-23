"""
A triangular number or triangle number counts objects arranged in an
equilateral triangle. This module provides a function to generate n'th
triangular number.

For more information about triangular numbers, refer to:
https://en.wikipedia.org/wiki/Triangular_number
"""


def nth_triangular_number(position: int) -> int:
    """
    Generate the triangular number at the specified position.

    Args:
        position (int): The position of the triangular number to generate.

    Returns:
        int: The triangular number at the specified position.

    Examples:
    >>> nth_triangular_number(1)
    1
    >>> nth_triangular_number(3)
    6
    >>> nth_triangular_number(5)
    15
    """
    if position < 1:
        raise ValueError("param `position` must be greater than 0")

    return position * (position + 1) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
