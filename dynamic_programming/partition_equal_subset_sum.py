"""
Partition Equal Subset Sum

Given a list of positive integers, determine whether it can be partitioned
into two subsets such that the sum of elements in both subsets is equal.

This is a classic dynamic-programming problem equivalent to asking:
"Does any subset of the list sum to exactly half the total?"

If the total sum is odd, no equal partition exists.
If the total sum is even, we run a 1-D DP (bitset / boolean array) to check
whether the target value (total // 2) is reachable.

Time Complexity  : O(n * total_sum)
Space Complexity : O(total_sum)

References:
- https://en.wikipedia.org/wiki/Partition_problem
- https://leetcode.com/problems/partition-equal-subset-sum/
"""


def partition_equal_subset_sum(nums: list[int]) -> bool:
    """
    Return True if *nums* can be split into two subsets with equal sum,
    False otherwise.

    Args:
        nums: A list of positive integers.

    Returns:
        True  if an equal-sum partition exists, False otherwise.

    Raises:
        ValueError: If *nums* is empty or contains a non-positive integer.

    Examples:
        >>> partition_equal_subset_sum([1, 5, 11, 5])
        True
        >>> partition_equal_subset_sum([1, 2, 3, 5])
        False
        >>> partition_equal_subset_sum([1, 1])
        True
        >>> partition_equal_subset_sum([3, 3, 3, 4, 5])
        True
        >>> partition_equal_subset_sum([2])
        False
        >>> partition_equal_subset_sum([1, 2, 5])
        False
        >>> partition_equal_subset_sum([100])
        False
    """
    if not nums:
        raise ValueError("nums must be a non-empty list.")
    if any(n <= 0 for n in nums):
        raise ValueError("All elements of nums must be positive integers.")

    total = sum(nums)

    # An odd total can never be split into two equal integer-sum subsets.
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[s] is True if sum s is achievable with some subset of nums seen so far.
    # We start knowing that the empty subset achieves sum 0.
    dp: list[bool] = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Traverse right-to-left to avoid counting the same element twice
        # (0/1 knapsack style).
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

        if dp[target]:
            # Early exit: target already reachable.
            return True

    return dp[target]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Partition Equal Subset Sum — Demo")
    print("=" * 42)

    examples: list[tuple[list[int], bool]] = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 1], True),
        ([3, 3, 3, 4, 5], True),
        ([2], False),
        ([1, 2, 5], False),
        ([2, 2, 1, 1], True),
        ([7, 3, 1, 5, 4], True),
    ]

    for nums, expected in examples:
        result = partition_equal_subset_sum(nums)
        status = "✓" if result == expected else "✗"
        print(f"  {status}  {nums!s:<25}  →  {result}")
