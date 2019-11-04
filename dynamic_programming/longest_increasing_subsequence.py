"""
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solution to the longest increasing subsequence of a given sequence.

The problem is  :
Given an array, to find the longest and increasing sub ARRAY in that given array and return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] as input will return [10, 22, 33, 41, 60, 80] as output
"""
from typing import List


def longest_subsequence(Array: List[int]) -> List[int]:  # This function is recursive
    """
    Some examples
    >>> longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_subsequence([9, 8, 7, 6, 5, 7])
    [8]
    >>> longest_subsequence([1, 1, 1])
    [1, 1, 1]
    """
    ArrayLength = len(Array)
    if (
        ArrayLength <= 1
    ):  # If the array contains only one element, we return it (it's the stop condition of recursion)
        return Array
        # Else
    Pivot = Array[0]
    isFound = False
    i = 1
    LongestSubseq = []
    while not isFound and i < ArrayLength:
        if Array[i] < Pivot:
            isFound = True
            TempArray = [element for element in Array[i:] if element >= Array[i]]
            TempArray = longest_subsequence(TempArray)
            if len(TempArray) > len(LongestSubseq):
                LongestSubseq = TempArray
        else:
            i += 1

    TempArray = [element for element in Array[1:] if element >= Pivot]
    TempArray = [Pivot] + longest_subsequence(TempArray)
    if len(TempArray) > len(LongestSubseq):
        return TempArray
    else:
        return LongestSubseq
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
