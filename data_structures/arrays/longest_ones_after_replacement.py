class LongestOnesAfterReplacement:
    """
    Problem:
    Given a binary array and an integer max_zero_flips, find the length of the
    longest subarray containing only 1s after flipping at most max_zero_flips
    zeros.

    Example:
    >>> solver = LongestOnesAfterReplacement()
    >>> solver.longest_ones([1, 0, 1, 1, 0, 1], 1)
    4
    """

    def longest_ones(self, nums: list[int], max_zero_flips: int) -> int:
        left = 0
        max_len = 0
        zeros_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count > max_zero_flips:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solver = LongestOnesAfterReplacement()
    print(
        "Longest Ones After Replacement:",
        solver.longest_ones([1, 0, 1, 1, 0, 1], 1),
    )

