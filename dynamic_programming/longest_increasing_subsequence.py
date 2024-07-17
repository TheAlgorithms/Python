"""
Author  : Mehdi ALAOUI
Optimized : Arunkumar

This is a pure Python implementation of Dynamic Programming solution to the longest
increasing subsequence of a given sequence.

The problem is  :
Given an array, to find the longest and increasing sub-array in that given array and
return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] as input will return
         [10, 22, 33, 41, 60, 80] as output
"""

from __future__ import annotations


def longest_subsequence(array: list[int]) -> list[int]:
    """
    Find the longest increasing subsequence in the given array
    using dynamic programming.

    Args:
        array (list[int]): The input array.

    Returns:
        list[int]: The longest increasing subsequence.

    Examples:
    >>> longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_subsequence([9, 8, 7, 6, 5, 7])
    [5, 7]
    >>> longest_subsequence([1, 1, 1])
    [1]
    >>> longest_subsequence([])
    []
    """
    if not array:
        return []

    n = len(array)
    # Initialize an array to store the length of the longest
    # increasing subsequence ending at each position.
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)

    # Find the maximum length of the increasing subsequence.
    max_length = max(lis_lengths)

    # Reconstruct the longest subsequence in reverse order.
    subsequence = []
    current_length = max_length
    for i in range(n - 1, -1, -1):
        if lis_lengths[i] == current_length:
            subsequence.append(array[i])
            current_length -= 1

    return subsequence[::-1]  # Reverse the subsequence to get the correct order.


if __name__ == "__main__":
    import doctest

    doctest.testmod()
