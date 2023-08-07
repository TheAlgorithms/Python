from __future__ import annotations


def find_min(nums: list[int | float]) -> int | float:
    """
    Find Minimum Number in a List
    :param nums: contains elements
    :return: min number in list

    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_min(nums) == min(nums)
    True
    True
    True
    True
    >>> find_min([0, 1, 2, 3, 4, 5, -3, 24, -56])
    -56
    >>> find_min([])
    Traceback (most recent call last):
        ...
    ValueError: find_min() arg is an empty sequence
    """
    if len(nums) == 0:
        raise ValueError("find_min() arg is an empty sequence")
    min_num = nums[0]
    for num in nums:
        min_num = min(min_num, num)
    return min_num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
