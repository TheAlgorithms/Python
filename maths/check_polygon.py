from __future__ import annotations


def check_polygon(nums: list[float]) -> bool:
    """
    Takes list of possible side lengths and determines whether a
    two-dimensional polygon with such side lengths can exist.

    Returns a boolean value for the < comparison
    of the largest side length with sum of the rest.
    Wiki: https://en.wikipedia.org/wiki/Triangle_inequality

    >>> check_polygon([6, 10, 5])
    True
    >>> check_polygon([3, 7, 13, 2])
    False
    >>> check_polygon([1, 4.3, 5.2, 12.2])
    False
    >>> nums = [3, 7, 13, 2]
    >>> _ = check_polygon(nums) #   Run function, do not show answer in output
    >>> nums #  Check numbers are not reordered
    [3, 7, 13, 2]
    >>> check_polygon([])
    Traceback (most recent call last):
        ...
    ValueError: Monogons and Digons are not polygons in the Euclidean space
    >>> check_polygon([-2, 5, 6])
    Traceback (most recent call last):
        ...
    ValueError: All values must be greater than 0
    """
    if len(nums) < 2:
        raise ValueError("Monogons and Digons are not polygons in the Euclidean space")
    if any(i <= 0 for i in nums):
        raise ValueError("All values must be greater than 0")
    copy_nums = nums.copy()
    copy_nums.sort()
    return copy_nums[-1] < sum(copy_nums[:-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
