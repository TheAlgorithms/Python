from __future__ import annotations


# Divide and Conquer algorithm
def find_min(nums: list[int | float], left: int, right: int) -> int | float:
    """
    find min value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: min in nums

    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_min(nums, 0, len(nums) - 1) == min(nums)
    True
    True
    True
    True
    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_min(nums, 0, len(nums) - 1) == min(nums)
    True
    >>> find_min([], 0, 0)
    Traceback (most recent call last):
        ...
    ValueError: find_min() arg is an empty sequence
    >>> find_min(nums, 0, len(nums)) == min(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> find_min(nums, -len(nums), -1) == min(nums)
    True
    >>> find_min(nums, -len(nums) - 1, -1) == min(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    if len(nums) == 0:
        raise ValueError("find_min() arg is an empty sequence")
    if (
        left >= len(nums)
        or left < -len(nums)
        or right >= len(nums)
        or right < -len(nums)
    ):
        raise IndexError("list index out of range")
    if left == right:
        return nums[left]
    mid = (left + right) >> 1  # the middle
    left_min = find_min(nums, left, mid)  # find min in range[left, mid]
    right_min = find_min(nums, mid + 1, right)  # find min in range[mid + 1, right]

    return left_min if left_min <= right_min else right_min


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
