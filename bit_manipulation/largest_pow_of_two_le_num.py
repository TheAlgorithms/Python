"""
Author  : Naman Sharma
Date    : October 2, 2023

Task:
To Find the largest power of 2 less than or equal to a given number
Implementation notes: Use bit manipulation.
We start from 1 & left shift the set bit to check if (res<<1)<=number.
Each left bit shift represents a pow of 2.
For example:
number: 15
res:    1   0b1
        2   0b10
        4   0b100
        8   0b1000
        16  0b10000 (Exit)
"""


def largest_pow_of_two_le_num(number: int) -> int:
    """
    Return the largest power of two less than or equal to a number.

    Finds the largest power of 2 that is ≤ the given number using bit shifting.
    Each left shift by 1 (res <<= 1) multiplies by 2, so it generates successive
    powers of 2: 1, 2, 4, 8, 16, ...
    Algorithm:
    1. Handle edge cases: if number <= 0, return 0
    2. Initialize result to 1 (the smallest power of 2)
    3. While (result << 1) <= number:
       a. Left-shift result by 1, effectively multiplying by 2
       b. This generates the next power of 2
    4. Return the result (the largest power of 2 that didn't exceed number)
    Example: number = 15
    - Start: res = 1 (0b1)
    - Iteration 1: res = 2 (0b10), check 4 <= 15 ✓
    - Iteration 2: res = 4 (0b100), check 8 <= 15 ✓
    - Iteration 3: res = 8 (0b1000), check 16 <= 15 ✗
    - Return 8 (the largest power of 2 ≤ 15)
    >>> largest_pow_of_two_le_num(0)
    0
    >>> largest_pow_of_two_le_num(1)
    1
    >>> largest_pow_of_two_le_num(-1)
    0
    >>> largest_pow_of_two_le_num(3)
    2
    >>> largest_pow_of_two_le_num(15)
    8
    >>> largest_pow_of_two_le_num(99)
    64
    >>> largest_pow_of_two_le_num(178)
    128
    >>> largest_pow_of_two_le_num(999999)
    524288
    >>> largest_pow_of_two_le_num(99.9)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    """
    if isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    if number <= 0:
        return 0
    res = 1
    while (res << 1) <= number:
        res <<= 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
