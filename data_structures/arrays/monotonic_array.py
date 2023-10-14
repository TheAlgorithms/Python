class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """
        Check if an array is monotonic (either increasing or decreasing).

        Args:
            nums (list[int]): The input array to check for monotonicity.

        Returns:
            bool: True if the array is monotonic (either increasing or decreasing), False otherwise.
        """

        is_increasing = True  # Indicates if the array is increasing.
        is_decreasing = True  # Indicates if the array is decreasing.

        # Check if the array is either increasing or non-increasing.
        for i in range(1, len(nums)):
            # Check increasing condition.
            if nums[i] < nums[i - 1]:
                is_increasing = False

            # Check decreasing condition.
            elif nums[i] > nums[i - 1]:
                is_decreasing = False

            # If it is neither increasing nor decreasing then don't continue the loop.
            if not is_increasing and not is_decreasing:
                break

        return is_increasing or is_decreasing  # Return true if either condition is met

# Test cases
if __name__ == '__main__':
    solution = Solution()
    assert solution.isMonotonic([1, 2, 2, 3]) is True  # Increasing
    assert solution.isMonotonic([3, 2, 1]) is True  # Decreasing
    assert solution.isMonotonic([1, 3, 2]) is False  # Not monotonic
    assert solution.isMonotonic([1, 1, 1, 1]) is True  # All equal values are considered monotonic
    assert solution.isMonotonic([1]) is True  # Single-element array is considered monotonic
    assert solution.isMonotonic([]) is True  # Empty array is considered monotonic
