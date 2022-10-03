""" A simple implementation of Unbounded Knapsack Problem
    https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
"""
from __future__ import annotations


def unbounded_knapsack(
    capacity: int, weights: list[int], values: list[int], counter: int
) -> int:
    """
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val and a item can be repeated.

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> unbounded_knapsack(cap, w, val, c)
    300

    The result is 300 cause the value of 60 can be used 5 times as it has weight 10
    and limit is 50.
    """

    # Base Case
    if counter == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity,
    #   then this item cannot be included in the optimal solution,
    # else return the maximum of two cases:
    #   (1) nth item included
    #   (2) not included
    if weights[counter - 1] > capacity:
        return unbounded_knapsack(capacity, weights, values, counter - 1)
    else:
        left_capacity = capacity - weights[counter - 1]
        new_value_included = values[counter - 1] + unbounded_knapsack(
            left_capacity, weights, values, counter
        )
        without_new_value = unbounded_knapsack(capacity, weights, values, counter - 1)
        return max(new_value_included, without_new_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
