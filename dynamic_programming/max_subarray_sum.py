def max_sub_array_sum(arr: list[int], size: int) -> int:
    """
    Finds the maximum sum of a subarray within the given array using Kadane's algorithm.

    Args:
        arr (list): The input array of numbers.
        size (int): The size of the array.

    Returns:
        int: The maximum sum of a subarray within the array.

    Example:
        >>> arr = [-2, -3, 4, -1, -2, 5, -3]
        >>> max_sub_array_sum(arr, len(arr))
        6
        In this example, the input array is [-2, -3, 4, -1, -2, 5, -3].
        The maximum sum of a subarray within this array is 6,
        which corresponds to the subarray [4, -1, -2, 5].

        >>> arr = [-3, -4, 5, -1, 2, -4, 6, -1]
        >>> max_sub_array_sum(arr, len(arr))
        8

    References:
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    max_till_now = arr[0]
    max_ending = 0

    for i in range(size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        elif max_till_now < max_ending:
            max_till_now = max_ending

    return max_till_now


if __name__ == "__main__":
    import doctest

    doctest.testmod()
