from typing import List


def a_very_big_sum(arr: List[int]) -> int:
    """
    Return the sum of all integers in the input array.

    >>> a_very_big_sum([2, 4, 6, 2, 4, 6, 3])
    27
    >>> a_very_big_sum([])
    0
    >>> a_very_big_sum([1000000000, 2000000000])
    3000000000
    """
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements in the array must be integers")

    total = 0
    for number in arr:
        total += number
    return total
