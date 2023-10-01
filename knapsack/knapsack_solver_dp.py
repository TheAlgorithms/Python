"""
Optimized Dynamic Programming Solution for the 0-1 Knapsack Problem

This implementation finds the maximum value that can be put in a knapsack of capacity `capacity`,
given a list of item weights and their corresponding values.

Reference: https://en.wikipedia.org/wiki/Knapsack_problem

Usage:
>>> knapsack(50, [10, 20, 30], [60, 100, 120])
220
"""

def knapsack(capacity: int, weights: list[int], values: list[int]) -> int:
    """
    Returns the maximum value that can be put in a knapsack of capacity `capacity`,
    whereby each weight `weights[i]` has a corresponding value `values[i]`.

    :param capacity: The capacity of the knapsack.
    :param weights: A list of weights for items.
    :param values: A list of values corresponding to items.
    :return: The maximum value that can be obtained.
    >>> knapsack(50, [10, 20, 30], [60, 100, 120])
    220
    """
    n = len(values)
    
    # Create a DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # If the current item can fit in the knapsack
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item is too heavy
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

