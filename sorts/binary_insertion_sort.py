"""
Python program for Binary Insertion Sort.

"""

from __future__ import annotations


def binary_search(array: list[int], key: int, start: int, end: int):
    """Pure implementation of binary search algorithm in Python

    :param array: some ascending sorted list with comparable items
    :param key: key value to search
    :param start: start index of the array consideration
    :param end: end index of the array consideration

    """

    if start == end:
        if array[start] > key:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if array[mid] < key:
        return binary_search(array, key, mid + 1, end)
    elif array[mid] > key:
        return binary_search(array, key, start, mid - 1)
    else:
        return mid


def binary_insertion_sort(array: list[int]):
    """Implementation of insertion sort with binary search to find position.

    :param array: list of elements to be sorted.

    Examples:

    >>> res = binary_insertion_sort([29, 10, 14, 37, 14])
    >>> print(res)
    [10, 14, 14, 29, 37]

    """
    total_num = len(array)
    for itr in range(1, total_num):
        key = array[itr]
        index_position = binary_search(array, key, 0, itr - 1)
        array = (
            array[:index_position]
            + [key]
            + array[index_position:itr]
            + array[itr + 1 :]
        )
    return array


if __name__ == "__main__":
    res = binary_insertion_sort([29, 10, 14, 37, 14])
    print(res)
