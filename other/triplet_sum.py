"""
Given an array of integers and another integer target,
we are required to find a triplet from the array such that it's sum is equal to
the target.
"""
from itertools import permutations
from random import randint
from timeit import repeat
from typing import List, Tuple


def make_dataset() -> Tuple[List[int], int]:
    arr = [randint(-1000, 1000) for i in range(10)]
    r = randint(-5000, 5000)
    return (arr, r)


dataset = make_dataset()


def triplet_sum1(arr: List[int], target: int) -> Tuple[int, int, int]:
    """
    Returns a triplet in in array with sum equal to target,
    else (0, 0, 0).
    >>> triplet_sum1([13, 29, 7, 23, 5], 35)
    (5, 7, 23)
    >>> triplet_sum1([37, 9, 19, 50, 44], 65)
    (9, 19, 37)
    >>> arr = [6, 47, 27, 1, 15]
    >>> target = 11
    >>> triplet_sum1(arr, target)
    (0, 0, 0)
    """
    for triplet in permutations(arr, 3):
        if sum(triplet) == target:
            return tuple(sorted(triplet))
    return (0, 0, 0)


def triplet_sum2(arr: List[int], target: int) -> Tuple[int, int, int]:
    """
    Returns a triplet in in array with sum equal to target,
    else (0, 0, 0).
    >>> triplet_sum2([13, 29, 7, 23, 5], 35)
    (5, 7, 23)
    >>> triplet_sum2([37, 9, 19, 50, 44], 65)
    (9, 19, 37)
    >>> arr = [6, 47, 27, 1, 15]
    >>> target = 11
    >>> triplet_sum2(arr, target)
    (0, 0, 0)
    """
    arr.sort()
    n = len(arr)
    for i in range(n - 1):
        left, right = i + 1, n - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] == target:
                return (arr[i], arr[left], arr[right])
            elif arr[i] + arr[left] + arr[right] < target:
                left += 1
            elif arr[i] + arr[left] + arr[right] > target:
                right -= 1
    else:
        return (0, 0, 0)


def solution_times() -> Tuple[float, float]:
    setup_code = """
from __main__ import dataset, triplet_sum1, triplet_sum2
"""
    test_code1 = """
triplet_sum1(*dataset)
"""
    test_code2 = """
triplet_sum2(*dataset)
"""
    times1 = repeat(setup=setup_code, stmt=test_code1, repeat=5, number=10000)
    times2 = repeat(setup=setup_code, stmt=test_code2, repeat=5, number=10000)
    return (min(times1), min(times2))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    times = solution_times()
    print(f"The time for naive implementation is {times[0]}.")
    print(f"The time for optimized implementation is {times[1]}.")
