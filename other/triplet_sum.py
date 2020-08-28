"""
Given an array of integers and another integer X,
we are required to find a triplet from the array such that it's sum is equal to X
"""
from typing import List
from itertools import permutations
from timeit import repeat


def triplet_sum1(arr: List[int], target: int) -> Tuple[int, int, int]:
    """
    Returns a triplet in in array with sum equal to X,
    else (0, 0, 0).
    >>> triplet_sum1([13, 29, 7, 23, 5], 35)
    (5, 7, 23)
    >>> triplet_sum1([37, 9, 19, 50, 44], 65)
    (9, 19, 37)
    >>> arr = [6, 47, 27, 1, 15]
    >>> summ = 11
    >>> triplet_sum1(arr,summ)
    (0, 0, 0)
    """
    for triplet in permutations(arr, 3):
        if sum(triplet) == X:
            return tuple(sorted(triplet))
    return (0, 0, 0)


def sol1_time() -> str:
    setup_code = """ 
from __main__ import triplet_sum1
from random import randint"""
    test_code = """
arr = [randint(-1000, 1000) for i in range(10)]
r = randint(-5000, 5000)
triplet_sum1(arr,r)
    """
    times = repeat(stmt=test_code, setup=setup_code, repeat=5, number=10000)
    return f"Naive solution time is {min(times)}"


def triplet_sum2(arr: List[int], X: int) -> tuple:
    """
    Returns a triplet in in array with sum equal to X,
    else (0, 0, 0).
    >>> triplet_sum2([13, 29, 7, 23, 5], 35)
    (5, 7, 23)
    >>> triplet_sum2([37, 9, 19, 50, 44], 65)
    (9, 19, 37)
    >>> arr = [6, 47, 27, 1, 15]
    >>> summ = 11
    >>> triplet_sum2(arr,summ)
    (0, 0, 0)
    """
    arr.sort()
    n = len(arr)
    for i in range(n - 1):
        left, right = i + 1, n - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] == X:
                return (arr[i], arr[left], arr[right])
            elif arr[i] + arr[left] + arr[right] < X:
                left += 1
            elif arr[i] + arr[left] + arr[right] > X:
                right -= 1
    else:
        return (0, 0, 0)


def sol2_time() -> str:
    setup_code = """ 
from __main__ import triplet_sum2
from random import randint"""
    test_code = """
arr = [randint(-1000, 1000) for i in range(10)]
r = randint(-5000, 5000)
triplet_sum2(arr,r)
    """
    times = repeat(stmt=test_code, setup=setup_code, repeat=5, number=10000)
    return f"Optimized solution time is {min(times)}"


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    from random import randint

    arr = [randint(-1000, 1000) for i in range(100)]
    r = randint(-5000, 5000)
    print(f"{triplet_sum1(arr,r)}")
    print(f"{sol1_time()}")
    print(f"{triplet_sum2(arr,r)}")
    print(f"{sol2_time()}")
