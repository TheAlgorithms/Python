"""
Partition a set into two subsets such that the difference of subset sums is minimum
"""

from collections.abc import Iterable


def find_min(numbers: Iterable[int]) -> int:
    """
    >>> find_min([1, 2, 3, 4, 5])
    1
    >>> find_min([5, 5, 5, 5, 5])
    5
    >>> find_min([5, 5, 5, 5])
    0
    >>> find_min([3])
    3
    >>> find_min([])
    0
    >>> find_min([1, 2, 3, 4])
    0
    >>> find_min([0, 0, 0, 0])
    0
    >>> find_min([-1, -5, 5, 1])
    0
    >>> find_min([9, 9, 9, 9, 9])
    9
    >>> find_min([1, 5, 10, 3])
    1
    >>> find_min([-1, 0, 1])
    0
    >>> find_min(range(10, 0, -1))
    1
    >>> find_min([-1])
    1
    >>> find_min([0, 0, 0, 1, 2, -4])
    1
    >>> find_min([-1, -5, -10, -3])
    1
    """
    total_sum = 0
    reachable_sums = {0}

    for number in numbers:
        total_sum += number
        reachable_sums |= {reachable_sum + number for reachable_sum in reachable_sums}

    return min(abs(total_sum - 2 * reachable_sum) for reachable_sum in reachable_sums)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
