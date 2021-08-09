from typing import List


def check_polygon(nums: List) -> bool:
    """
    Takes list of possible sidelengths and determines whether a two-dimensional polygon with such sidelengths can exist.
    Return a boolean value for the < comparison of the largest sidelength with sum of the rest.
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
