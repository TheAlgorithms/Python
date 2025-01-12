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

    # Either the subsequence contains the pivot or it does not,
    # The longest subsequence is calculated in both cases and
    # The longer subsequence is returned
    without_pivot = longest_subsequence(array[1:])
    with_pivot = [element for element in array[1:] if element >= pivot]
    with_pivot = [pivot, *longest_subsequence(with_pivot)]
    if len(with_pivot) > len(without_pivot):
        return with_pivot
    else:
        return without_pivot


if __name__ == "__main__":
    import doctest

    doctest.testmod()
