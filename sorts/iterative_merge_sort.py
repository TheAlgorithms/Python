"""
This is pure implementation of iterative merge sort in python
Author: Aman Gupta

For doctests run following command:
python3 -m doctest -v iterative_merge_sort.py

For manual testing run:
python3 iterative_merge_sort.py
"""

from typing import List


def merge(inputlist: List, low: int, mid: int, high: int) -> List:
    """
    sorting left-half and right-half individually
    then merging them into result
    """
    result = []
    left, right = inputlist[low:mid], inputlist[mid : high + 1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    inputlist[low : high + 1] = result + left + right
    return inputlist


# iteration over the unsorted list
def iter_merge_sort(inputlist: List) -> List:
    """
    Returns sorted list of the input numbers list

    Examples

    >>> iter_merge_sort([5,9,8,1,2,7])
    [1, 2, 5, 7, 8, 9]

    >>> iter_merge_sort([6])
    [6]

    >>> iter_merge_sort([])
    []

    >>> iter_merge_sort([-2,-9,-1,-4])
    [-9, -4, -2, -1]
    
    """

    if len(inputlist) <= 1:
        return inputlist

    # iteration for two-way merging
    p = 2
    while p < len(inputlist):
        # getting low, high and middle value for merge-sort of single list
        for i in range(0, len(inputlist), p):
            low = i
            high = i + p - 1
            mid = (low + high + 1) // 2
            inputlist = merge(inputlist, low, mid, high)
        # final merge of last two parts
        if p * 2 >= len(inputlist):
            mid = i
            inputlist = merge(inputlist, 0, mid, len(inputlist) - 1)

        p *= 2

    return inputlist


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]
    print(*iter_merge_sort(unsorted), sep=",")
