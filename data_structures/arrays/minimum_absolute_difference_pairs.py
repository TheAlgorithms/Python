def minimum_absolute_difference_pairs(arr: list[int]) -> list[list[int]]:
    """
    Given an array of distinct integers, return all pairs of elements
    with the minimum absolute difference.

    Args:
        arr: list of integers

    Returns:
        list of pairs (as lists) with the minimum absolute difference

    Examples:
        >>> minimum_absolute_difference_pairs([4, 2, 1, 3])
        [[1, 2], [2, 3], [3, 4]]
        >>> minimum_absolute_difference_pairs([1, 3, 6, 10, 15])
        [[1, 3]]
        >>> minimum_absolute_difference_pairs([3, 8, -10, 23, 19, -4, -14, 27])
        [[-14, -10], [19, 23], [23, 27]]
        >>> minimum_absolute_difference_pairs([])
        []
        >>> minimum_absolute_difference_pairs([5])
        []
    """
    if len(arr) < 2:
        return []

    # Sort array for adjacent difference comparison
    arr.sort()

    # Find minimum difference
    min_diff = float("inf")
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])

    # Collect all pairs with minimum difference
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == min_diff:
            result.append([arr[i - 1], arr[i]])

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()
