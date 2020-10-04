# Video Explanation: https://www.youtube.com/watch?v=6w60Zi1NtL8&feature=emb_logo

from __future__ import annotations


def maximum_non_adjacent_sum(nums: list[int]) -> int:
    """
    Find the maximum non-adjacent sum of the integers in the nums input list

    >>> print(maximum_non_adjacent_sum([1, 2, 3]))
    4
    >>> maximum_non_adjacent_sum([1, 5, 3, 7, 2, 2, 6])
    18
    >>> maximum_non_adjacent_sum([-1, -5, -3, -7, -2, -2, -6])
    0
    >>> maximum_non_adjacent_sum([499, 500, -3, -7, -2, -2, -6])
    500
    """
    if not nums:
        return 0
    max_including = nums[0]
    max_excluding = 0
    for num in nums[1:]:
        max_including, max_excluding = (
            max_excluding + num,
            max(max_including, max_excluding),
        )
    return max(max_excluding, max_including)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
