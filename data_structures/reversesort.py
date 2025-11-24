def reverse_selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts an array using a modified selection sort algorithm where after finding
    the minimum element, a subarray is reversed instead of swapping.

    Parameters:
    arr (list[int]): The list of integers to sort.

    Returns:
    list[int]: The sorted list of integers.

    Example:
    >>> reverse_selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]

    >>> reverse_selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> reverse_selection_sort([3, 1, 2])
    [1, 2, 3]

    >>> reverse_selection_sort([10])
    [10]

    >>> reverse_selection_sort([])
    []
    """

    n = len(arr)

    # Iterate over each position of the array
    for i in range(n - 1):
        # Find the index of the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # If the minimum is not already at position i, reverse the subarray
        if min_index != i:
            # Reverse the subarray from position i to min_index
            arr[i : min_index + 1] = reversed(arr[i : min_index + 1])

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
