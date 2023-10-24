from typing import List, Optional

def binary_search(arr: List[int], target: int, low: int, high: int) -> Optional[int]:
    """
    Perform a recursive binary search to find the target value in a sorted array.

    Args:
        arr (List[int]): The sorted array to search in.
        target (int): The value to search for.
        low (int): The low index of the search range.
        high (int): The high index of the search range.

    Returns:
        Optional[int]: The index of the target element if found, or None if not found.
    """
    if low > high:
        return None  # Element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Element found at index 'mid'
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Search in the right half

# Example usage and doctest
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)
if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found")
