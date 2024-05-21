def knapsack_dp(capacity: int, weights: list[int], values: list[int]) -> int:
    """
    Returns the maximum value that can be put in a knapsack of a given capacity,
    with each weight having a specific value.

    Uses a dynamic programming approach to solve the 0/1 Knapsack Problem.

    >>> capacity = 50
    >>> values = [60, 100, 120]
    >>> weights = [10, 20, 30]
    >>> knapsack_dp(capacity, weights, values)
    220

    >>> capacity = 0
    >>> values = [60, 100, 120]
    >>> weights = [10, 20, 30]
    >>> knapsack_dp(capacity, weights, values)
    0

    >>> capacity = 10
    >>> values = [10, 10, 10]
    >>> weights = [5, 5, 5]
    >>> knapsack_dp(capacity, weights, values)
    20

    >>> capacity = 100
    >>> values = [60, 100, 120, 80, 30]
    >>> weights = [10, 20, 30, 40, 50]
    >>> knapsack_dp(capacity, weights, values)
    360

    >>> capacity = 7
    >>> values = [1, 4, 5, 7]
    >>> weights = [1, 3, 4, 5]
    >>> knapsack_dp(capacity, weights, values)
    9
    """

    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                value_included = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                value_excluded = dp[i - 1][w]
                dp[i][w] = max(value_included, value_excluded)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    import doctest

    doctest.testmod()