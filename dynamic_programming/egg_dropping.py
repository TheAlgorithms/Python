"""
Dynamic Programming - Egg Dropping Problem

The Egg Dropping Puzzle:
------------------------
You are given k eggs and n floors. Find the minimum number of trials needed
in the worst case to find the critical floor from which the egg starts breaking.

Reference:
https://en.wikipedia.org/wiki/Dynamic_programming#Egg_dropping_puzzle

>>> egg_drop(1, 10)
10
>>> egg_drop(2, 10)
4
>>> egg_drop(3, 14)
4
"""

from functools import cache


@cache
def egg_drop(eggs: int, floors: int) -> int:
    """
    Compute the minimum number of trials needed in the worst case with
    a given number of eggs and floors.

    Args:
        eggs (int): number of eggs
        floors (int): number of floors

    Returns:
        int: minimum number of trials required

    >>> egg_drop(1, 5)
    5
    >>> egg_drop(2, 6)
    3
    >>> egg_drop(3, 14)
    4
    """
    if floors in {0, 1}:
        return floors
    if eggs == 1:
        return floors

    min_trials = float("inf")
    for floor in range(1, floors + 1):
        # If egg breaks -> check below floor
        # If egg doesn't break -> check above floor
        trials = 1 + max(egg_drop(eggs - 1, floor - 1), egg_drop(eggs, floors - floor))
        min_trials = min(min_trials, trials)
    return int(min_trials)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
