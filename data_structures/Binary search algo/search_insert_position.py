from typing import List

def search_insert(nums: List[int], target: int) -> int:
    """
    Finds the index to insert a target value into a sorted list.

    If the target is found, its index is returned. Otherwise, returns the
    index where it would be if it were inserted in order.

    Args:
        nums: A sorted list of integers.
        target: The integer to search for.

    Returns:
        The index for the target value.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left