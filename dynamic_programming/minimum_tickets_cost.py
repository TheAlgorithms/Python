"""
Author  : Alexander Pantyukhin
Date    : November 1, 2022

Task:
Given a list of days when you need to travel. Each day is integer from 1 to 365.
You are able to use tickets for 1 day, 7 days and 30 days.
Each ticket has a cost.

Find the minimum cost you need to travel every day in the given list of days.

Implementation notes:
implementation Dynamic Programming up bottom approach.

Runtime complexity: O(n)

The implementation was tested on the
leetcode: https://leetcode.com/problems/minimum-cost-for-tickets/


Minimum Cost For Tickets
Dynamic Programming: up -> down.
"""

import functools


def mincost_tickets(days: list[int], costs: list[int]) -> int:
    """
    >>> mincost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
    11

    >>> mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],  [2, 7, 15])
    17

    >>> mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    24

    >>> mincost_tickets([2], [2, 90, 150])
    2

    >>> mincost_tickets([], [2, 90, 150])
    0

    >>> mincost_tickets('hello', [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: The parameter days should be a list of integers

    >>> mincost_tickets([], 'world')
    Traceback (most recent call last):
     ...
    ValueError: The parameter costs should be a list of three integers

    >>> mincost_tickets([0.25, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: The parameter days should be a list of integers

    >>> mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 0.9, 150])
    Traceback (most recent call last):
     ...
    ValueError: The parameter costs should be a list of three integers

    >>> mincost_tickets([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: All days elements should be greater than 0

    >>> mincost_tickets([2, 367], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: All days elements should be less than 366

    >>> mincost_tickets([2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [])
    Traceback (most recent call last):
     ...
    ValueError: The parameter costs should be a list of three integers

    >>> mincost_tickets([], [])
    Traceback (most recent call last):
     ...
    ValueError: The parameter costs should be a list of three integers

    >>> mincost_tickets([2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [1, 2, 3, 4])
    Traceback (most recent call last):
     ...
    ValueError: The parameter costs should be a list of three integers
    """

    # Validation
    if not isinstance(days, list) or not all(isinstance(day, int) for day in days):
        raise ValueError("The parameter days should be a list of integers")

    if len(costs) != 3 or not all(isinstance(cost, int) for cost in costs):
        raise ValueError("The parameter costs should be a list of three integers")

    if len(days) == 0:
        return 0

    if min(days) <= 0:
        raise ValueError("All days elements should be greater than 0")

    if max(days) >= 366:
        raise ValueError("All days elements should be less than 366")

    days_set = set(days)

    @functools.cache
    def dynamic_programming(index: int) -> int:
        if index > 365:
            return 0

        if index not in days_set:
            return dynamic_programming(index + 1)

        return min(
            costs[0] + dynamic_programming(index + 1),
            costs[1] + dynamic_programming(index + 7),
            costs[2] + dynamic_programming(index + 30),
        )

    return dynamic_programming(1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
