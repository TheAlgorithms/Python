"""
Integer Square Root Algorithm -- An efficient method to calculate the square root of a
non-negative integer 'num' rounded down to the nearest integer. It uses a binary search
approach to find the integer square root without using any built-in exponent functions
or operators.
* https://en.wikipedia.org/wiki/Integer_square_root
* https://docs.python.org/3/library/math.html#math.isqrt
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
        ValueError: If num is not an integer or is negative.
    >>> [integer_square_root(i) for i in range(18)]
    [0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4]
    >>> integer_square_root(625)
    25
    >>> integer_square_root(2_147_483_647)
    46340
    >>> from math import isqrt
    >>> all(integer_square_root(i) == isqrt(i) for i in range(20))
    True
    >>> integer_square_root(-1)
    Traceback (most recent call last):
        ...
    ValueError: num must be non-negative integer
    >>> integer_square_root(1.5)
    Traceback (most recent call last):
        ...
    ValueError: num must be non-negative integer
    >>> integer_square_root("0")
    Traceback (most recent call last):
        ...
    ValueError: num must be non-negative integer
    """
    if not isinstance(num, int) or num < 0:
        raise ValueError("num must be non-negative integer")

    if num < 2:
        return num

    left_bound = 0
    right_bound = num // 2

    while left_bound <= right_bound:
        mid = left_bound + (right_bound - left_bound) // 2
        mid_squared = mid * mid
        if mid_squared == num:
            return mid

        if mid_squared < num:
            left_bound = mid + 1
        else:
            right_bound = mid - 1

    return right_bound


if __name__ == "__main__":
    import doctest

    doctest.testmod()
