from typing import List

""" A naive recursive implementation of 0-1 Knapsack Problem
    https://en.wikipedia.org/wiki/Knapsack_problem
"""


def knapsack(capacity: int, weights: List[int], values: List[int], counter: int) -> int:
    """
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val.

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack(cap, w, val, c)
    220

    The result is 220 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
    """

    # Base Case
    if counter == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity,
    #   then this item cannot be included in the optimal solution,
    # else return the maximum of two cases:
    #   (1) nth item excluded
    #   (2) nth item included
    
    if weights[counter] > capacity:
        return knapsack(capacity, weights, values, counter - 1)
    
    return max(
        knapsack(capacity               , weights, values, counter - 1),
        knapsack(size - weights[counter], weights, values, counter - 1) + values[counter]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
