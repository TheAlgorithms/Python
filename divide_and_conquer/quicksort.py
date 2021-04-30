import sys
from typing import List

sys.setrecursionlimit(10 ** 5)


def partition(array: List, start: int, end: int) -> int:
    """
     Helper function for quick_sort
    Partitions array around a pivot
    such that elements to the right of pivot are > pivot
    elements to the left of pivot < pivot
    and pivot is in the correct position
    and returns index of pivot in sorted array

    >>> array = [4,1,5,6,3,5,2]
    >>> p = partition(array,0,6)
    >>> p
    3
    """
    pivot = array[start]  # pivot element to partition the array around
    i = start + 1  # pointer to keep track of partition elements
    for j in range(i, end + 1):
        """
        loop that runs through all elements in the sub array
        and partitions around the pivot
        """
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        """
        Swapping pivot so that it ends up in it's right place
        """
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quick_sort(array: List, start: int = 0, end: int = None) -> List:
    """
    function that takes in a list as input
    and return sorted list
    >>> array = [4 , 1, 6, 5, 3, 2, 5]
    >>> sorted_array = quick_sort(array)
    >>> sorted_array
    [1, 2, 3, 4, 5, 5, 6]
    """
    if end is None:
        """
        Overriding default pointer to end of original array
        """
        end = len(array) - 1

    if len(array) <= 1:
        return array
    elif start >= end:
        return array
    else:
        pivot_index = partition(array, start, end)  # partition array around a pivot
        array = quick_sort(
            array, start, pivot_index - 1
        )  # run quicksort on left subarray on elements < pivot
        array = quick_sort(
            array, pivot_index + 1, end
        )  # run quicksort on right subarray on elements >= pivot

    return array


if __name__ == "__main__":
    import doctest

    doctest.testmod()
