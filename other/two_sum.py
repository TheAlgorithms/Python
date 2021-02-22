"""
Given an array of integers, return indices of the two numbers such that they add up to
a specific target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([15, 2, 11, 7], 13)
    [1, 2]
    >>> two_sum([2, 7, 11, 15], 17)
    [0, 3]
    >>> two_sum([7, 15, 11, 2], 18)
    [0, 2]
    >>> two_sum([2, 7, 11, 15], 26)
    [2, 3]
    >>> two_sum([2, 7, 11, 15], 8)
    []
    >>> two_sum([3 * i for i in range(10)], 19)
    []
    """
    chk_map = {}
    for index, val in enumerate(nums):
        compl = target - val
        if compl in chk_map:
            return [chk_map[compl], index]
        chk_map[val] = index
    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{two_sum([2, 7, 11, 15], 9) = }")
