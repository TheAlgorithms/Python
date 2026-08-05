def binary_search_first_occurrence(arr: list[int], target: int) -> int:
    """
    Return the index of the first occurrence of target in a sorted list.

    >>> binary_search_first_occurrence([1, 2, 4, 4, 4, 5], 4)
    2
    >>> binary_search_first_occurrence([1, 2, 3], 5)
    -1
    """
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
