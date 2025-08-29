#############################
# Author: Aravind Kashyap
# File: lis.py
# comments: This programme outputs the Longest Strictly Increasing Subsequence in
#           O(NLogN) Where N is the Number of elements in the list
#############################
from __future__ import annotations


def ceil_index(v, left, right, key):
    while right - left > 1:
        middle = (left + right) // 2
        if v[middle] >= key:
            right = middle
        else:
            left = middle
    return right


def longest_increasing_subsequence_length(v: list[int]) -> int:
    """
    >>> longest_increasing_subsequence_length([2, 5, 3, 7, 11, 8, 10, 13, 6])
    6
    >>> longest_increasing_subsequence_length([])
    0
    >>> longest_increasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
    ...                                     3, 11, 7, 15])
    6
    >>> longest_increasing_subsequence_length([5, 4, 3, 2, 1])
    1
    """
    if len(v) == 0:
        return 0

    tail = [0] * len(v)
    length = 1

    tail[0] = v[0]

    for i in range(1, len(v)):
        if v[i] < tail[0]:
            tail[0] = v[i]
        elif v[i] > tail[length - 1]:
            tail[length] = v[i]
            length += 1
        else:
            tail[ceil_index(tail, -1, length - 1, v[i])] = v[i]

    return length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
