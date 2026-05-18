#!/usr/bin/env python3


def house_robber(nums: list[int]) -> int:
    """
    LeetCode No.198: House Robber
    Given a list of non-negative integers representing the amount of money in each
    house, determine the maximum amount you can rob tonight without alerting the police.
    You cannot rob two adjacent houses.

    Args:
        nums: list of non-negative integers representing money in each house

    Returns:
        Maximum amount of money that can be robbed

    Raises:
        AssertionError: nums is not a list of non-negative integers

    Examples:
        >>> house_robber([1, 2, 3, 1])
        4
        >>> house_robber([2, 7, 9, 3, 1])
        12
        >>> house_robber([0])
        0
        >>> house_robber([])
        0
        >>> house_robber([5])
        5
        >>> house_robber([-1, 2])  # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        AssertionError: nums must contain only non-negative integers, got -1
    """
    assert isinstance(nums, list), "nums must be a list"
    for num in nums:
        assert isinstance(num, int) and num >= 0, (
            f"nums must contain only non-negative integers, got {num}"
        )

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev_prev = 0  # max profit up to i-2
    prev = nums[0]  # max profit up to i-1

    for i in range(1, len(nums)):
        current = max(prev, prev_prev + nums[i])
        prev_prev = prev
        prev = current

    return prev


if __name__ == "__main__":
    import doctest

    doctest.testmod()
