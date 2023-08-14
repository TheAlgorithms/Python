from __future__ import annotations


def find_min_iterative(nums: list[int | float]) -> int | float:
    """
    Find Minimum Number in a List
    :param nums: contains elements
    :return: min number in list

    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_min_iterative(nums) == min(nums)
    True
    True
    True
    True
    >>> find_min_iterative([0, 1, 2, 3, 4, 5, -3, 24, -56])
    -56
    >>> find_min_iterative([])
    Traceback (most recent call last):
        ...
    ValueError: find_min_iterative() arg is an empty sequence
    """
    if len(nums) == 0:
        raise ValueError("find_min_iterative() arg is an empty sequence")
    min_num = nums[0]
    for num in nums:
        min_num = min(min_num, num)
    return min_num


# Divide and Conquer algorithm
def find_min_recursive(nums: list[int | float], left: int, right: int) -> int | float:
    """
    find min value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: min in nums

    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_min_recursive(nums, 0, len(nums) - 1) == min(nums)
    True
    True
    True
    True
    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_min_recursive(nums, 0, len(nums) - 1) == min(nums)
    True
    >>> find_min_recursive([], 0, 0)
    Traceback (most recent call last):
        ...
    ValueError: find_min_recursive() arg is an empty sequence
    >>> find_min_recursive(nums, 0, len(nums)) == min(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> find_min_recursive(nums, -len(nums), -1) == min(nums)
    True
    >>> find_min_recursive(nums, -len(nums) - 1, -1) == min(nums)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    if len(nums) == 0:
        raise ValueError("find_min_recursive() arg is an empty sequence")
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
    left_min = find_min_recursive(nums, left, mid)  # find min in range[left, mid]
    right_min = find_min_recursive(
        nums, mid + 1, right
    )  # find min in range[mid + 1, right]

    return left_min if left_min <= right_min else right_min


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
