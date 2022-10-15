from __future__ import annotations


# Divide and Conquer algorithm
def find_max(nums: list[int | float], left: int, right: int) -> int | float:
    """
    find max value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: max in nums

    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_max(nums, 0, len(nums) - 1) == max(nums)
    True
    True
    True
    True
    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_max(nums, 0, len(nums) - 1) == max(nums)
    True
    >>> find_max([], 0, 0)
    Traceback (most recent call last):
        ...
    ValueError: find_max() arg is an empty sequence
    >>> find_max(nums, 0, len(nums)) == max(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> find_max(nums, -len(nums), -1) == max(nums)
    True
    >>> find_max(nums, -len(nums) - 1, -1) == max(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    if len(nums) == 0:
        raise ValueError("find_max() arg is an empty sequence")
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
    left_max = find_max(nums, left, mid)  # find max in range[left, mid]
    right_max = find_max(nums, mid + 1, right)  # find max in range[mid + 1, right]

    return left_max if left_max >= right_max else right_max


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
