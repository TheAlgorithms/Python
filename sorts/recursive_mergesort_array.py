"""A merge sort which accepts an array as input and recursively
splits an array in half and sorts and combines them.
"""

"""https://en.wikipedia.org/wiki/Merge_sort """


def merge(arr: list[int]) -> list[int]:
    """Return a sorted array.
    >>> merge([10,9,8,7,6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([1,2,3,4,5,6,7,8,9,10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([10,22,1,2,3,9,15,23])
    [1, 2, 3, 9, 10, 15, 22, 23]
    >>> merge([100])
    [100]
    >>> merge([])
    []
    """
    if len(arr) > 1:
        middle_length = len(arr) // 2  # Finds the middle of the array
        left_array = arr[
            :middle_length
        ]  # Creates an array of the elements in the first half.
        right_array = arr[
            middle_length:
        ]  # Creates an array of the elements in the second half.
        left_size = len(left_array)
        right_size = len(right_array)
        merge(left_array)  # Starts sorting the left.
        merge(right_array)  # Starts sorting the right
        left_index = 0  # Left Counter
        right_index = 0  # Right Counter
        index = 0  # Position Counter
        while (
            left_index < left_size and right_index < right_size
        ):  # Runs until the lowers size of the left and right are sorted.
            if left_array[left_index] < right_array[right_index]:
                arr[index] = left_array[left_index]
                left_index = left_index + 1
            else:
                arr[index] = right_array[right_index]
                right_index = right_index + 1
            index = index + 1
        while (
            left_index < left_size
        ):  # Adds the left over elements in the left half of the array
            arr[index] = left_array[left_index]
            left_index = left_index + 1
            index = index + 1
        while (
            right_index < right_size
        ):  # Adds the left over elements in the right half of the array
            arr[index] = right_array[right_index]
            right_index = right_index + 1
            index = index + 1
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
