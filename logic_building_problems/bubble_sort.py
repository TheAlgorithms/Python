"""Bubble Sort Algorithm.

This module implements the bubble sort algorithm, a simple sorting technique
that repeatedly steps through the list, compares adjacent elements and swaps
them if they are in the wrong order.
"""


def bubble_sort(arr: list[int | float]) -> list[int | float]:
    """
    Sort an array using the bubble sort algorithm.

    Bubble sort works by repeatedly swapping adjacent elements if they are
    in the wrong order. This process continues until no more swaps are needed.

    Args:
        arr: List of numbers to be sorted

    Returns:
        The sorted list in ascending order

    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> bubble_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
        >>> bubble_sort([1])
        [1]
        >>> bubble_sort([])
        []
        >>> bubble_sort([3, 3, 3, 3])
        [3, 3, 3, 3]
        >>> bubble_sort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
        >>> bubble_sort([1.5, 2.3, 0.8, 1.1])
        [0.8, 1.1, 1.5, 2.3]
    """
    # Create a copy to avoid modifying the original list
    arr_copy = arr.copy()
    n = len(arr_copy)

    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize by detecting if array is already sorted
        swapped = False

        # Last i elements are already in place
        for j in range(n - i - 1):
            # Swap if the element found is greater than the next element
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True

        # If no swapping occurred, array is sorted
        if not swapped:
            break

    return arr_copy


if __name__ == "__main__":
    import doctest

    doctest.testmod()
