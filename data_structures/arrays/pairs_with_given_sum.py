#!/usr/bin/env python3

"""
Given an array of integers and an integer req_sum, find the number of pairs of array
elements whose sum is equal to req_sum.

https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/0
"""


def pairs_with_sum(arr: list[int], req_sum: int) -> int:
    """
    Return the number of pairs with sum equal to req_sum.

    >>> pairs_with_sum([1, 5, 7, 1], 6)
    2
    >>> pairs_with_sum([1, 1, 1, 1, 1, 1, 1, 1], 2)
    28
    >>> pairs_with_sum([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    4
    """
    count = 0
    seen = {}

    for num in arr:
        complement = req_sum - num
        if complement in seen:
            count += seen[complement]

        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return count


if __name__ == "__main__":
    from doctest import testmod

    testmod()
