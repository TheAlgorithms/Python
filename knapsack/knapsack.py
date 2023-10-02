""" A naive recursive implementation of 0-1 Knapsack Problem
    https://en.wikipedia.org/wiki/Knapsack_problem
"""
from __future__ import annotations


def knapsack(capacity, weights, values, permit_repetition=False):
    """
    #Parameters:
    #capacity - max item weight knapsack can hold
    #weights - list of item weights
    #values -list of item values
    #permit_repetition - boolean restricting repetitve selection of items

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> knapsack(cap, w, val, permit_repetition=False)
    220

    >>> knapsack(cap, w, val, permit_repetition=True)
    300
    """
    # assign length of weights to variable n
    n = len(weights)
    # create 2d list called dp
    # each row represents a subproblem
    # dp size is (n + 1) rows and (capacity + 1) columns
    # initialize each element of dp to 0
    # use a loop to generate 'n + 1' rows, one for each item plus an extra row for the base case
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Two nested loops iterate over each item (i) and each capacity (w)
    # For each subproblem (i, w), check:
    # 1) If i == 0 (no items selected) or w == 0 (no capacity), set dp[i][w] to 0 (base case).
    # 2) If the weight of the current item (weights[i - 1]) <= to w, calculate maximum value based on:
    #    i. If item been picked up 1 or 1+ times = permit_repetition = True
    #   ii. If item picked up only 1 time = permit_repetition = False
    # 3) If the weight of the current item > the current capacity, set dp[i][w] to the value without including the current item.
    # 4) The final result is stored in dp[n][capacity], which represents the maximum value with all items in given capacity
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                if permit_repetition:
                    dp[i][w] = max(
                        dp[i - 1][w], dp[i][w - weights[i - 1]] + values[i - 1]
                    )
                else:
                    dp[i][w] = max(
                        dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                    )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
