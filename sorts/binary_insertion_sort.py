"""
Illustrate how to implement binary insertion sort algorithm.

Author: REHAN SHAIKH

Binary Insertion Sort: Binary insertion sort is a sorting algorithm which uses insertion sort with binary search rather than linear search to find the position where the element should be inserted . The advantage is that we reduce the number of comparisons for inserting one element from O(N) to O(log N).

Time Complexity: O(n2) is the worst case running time because of the series of swaps required for each insertion

Auxiliary Space: O(logn)

For doctests run following command:
python -m doctest -v binary_insertion_sort.py
or
python3 -m doctest -v binary_insertion_sort.py
For manual testing run:
python binary_insertion_sort.py

"""


def binary_search(arr: list, length: int, key: int) -> int:
    """
    Pure implementation of binary search algorithm in Python

    :param arr: list
    :param length: int
    :param key: int
    :return: int

    Examples:
    >>> binary_search([7, 3, 9, 5, 2], 4, 5)
    2
    >>> binary_search([7, 3, 9, 5, 2], 4, 9)
    4

    """
    low = 0
    high = length
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid
    return low


def insertion_sort(arr: list) -> list:
    """Pure implementation of binary insertion sort algorithm in Python

    :param arr: list
    :return: list

    Examples:
    >>> insertion_sort([7, 3, 9, 5, 2])
    [2, 3, 5, 7, 9]

    """
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, i, key)
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[pos] = key
    return arr


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    assert binary_search([7, 3, 9, 5, 2], 4, 5) == 2
    assert binary_search([7, 3, 9, 5, 2], 4, 9) == 4

    assert insertion_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
