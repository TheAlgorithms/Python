from __future__ import annotations

def partition(array: list, low: int, high: int) -> int:
    """
    Helper function for quicksort to partition the array.

    >>> array = [3, 2, 1]
    >>> idx = partition(array, 0, len(array) - 1)
    >>> idx
    0
    >>> array
    [1, 2, 3]

    >>> array = [12, 4, 5, 2, 3]
    >>> idx = partition(array, 0, len(array) - 1)
    >>> array[:idx], array[idx], array[idx+1:]
    ([2, 3, 4], 5, [12])

    >>> array = [2, 1]
    >>> idx = partition(array, 0, len(array) - 1)
    >>> array
    [1, 2]
    """
    pivot = array[high]
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array: list, low: int = 0, high: int | None = None) -> list:
    """
    Returns a sorted list using the quicksort algorithm.

    >>> quicksort([-2, 3, -10, 11, 99, 100000, 100, -200])
    [-200, -10, -2, 3, 11, 99, 100, 100000]

    >>> quicksort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> quicksort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> quicksort([-200])
    [-200]

    >>> quicksort([])
    []

    >>> quicksort([10000000, 1, -1111111111, 101111111112, 9000002])
    [-1111111111, 1, 9000002, 10000000, 101111111112]
    """
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

    return array

if __name__ == "__main__":
    import doctest
    doctest.testmod()
