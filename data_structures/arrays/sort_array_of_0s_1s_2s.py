"""
Author: Aditya Pathak
Date: 15th Oct 2023
Given an array of integers consisting of 0s, 1s and 2s only, we need to
return the sorted array in O(n) complexity i.e., without actually sorting.

https://practice.geeksforgeeks.org/problems/sort-an-array-o f-0s-1s-and-2s4231/
"""


def sort012(arr: list[int]) -> list[int]:
    """
    args: arr -> An array of integer
    return: list -> an Array of integer

    >>> sort012([1, 2, 0, 0, 2])
    [0, 0, 1, 2, 2]
    >>> sort012([0, 0, 2])
    [0, 0, 2]
    >>> sort012([])
    []
    """
    return arr.count(0) * [0] + arr.count(1) * [1] + arr.count(2) * [2]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
