"""
The maximum subarray problem is the task of finding the continuous subarray that has the
maximum sum within a given array of numbers. For example, given the array
[-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray with the maximum sum is
[4, -1, 2, 1], which has a sum of 6.

This divide-and-conquer algorithm finds the maximum subarray in O(n log n) time.
"""

from __future__ import annotations

import time
from collections.abc import Sequence
from random import randint

from matplotlib import pyplot as plt


def max_subarray(
    arr: Sequence[float], low: int, high: int
) -> tuple[int | None, int | None, float]:
    """
    Solves the maximum subarray problem using divide and conquer.
    :param arr:     the given array of numbers
    :param low:     the start index
    :param high:    the end index
    :return:        the start index of the maximum subarray, the end index of the
                    maximum subarray, and the maximum subarray sum

    >>> nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    >>> max_subarray(nums, 0, len(nums) - 1)
    (3, 6, 6)
    >>> nums = [2, 8, 9]
    >>> max_subarray(nums, 0, len(nums) - 1)
    (0, 2, 19)
    >>> nums = [0, 0]
    >>> max_subarray(nums, 0, len(nums) - 1)
    (0, 0, 0)
    >>> nums = [-1.0, 0.0, 1.0]
    >>> max_subarray(nums, 0, len(nums) - 1)
    (2, 2, 1.0)
    >>> nums = [-2, -3, -1, -4, -6]
    >>> max_subarray(nums, 0, len(nums) - 1)
    (2, 2, -1)
    >>> max_subarray([], 0, 0)
    (None, None, 0)
    """
    if not arr:
        return None, None, 0
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray(arr, low, mid)
    right_low, right_high, right_sum = max_subarray(arr, mid + 1, high)
    cross_left, cross_right, cross_sum = max_cross_sum(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_left, cross_right, cross_sum


def max_cross_sum(
    arr: Sequence[float], low: int, mid: int, high: int
) -> tuple[int, int, float]:
    left_sum, max_left = float("-inf"), -1
    right_sum, max_right = float("-inf"), -1

    summ: int | float = 0
    for i in range(mid, low - 1, -1):
        summ += arr[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i

    summ = 0
    for i in range(mid + 1, high + 1):
        summ += arr[i]
        if summ > right_sum:
            right_sum = summ
            max_right = i

    return max_left, max_right, (left_sum + right_sum)


def time_max_subarray(input_size: int) -> float:
    arr = [randint(1, input_size) for _ in range(input_size)]
    start = time.time()
    max_subarray(arr, 0, input_size - 1)
    end = time.time()
    return end - start


def plot_runtimes() -> None:
    input_sizes = [10, 100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]
    runtimes = [time_max_subarray(input_size) for input_size in input_sizes]
    print("No of Inputs\t\tTime Taken")
    for input_size, runtime in zip(input_sizes, runtimes):
        print(input_size, "\t\t", runtime)
    plt.plot(input_sizes, runtimes)
    plt.xlabel("Number of Inputs")
    plt.ylabel("Time taken in seconds")
    plt.show()


if __name__ == "__main__":
    """
    A random simulation of this algorithm.
    """
    from doctest import testmod

    testmod()
