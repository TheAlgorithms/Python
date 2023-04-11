"""
author : Snehanjali G  V S
"""
from __future__ import annotations


def max_sub_array(a: list[int]) -> int:
    """
    Finds the contiguous subarray which has the largest sum and return its sum.

    >>> max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    An empty (sub)array has sum 0.
    >>> max_sub_array([])
    0

    If all elements are negative, the largest subarray would be the empty array,
    having the sum 0.
    >>> max_sub_array([-1, -2, -3])
    0
    >>> max_sub_array([5, -2, -3])
    5
    >>> max_sub_array([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    >>> max_sub_array([10, 100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000])
    1561110
    """
    sol = [0] * (len(a) + 1)
    for i in range(1, len(sol)):
        sol[i] = max(sol[i - 1] + a[i - 1], a[i - 1])

    answer = sol[0]
    for i in range(1, len(sol)):
        if answer < sol[i]:
            answer = sol[i]
    return answer


if __name__ == "__main__":
    """
    A random simulation of this algorithm.
    """

    inputs = [10, 100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]
    print(max_sub_array(inputs))
