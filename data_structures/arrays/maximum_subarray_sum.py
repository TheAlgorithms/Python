def max_subarray_sum(arr: list[int]) -> int:
    """
    Find the maximum sum of a subarray.

    Args:
        arr: array of numbers.

    Returns:
        Maximum sum possible in a subarray

    Examples:
        >>> max_subarray_sum([1, 3, 2])
        6

        >>> max_subarray_sum([1, 2, 3, -1, 0])
        6
    """
    ans = arr[0]

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum = current_sum + arr[j]
            ans = max(ans, current_sum)

    return ans


if __name__ == "__main__":
    print(max_subarray_sum([1, 2, 3, 4, 5]))
    import doctest

    doctest.testmod()
