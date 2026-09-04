"""
Author  : Alexander Pantyukhin
Date    : November 30, 2022

Task:
Given two int numbers. Return True these numbers have opposite signs
or False otherwise.

Implementation notes: Use bit manipulation.
Use XOR for two numbers.
"""


def different_signs(num1: int, num2: int) -> bool:
    """
    Return True if numbers have opposite signs False otherwise.
    Uses XOR and the sign bit to detect opposite signs. In two's complement
    representation (used for integers), the most significant bit is the sign bit:
    - Positive numbers have MSB = 0
    - Negative numbers have MSB = 1
    When two numbers have opposite signs, their sign bits differ, so XOR will
    produce a negative result (MSB = 1).
    Algorithm:
    1. XOR the two numbers: num1 ^ num2
    2. If the result is negative, the sign bits were different (opposite signs)
    3. Return True if result < 0, False otherwise
    Why it works:
    - num1 = 1 (positive, MSB=0): ...0001
    - num2 = -1 (negative, MSB=1): ...1111 (in two's complement)
    - num1 ^ num2 = 1 ^ (-1) = ...1110 (negative, because MSB=1)
    - Result < 0, so they have opposite signs ✓
    Example:
    - different_signs(1, -1): 1 ^ -1 < 0 → True ✓
    - different_signs(1, 1): 1 ^ 1 = 0, not < 0 → False ✓
    >>> different_signs(1, -1)
    True
    >>> different_signs(1, 1)
    False
    >>> different_signs(1000000000000000000000000000, -1000000000000000000000000000)
    True
    >>> different_signs(-1000000000000000000000000000, 1000000000000000000000000000)
    True
    >>> different_signs(50, 278)
    False
    >>> different_signs(0, 2)
    False
    >>> different_signs(2, 0)
    False
    """
    return num1 ^ num2 < 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
