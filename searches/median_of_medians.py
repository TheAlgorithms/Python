"""
A Python implementation of the Median of Medians algorithm
to select pivots for quick_select, which is efficient for
calculating the value that would appear in the index of a
list if it would be sorted, even if it is not already
sorted. Search in time complexity O(n) at any rank
deterministically
https://en.wikipedia.org/wiki/Median_of_medians
"""


def median_of_five(arr: list) -> int:
    """
    Return the median of the input list
    :param arr: Array to find median of
    :return: median of arr

    >>> median_of_five([2, 4, 5, 7, 899])
    5
    >>> median_of_five([5, 7, 899, 54, 32])
    32
    >>> median_of_five([5, 4, 3, 2])
    4
    >>> median_of_five([3, 5, 7, 10, 2])
    5
    """
    arr = sorted(arr)
    return arr[len(arr) // 2]


def median_of_medians(arr: list) -> int:
    """
    Return a pivot to partition data on by calculating
    Median of medians of input data
    :param arr: The data to be checked (a list)
    :return: median of medians of input array

    >>> median_of_medians([2, 4, 5, 7, 899, 54, 32])
    54
    >>> median_of_medians([5, 7, 899, 54, 32])
    32
    >>> median_of_medians([5, 4, 3, 2])
    4
    >>> median_of_medians([3, 5, 7, 10, 2, 12])
    12
    """

    if len(arr) <= 5:
        return median_of_five(arr)
    medians = []
    i = 0
    while i < len(arr):
        if (i + 4) <= len(arr):
            medians.append(median_of_five(arr[i:].copy()))
        else:
            medians.append(median_of_five(arr[i : i + 5].copy()))
        i += 5
    return median_of_medians(medians)


def quick_select(arr: list, target: int) -> int:
    """
    Two way partition the data into smaller and greater lists,
    in relationship to the pivot
    :param arr: The data to be searched (a list)
    :param target: The rank to be searched
    :return: element at rank target

    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    32
    >>> quick_select([2, 4, 5, 7, 899, 54, 32], 1)
    2
    >>> quick_select([5, 4, 3, 2], 2)
    3
    >>> quick_select([3, 5, 7, 10, 2, 12], 3)
    5
    """

    # Invalid Input
    if target > len(arr):
        return -1

    # x is the estimated pivot by median of medians algorithm
    x = median_of_medians(arr)
    left = []
    right = []
    check = False
    for i in range(len(arr)):
        if arr[i] < x:
            left.append(arr[i])
        elif arr[i] > x:
            right.append(arr[i])
        elif arr[i] == x and not check:
            check = True
        else:
            right.append(arr[i])
    rank_x = len(left) + 1
    if rank_x == target:
        answer = x
    elif rank_x > target:
        answer = quick_select(left, target)
    elif rank_x < target:
        answer = quick_select(right, target - rank_x)
    return answer


print(median_of_five([5, 4, 3, 2]))
