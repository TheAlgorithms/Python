"""
author : Mayank Kumar Jha (mk9440)
"""
from __future__ import annotations


def find_max_sub_array(a, low, high):
    if low == high:
        return low, high, a[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_sub_array(a, low, mid)
        right_low, right_high, right_sum = find_max_sub_array(a, mid + 1, high)
        cross_left, cross_right, cross_sum = find_max_cross_sum(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_left, cross_right, cross_sum


def find_max_cross_sum(a, low, mid, high):
    left_sum, max_left = -999999999, -1
    right_sum, max_right = -999999999, -1
    summ = 0
    for i in range(mid, low - 1, -1):
        summ += a[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    summ = 0
    for i in range(mid + 1, high + 1):
        summ += a[i]
        if summ > right_sum:
            right_sum = summ
            max_right = i
    return max_left, max_right, (left_sum + right_sum)


def max_sub_array(nums: list[int]) -> int:
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
    """
    best = 0
    current = 0
    for i in nums:
        current += i
        if current < 0:
            current = 0
        best = max(best, current)
    return best


if __name__ == "__main__":
    """
    A random simulation of this algorithm.
    """
    import time
    from random import randint

    from matplotlib import pyplot as plt

    inputs = [10, 100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]
    tim = []
    for i in inputs:
        li = [randint(1, i) for j in range(i)]
        strt = time.time()
        (find_max_sub_array(li, 0, len(li) - 1))
        end = time.time()
        tim.append(end - strt)
    print("No of Inputs       Time Taken")
    for i in range(len(inputs)):
        print(inputs[i], "\t\t", tim[i])
    plt.plot(inputs, tim)
    plt.xlabel("Number of Inputs")
    plt.ylabel("Time taken in seconds ")
    plt.show()
