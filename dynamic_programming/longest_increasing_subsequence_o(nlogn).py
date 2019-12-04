#############################
# Author: Aravind Kashyap
# File: lis.py
# comments: This programme outputs the Longest Strictly Increasing Subsequence in O(NLogN)
#           Where N is the Number of elements in the list
#############################
from typing import List
from bisect import bisect_left


def LongestIncreasingSubsequenceLength(v: List[int]) -> int:
    """
    >>> LongestIncreasingSubsequenceLength([2, 5, 3, 7, 11, 8, 10, 13, 6])
    6
    >>> LongestIncreasingSubsequenceLength([])
    0
    >>> LongestIncreasingSubsequenceLength([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    6
    >>> LongestIncreasingSubsequenceLength([5, 4, 3, 2, 1])
    1
    """
    if not v:
        return 0

    tail = [v[0]]

    for n in v:
        if n < tail[0]:
            tail[0] = n
        elif n > tail[-1]:
            tail.append(n)
        else:
            tail[bisect_left(tail, n)] = n

    return len(tail)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
