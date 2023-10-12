"""
Author  : Siddharth Warrier
Date    : October 3, 2023

Task:
Count the no of pairs in a given array with given sum
Problem URL- https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/0

Implementation notes: Using hashing
The idea is that we hash the array in a dictionary
Then go through the elements of the array
We subtract this with the given sum
and check if that is there in the array
We also check the edge cases like if there are multiple same elements
Finally we divide the count by 2
to avoid the same pair getting counted twice
"""

from collections import defaultdict


def pairs_with_sum(arr: list, req_sum: int) -> int:
    """
    Return the no. of pairs with sum "sum"

    >>> pairs_with_sum([1,5,7,1],6)
    2
    >>> pairs_with_sum([1,1,1,1,1,1,1,1],2)
    28
    >>> pairs_with_sum([1,7,6,2,5,4,3,1,9,8],7)
    4
    """
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
    ans = 0
    for i in arr:
        d[i] -= 1
        if req_sum - i in d and d[req_sum - i] != 0:
            ans += d[req_sum - i] - 1
        d[i] += 1
    return ans // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
