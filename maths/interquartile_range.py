"""
This is the implementation of inter_quartile range (IQR).

function takes the list of numeric values as input
and return the IQR as output.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Interquartile_range
"""
from __future__ import annotations


def find_median(nums: list[int | float]) -> float:
    """
    This is the implementation of median.
    :param nums: The list of numeric nums
    :return: Median of the list
    >>> find_median(nums=([1,2,2,3,4]))
    2

    >>> find_median(nums=([1,2,2,3,4,4]))
    2.5


    """
    length = len(nums)
    if length % 2:
        return nums[length // 2]
    return float((nums[length // 2] + nums[(length // 2) - 1]) / 2)


def interquartile_range(nums: list[int | float]) -> float:
    """
    This is the implementation of inter_quartile
    range for a list of numeric.
    :param nums: The list of data point
    :return: Inter_quartile range

    >>> interquartile_range(nums=[4,1,2,3,2])
    2.0


    >>> interquartile_range(nums=[])
    Traceback (most recent call last):
    ...
    ValueError: The list is empty. Provide a non-empty list.

    >>> interquartile_range(nums = [-2,-7,-10,9,8,4, -67, 45])
    17.0

    >>> interquartile_range(nums = [0,0,0,0,0])
    0.0



    """
    length = len(nums)
    if length == 0:
        raise ValueError("The list is empty. Provide a non-empty list.")
    nums.sort()
    div, mod = divmod(length, 2)
    q1 = find_median(nums[:div])
    half_length = sum((div, mod))
    q3 = find_median(nums[half_length:length])
    return q3 - q1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
