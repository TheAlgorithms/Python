"""Next higher integer with the same number of set bits (SNOOB).
author: @0xPrashanthSec

Given a non-negative integer n, return the next higher integer that has the same
number of 1 bits in its binary representation. If no such number exists within
Python's unbounded int range (practically always exists unless n is 0 or all
ones packed at the most significant end for fixed-width), this implementation
returns -1.

This is the classic SNOOB algorithm from "Hacker's Delight".

Reference: https://graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation

>>> next_higher_same_ones(0b0011)
5
>>> bin(next_higher_same_ones(0b0011))
'0b101'
>>> bin(next_higher_same_ones(0b01101))  # 13 -> 14 (0b01110)
'0b1110'
>>> next_higher_same_ones(1)
2
>>> next_higher_same_ones(0)  # no higher with same popcount
-1
>>> next_higher_same_ones(-5)  # negative not allowed
Traceback (most recent call last):
    ...
ValueError: input_value must be a non-negative integer
"""
from __future__ import annotations


def next_higher_same_ones(input_value: int) -> int:
    """Return the next higher integer with the same number of set bits as the input.

    :param input_value: Non-negative integer
    :return: Next higher integer with same popcount or -1 if none
    :raises ValueError: if input_value < 0
    """
    if input_value < 0:
        raise ValueError("input_value must be a non-negative integer")
    if input_value == 0:
        return -1

    # snoob algorithm
    # c = rightmost set bit
    c = input_value & -input_value
    # r = ripple carry: add c to input_value
    r = input_value + c
    if r == 0:
        return -1
    # ones = pattern of ones that moved from lower part
    ones = ((r ^ input_value) >> 2) // c
    return r | ones


if __name__ == "__main__":  # pragma: no cover
    import doctest

    doctest.testmod()
