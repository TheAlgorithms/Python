from typing import List


def binary_search(arr: List[int], left: int, right: int, target: int) -> int:
    """
    Perform binary search on a sorted array.

    Parameters:
    arr (List[int]): The sorted list in which to search.
    left (int): The starting index for the search range.
    right (int): The ending index for the search range.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.

    Doctest:
    >>> binary_search([2, 3, 4, 10, 40], 0, 4, 10)
    3
    >>> binary_search([2, 3, 4, 10, 40], 0, 4, 5)
    -1
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr: List[int], target: int) -> int:
    """
    Perform exponential search on a sorted array.

    Exponential search first finds a range where the target may reside
    by repeatedly doubling the index. It then performs binary search
    within that range.

    Parameters:
    arr (List[int]): The sorted list in which to search.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.

    Doctest:
    >>> exponential_search([2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100], 10)
    3
    >>> exponential_search([2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100], 5)
    -1
    """
    n = len(arr)

    # If the target is at the first position
    if arr[0] == target:
        return 0

    # Find the range for binary search by repeatedly doubling the index
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Perform binary search within the found range
    return binary_search(arr, i // 2, min(i, n - 1), target)


if __name__ == "__main__":
    """
    Example to demonstrate the usage of exponential_search function.
    """
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    target = 10

    result = exponential_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")
