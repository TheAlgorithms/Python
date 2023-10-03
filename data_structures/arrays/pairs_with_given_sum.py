"""
Author  : Siddharth Warrier
Date    : October 3, 2023

Task:
Count the no of pairs in a given array with given sum

Implementation notes: Using hashing
The idea is that we hash the array in a dictionary
Then go through the elements of the array
We subtract this with the given sum
and check if that is there in the array
We also check the edge cases like if there are multiple same elements
Finally we divide the count by 2
to avoid the same pair getting counted twice
"""


def pairs_with_sum(arr: list, sum: int) -> int:
    """
    Return the no. of pairs with sum "sum"

    >>> pairs_with_sum([1,5,7,1],6)
    2
    >>> pairs_with_sum([1,1,1,1,1,1,1,1],2)
    28
    >>> pairs_with_sum([1,7,6,2,5,4,3,1,9,8],7)
    4
    """
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in arr:
        d[i] -= 1
        if sum - i in d and d[sum - i] != 0:
            ans += d[sum - i]
        d[i] += 1
    return ans // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
