from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    """
    Finds the first and last position of a given target value in a sorted array.

    Args:
        nums: A sorted list of integers.
        target: The integer to search for.

    Returns:
        A list containing the starting and ending index of the target.
        Returns [-1, -1] if the target is not found.
    """

    def find_bound(is_first: bool) -> int:
        """Helper to find the leftmost or rightmost occurrence of the target."""
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # Continue searching on the left
                else:
                    left = mid + 1  # Continue searching on the right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first_bound = find_bound(True)
    if first_bound == -1:
        return [-1, -1]

    last_bound = find_bound(False)
    return [first_bound, last_bound]
