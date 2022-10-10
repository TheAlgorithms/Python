"""
Referencing the Big O Notation, this algorithm has a liner time complexity, O(N).
In the worst case scenario, the iterator will pass through each item's list and
check if the item is the maximum item or not. If the list's size is N, the algorithm
will make N operations, leading to O(N) complexity.
[https://en.wikipedia.org/wiki/Big_O_notation#Use_in_computer_science]
"""


from __future__ import annotations


def find_max(nums: list[int | float]) -> int | float:
    """
    >>> for nums in ([3, 2, 1], [-3, -2, -1], [3, -3, 0], [3.0, 3.1, 2.9]):
    ...     find_max(nums) == max(nums)
    True
    True
    True
    True
    >>> find_max([2, 4, 9, 7, 19, 94, 5])
    94
    >>> find_max([])
    Traceback (most recent call last):
        ...
    ValueError: find_max() arg is an empty sequence
    """
    if len(nums) == 0:
        raise ValueError("find_max() arg is an empty sequence")
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
