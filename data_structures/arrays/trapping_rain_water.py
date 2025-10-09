"""
Trapping Rain Water

Given an array of non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Problem: LeetCode #42 (Hard)
Link: https://leetcode.com/problems/trapping-rain-water

Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""


def trap(height):
    """
    Calculate the amount of water trapped after raining.

    Args:
        height (List[int]): List of non-negative integers representing elevation map.

    Returns:
        int: Total units of trapped rainwater.

    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains negative values.
    """
    if not isinstance(height, list):
        raise TypeError("Input must be a list of integers.")
    if any(h < 0 for h in height):
        raise ValueError("Elevation map cannot contain negative values.")

    if len(height) < 3:
        return 0  # At least 3 bars needed to trap water

    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    total_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                total_water += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                total_water += max_right - height[right]
            right -= 1

    return total_water


# Example usage and test
if __name__ == "__main__":
    # Test case from LeetCode
    elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trap(elevation_map)
    print(f"Trapped Rain Water: {result} units")  # Output: 6

    # Additional edge cases
    print(trap([]))           # 0
    print(trap([1]))          # 0
    print(trap([3, 0, 2, 0, 4]))  # 7
