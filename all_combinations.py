"""
        In this problem, we want to determine all possible combinations of k
        numbers out of 1 ... n. We use backtracking to solve this problem.

        Time complexity: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!))),
"""
from __future__ import annotations

from itertools import combinations


def combination_lists(n: int, k: int) -> list[list[int]]:
    """
    >>> combination_lists(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    return [list(x) for x in combinations(range(1, n + 1), k)]


def generate_all_combinations(n: int, k: int) -> list[list[int]]:
    """
    >>> generate_all_combinations(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    >>> generate_all_combinations(n=0, k=0)
    [[]]
    >>> generate_all_combinations(n=10, k=-1)
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded
    >>> generate_all_combinations(n=-1, k=10)
    []
    >>> generate_all_combinations(n=5, k=4)
    [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
    >>> from itertools import combinations
    >>> all(generate_all_combinations(n, k) == combination_lists(n, k)
    ...     for n in range(1, 6) for k in range(1, 6))
    True
    """

    result: list[list[int]] = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(
    increment: int,
    total_number: int,
    level: int,
    current_list: list[int],
    total_list: list[list[int]],
) -> None:
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(generate_all_combinations(n=4, k=2))
    tests = ((n, k) for n in range(1, 5) for k in range(1, 5))
    for n, k in tests:
        print(n, k, generate_all_combinations(n, k) == combination_lists(n, k))

    print("Benchmark:")
    from timeit import timeit

    for func in ("combination_lists", "generate_all_combinations"):
        print(f"{func:>25}(): {timeit(f'{func}(n=4, k = 2)', globals=globals())}")
