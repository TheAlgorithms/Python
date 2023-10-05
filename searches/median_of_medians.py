"""
A Python implementation of the Median of Medians algorithm to select pivots for QuickSelect,
which is efficient for calculating the value that would appear in the index of a list if it
would be sorted, even if it is not already sorted. Search in time complexity O(n) at any rank
deterministically
https://en.wikipedia.org/wiki/Median_of_medians
"""

def MedianofFive(arr:list) -> int:
    """
    Return the median of the input list
    :param arr: Array to find median of
    :return: median of arr
    """
    arr=sorted(arr)
    return arr[len(arr)//2]

def MedianofMedians(arr:list) -> int:
    """
    Return a pivot to partition data on by calculating
    Median of medians of input data
    :param arr: The data to be sorted (a list)
    :param k: The rank to be searched
    :return: element at rank k
    """
    if len(arr) <= 5:        return MedianofFive(arr)
    medians = []
    i=0
    while i<len(arr):
        if (i + 4) <= len(arr):            medians.append(MedianofFive(arr[i:].copy()))
        else:                              medians.append(MedianofFive(arr[i:i+5].copy()))
        i+=5
    return MedianofMedians(medians)

def QuickSelect(arr:list, k:int) -> int:
    """
    >>> QuickSelect([2, 4, 5, 7, 899, 54, 32], 5)
    32
    >>> QuickSelect([2, 4, 5, 7, 899, 54, 32], 1)
    2
    >>> QuickSelect([5, 4, 3, 2], 2)
    3
    >>> QuickSelect([3, 5, 7, 10, 2, 12], 3)
    5
    """

    """
    Two way partition the data into smaller and greater lists,
    in relationship to the pivot
    :param arr: The data to be sorted (a list)
    :param k: The rank to be searched
    :return: element at rank k
    """

    # Invalid Input
    if k>len(arr):
        return None

    # x is the estimated pivot by median of medians algorithm
    x = MedianofMedians(arr)
    left = []
    right = []
    check = False
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < x:
            left.append(arr[i])
        elif arr[i] > x:
            right.append(arr[i])
        elif arr[i] == x and not check:
            check = True
        else:
            right.append(arr[i])
    rankX = len(left) + 1
    if(rankX==k):        answer = x
    elif rankX>k:        answer = QuickSelect(left,k)
    elif rankX<k:        answer = QuickSelect(right,k-rankX)
    return answer;
