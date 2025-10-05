"""
Rotate an array to the right by k steps.
"""


def rotate(nums: list[int], k: int) -> list[int]:
    """
    Rotate the array to the right by k steps.

    Args:
        nums: List of integers.
        k: Number of steps to rotate.

    Returns:
        The rotated list.

    Examples:
        >>> rotate([1,2,3,4,5,6,7], 3)
        [5, 6, 7, 1, 2, 3, 4]

        >>> rotate([-1,-100,3,99], 2)
        [3, 99, -1, -100]
    """
    n = len(nums)
    k = k % n  # In case k > n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
