"""Bubble Sort with early termination optimization."""


def bubble_sort_optimized(arr: list[float]) -> list[float]:
    """
    Sort a list using bubble sort with early termination.

    Stops early if no swaps occur in a pass (already sorted).

    >>> bubble_sort_optimized([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> bubble_sort_optimized([1, 2, 3])
    [1, 2, 3]
    >>> bubble_sort_optimized([])
    []
    >>> bubble_sort_optimized([5])
    [5]
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
