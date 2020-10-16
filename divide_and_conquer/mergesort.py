from typing import List


def merge(left_half: List, right_half: List) -> List:
    """Helper function for mergesort.

    >>> left_half = [-2]
    >>> right_half = [-1]
    >>> merge(left_half, right_half)
    [-2, -1]

    >>> left_half = [1,2,3]
    >>> right_half = [4,5,6]
    >>> merge(left_half, right_half)
    [1, 2, 3, 4, 5, 6]

    >>> left_half = [-2]
    >>> right_half = [-1]
    >>> merge(left_half, right_half)
    [-2, -1]

    >>> left_half = [12, 15]
    >>> right_half = [13, 14]
    >>> merge(left_half, right_half)
    [12, 13, 14, 15]

    >>> left_half = []
    >>> right_half = []
    >>> merge(left_half, right_half)
    []
    """
    sorted_array = [None] * (len(right_half) + len(left_half))

    pointer1 = 0  # pointer to current index for left Half
    pointer2 = 0  # pointer to current index for the right Half
    index = 0  # pointer to current index for the sorted array Half

    while pointer1 < len(left_half) and pointer2 < len(right_half):
        if left_half[pointer1] < right_half[pointer2]:
            sorted_array[index] = left_half[pointer1]
            pointer1 += 1
            index += 1
        else:
            sorted_array[index] = right_half[pointer2]
            pointer2 += 1
            index += 1
    while pointer1 < len(left_half):
        sorted_array[index] = left_half[pointer1]
        pointer1 += 1
        index += 1

    while pointer2 < len(right_half):
        sorted_array[index] = right_half[pointer2]
        pointer2 += 1
        index += 1

    return sorted_array


def merge_sort(array: List) -> List:
    """Returns a list of sorted array elements using merge sort.

    >>> from random import shuffle
    >>> array = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> shuffle(array)
    >>> merge_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]

    >>> shuffle(array)
    >>> merge_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]

    >>> array = [-200]
    >>> merge_sort(array)
    [-200]

    >>> array = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> shuffle(array)
    >>> sorted(array) == merge_sort(array)
    True

    >>> array = [-2]
    >>> merge_sort(array)
    [-2]

    >>> array = []
    >>> merge_sort(array)
    []

    >>> array = [10000000, 1, -1111111111, 101111111112, 9000002]
    >>> sorted(array) == merge_sort(array)
    True
    """
    if len(array) <= 1:
        return array
    # the actual formula to calculate the middle element = left + (right - left) // 2
    # this avoids integer overflow in case of large N
    middle = 0 + (len(array) - 0) // 2

    # Split the array into halves till the array length becomes equal to One
    # merge the arrays of single length returned by mergeSort function and
    # pass them into the merge arrays function which merges the array
    left_half = array[:middle]
    right_half = array[middle:]

    return merge(merge_sort(left_half), merge_sort(right_half))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
