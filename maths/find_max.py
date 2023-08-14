from __future__ import annotations


def find_max_iterative(nums: list[int | float]) -> int | float:
    """
    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_max_iterative(nums) == max(nums)
    True
    True
    True
    True
    >>> find_max_iterative([2, 4, 9, 7, 19, 94, 5])
    94
    >>> find_max_iterative([])
    Traceback (most recent call last):
        ...
    ValueError: find_max_iterative() arg is an empty sequence
    """
    if len(nums) == 0:
        raise ValueError("find_max_iterative() arg is an empty sequence")
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num


# Divide and Conquer algorithm
def find_max_recursive(nums: list[int | float], left: int, right: int) -> int | float:
    """
    find max value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: max in nums

    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_max_recursive(nums, 0, len(nums) - 1) == max(nums)
    True
    True
    True
    True
    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_max_recursive(nums, 0, len(nums) - 1) == max(nums)
    True
    >>> find_max_recursive([], 0, 0)
    Traceback (most recent call last):
        ...
    ValueError: find_max_recursive() arg is an empty sequence
    >>> find_max_recursive(nums, 0, len(nums)) == max(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> find_max_recursive(nums, -len(nums), -1) == max(nums)
    True
    >>> find_max_recursive(nums, -len(nums) - 1, -1) == max(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    if len(nums) == 0:
        raise ValueError("find_max_recursive() arg is an empty sequence")
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
    left_max = find_max_recursive(nums, left, mid)  # find max in range[left, mid]
    right_max = find_max_recursive(
        nums, mid + 1, right
    )  # find max in range[mid + 1, right]

    return left_max if left_max >= right_max else right_max


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
