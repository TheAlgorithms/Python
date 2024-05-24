#!/usr/bin/env python3

"""
Given an array of integers and an integer req_sum, find the number of pairs of array
elements whose sum is equal to req_sum.

https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/0
"""

from itertools import combinations


def pairs_with_sum(arr: list, req_sum: int) -> int:
    """
    Return the no. of pairs with sum "sum"
    >>> pairs_with_sum([1, 5, 7, 1], 6)
    2
    >>> pairs_with_sum([1, 1, 1, 1, 1, 1, 1, 1], 2)
    28
    >>> pairs_with_sum([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    4
    """
    return len([1 for a, b in combinations(arr, 2) if a + b == req_sum])


# Without using the  itertools Package we can do it too
def no_of_pairs(arr: list, req_sum: int) -> int:
    # this is a non optimised code and easy to understand as i am a beginner in coding
    # the code above is the best one to use as this function uses nested loops which is
    # very much slower in execution
    count_total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) == req_sum:
                count_total += 1
    return count_total


if __name__ == "__main__":
    from doctest import testmod

    testmod()
