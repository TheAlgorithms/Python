"""
This is a pure Python implementation of the heap sort algorithm.

For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py

For manual testing run:
python heap_sort.py
"""
from typing import List


def heapify(unsorted_list: List[int], index: int, heap_size: int) -> None:
    """

    :param unsorted_list: unsorted list containing integers numbers
    :param index: index
    :param heap_size: size of the heap
    :return: None
    """
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted_list[left_index] > unsorted_list[largest]:
        largest = left_index

    if right_index < heap_size and unsorted_list[right_index] > unsorted_list[largest]:
        largest = right_index

    if largest != index:
        unsorted_list[largest], unsorted_list[index] = unsorted_list[index], unsorted_list[largest]
        heapify(unsorted_list, largest, heap_size)


def heap_sort(unsorted_list: List[int]) -> List[int]:
    """
    Pure implementation of the heap sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> heap_sort([])
    []

    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]

    >>> heap_sort([3, 7, 9, 28, 123, -5, 8, -30, -200, 0, 4])
    [-200, -30, -5, 0, 3, 4, 7, 8, 9, 28, 123]
    """
    n = len(unsorted_list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted_list, i, n)
    for i in range(n - 1, 0, -1):
        unsorted_list[0], unsorted_list[i] = unsorted_list[i], unsorted_list[0]
        heapify(unsorted_list, 0, i)
    return unsorted_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
