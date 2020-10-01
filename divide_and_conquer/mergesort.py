def merge(left_half, right_half):
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


def merge_sort(array):
    """
    >>> from random import shuffle
    >>> array = [-2, 3, -10, 11, 99, 100000, 100, -200]
    >>> shuffle(array)
    >>> merge_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]
    >>> shuffle(array)
    >>> merge_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]
    >>> shuffle(array)
    >>> merge_sort(array)
    [-200, -10, -2, 3, 11, 99, 100, 100000]
    """
    if len(array) == 1:
        return array

    middle = len(array) // 2

    # Split the array into halves till the array length becomes equal to One
    # merge the arrays of single length returned by mergeSort function and
    # pass them into the merge arrays function which merges the array
    left_half = array[:middle]
    right_half = array[middle:]

    return merge(merge_sort(left_half), merge_sort(right_half))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
