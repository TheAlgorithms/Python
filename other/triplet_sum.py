"""
Given an array of integers and another integer X,
we are required to find a triplet from the array such that it's sum is equal to X
"""
from typing import List


def triplet_sum(arr: List[int], X: int) -> tuple:
    """
    Returns a triplet in in array with sum equal to X,
    else (0, 0, 0).
    >>> triplet_sum([13, 29, 7, 23, 5], 35)
    (5, 7, 23)
    >>> triplet_sum([37, 9, 19, 50, 44], 65)
    (9, 19, 37)
    >>> arr = [6, 47, 27, 1, 15]
    >>> summ = 11
    >>> triplet_sum(arr,summ)
    (0, 0, 0)
    """
    arr.sort()
    n = len(arr)
    for i in range(n - 1):
        l, r = i + 1, n - 1
        while l < r:
            if arr[i] + arr[l] + arr[r] == X:
                return (arr[i], arr[l], arr[r])
            elif arr[i] + arr[l] + arr[r] < X:
                l += 1
            elif arr[i] + arr[l] + arr[r] > X:
                r -= 1
    else:
        return (0, 0, 0)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    from random import randint

    arr = [randint(-1000, 1000) for i in range(100)]
    r = randint(-5000, 5000)
    print(f"{triplet_sum(arr,r)}")
