from typing import List


def check_polygon(nums: List) -> bool:
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
    >>> check_polygon([])
    Traceback (most recent call last):
        ...
    ValueError: List is invalid
    """
    if not nums:
        raise ValueError("List is invalid")
    nums.sort()
    return nums.pop() < sum(nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
