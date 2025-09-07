"""
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solution to the longest
increasing subsequence of a given sequence.

The problem is:
    Given an array, to find the longest and increasing sub-array in that given array and
    return it.

Example:
    ``[10, 22, 9, 33, 21, 50, 41, 60, 80]`` as input will return
    ``[10, 22, 33, 41, 60, 80]`` as output
"""

from __future__ import annotations


def longest_subsequence(array: list[int]) -> list[int]:  # This function is recursive
    """
    Some examples

    >>> longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_subsequence([28, 26, 12, 23, 35, 39])
    [12, 23, 35, 39]
    >>> longest_subsequence([9, 8, 7, 6, 5, 7])
    [5, 7]
    >>> longest_subsequence([1, 1, 1])
    [1, 1, 1]
    >>> longest_subsequence([])
    []
    """
    array_length = len(array)
    # If the array contains only one element, we return it (it's the stop condition of
    # recursion)
    if array_length <= 1:
        return array
        # Else
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq: list[int] = []
    while not is_found and i < array_length:
        if array[i] < pivot:
            is_found = True
            temp_array = array[i:]
            temp_array = longest_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq


if __name__ == "__main__":
    import doctest

    doctest.testmod()
