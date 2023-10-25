"""
Integer Square Root Algorithm

This module provides an efficient method to calculate the square root of a
non-negative integer 'num' rounded down to the nearest integer. It uses
a binary search approach to find the integer square root without using any
built-in exponent functions or operators.

Note:
    - This algorithm is designed for non-negative integers only.
    - The result is rounded down to the nearest integer.
    - The algorithm has a time complexity of O(log(x)).
    - Original algorithm idea based on binary search.
"""


def integer_square_root(num: int) -> int:
    """
    Returns the integer square root of a non-negative integer num.

    Args:
        num: A non-negative integer.

    Returns:
        The integer square root of num.

    Raises:
        ValueError: If num is negative.

    >>> integer_square_root(0)
    0
    >>> integer_square_root(1)
    1
    >>> integer_square_root(4)
    2
    >>> integer_square_root(625)
    25
    >>> integer_square_root(9)
    3
    >>> integer_square_root(10)
    3
    """
    if num < 0:
        raise ValueError("num must be non-negative")

    if num < 2:
        return num

    left_bound, right_bound = 0, num // 2

    while left_bound <= right_bound:
        mid = left_bound + (right_bound - left_bound) // 2
        mid_squared = mid * mid

        if mid_squared == num:
            return mid
        elif mid_squared < num:
            left_bound = mid + 1
        else:
            right_bound = mid - 1

    return right_bound


if __name__ == "__main__":
    import doctest

    doctest.testmod()
