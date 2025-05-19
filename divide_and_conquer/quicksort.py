from __future__ import annotations


def partition(array: list, start: int, end: int) -> int:
    """Helper function for Quick Sort.

    >>> array = [5, 8, 3, 2, 9, 6]
    >>> start = 0
    >>> end = 5
    >>> index = partition(array, start, end)
    >>> index  # The pivot index
    3
    >>> sorted(array[:index])  # Elements less than pivot
    [2, 3, 5]
    >>> sorted(array[index+1:])  # Elements greater than pivot
    [8, 9]

    >>> array = []
    >>> start = 0
    >>> end = 0
    >>> partition(array, start, end)
    0
    >>> array
    []
    """
    if not array:
        return 0
    pivot = array[end]
    index = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            index += 1
            array[index], array[j] = array[j], array[index]
    array[index + 1], array[end] = array[end], array[index + 1]
    return index + 1


def quicksort(array, start, end):
    """Returns a list of sorted array elements using Quick Sort.

    >>> from random import shuffle
    >>> array = [5, 8, 3, 2, 9, 6]
    >>> start = 0
    >>> end = 5
    >>> quicksort(array, start, end)
    >>> array
    [2, 3, 5, 6, 8, 9]

    >>> shuffle(array)
    >>> quicksort(array, start, end)
    >>> array
    [2, 3, 5, 6, 8, 9]

    >>> array = [-100]
    >>> quicksort(array, 0, len(array) - 1)
    >>> array
    [-100]

    >>> array = []
    >>> quicksort(array, 0, 0)
    >>> array
    []
    """
    if start < end:
        partition_index = partition(array, start, end)
        quicksort(array, start, partition_index - 1)
        quicksort(array, partition_index + 1, end)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
