"""
Recursive and Dynamic Programming implementation of the 0-N Knapsack Problem.

References:
    https://en.wikipedia.org/wiki/Knapsack_problem
"""

from functools import cache


def knapsack(
    capacity: int,
    weights: list[int],
    values: list[int],
    allow_repetition: bool = False,
    method: str = "recursive",
) -> int:
    """
    Compute the maximum total value that can be obtained by placing items
    in a knapsack of given capacity.

    Args:
        capacity (int): Maximum weight capacity of the knapsack.
        weights (list[int]): List of item weights.
        values (list[int]): List of item values corresponding to weights.
        allow_repetition (bool): If True, items can be taken multiple times.
        method (str): "recursive" (default) or "dp" for bottom-up approach.

    Returns:
        int: Maximum achievable value.

    Examples:
        >>> knapsack(50, [10, 20, 30], [60, 100, 120])
        220
        >>> knapsack(50, [10, 20, 30], [60, 100, 120], allow_repetition=True)
        300
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if method not in ("recursive", "dp"):
        raise ValueError("method must be 'recursive' or 'dp'")

    n_items = len(weights)

    if method == "dp":
        return _knapsack_dp(capacity, weights, values, allow_repetition)

    @cache
    def recur(cap: int, idx: int) -> int:
        if idx == 0 or cap == 0:
            return 0
        if weights[idx - 1] > cap:
            return recur(cap, idx - 1)
        include_value = values[idx - 1] + recur(
            cap - weights[idx - 1],
            idx if allow_repetition else idx - 1,
        )
        exclude_value = recur(cap, idx - 1)
        return max(include_value, exclude_value)

    return recur(capacity, n_items)


def _knapsack_dp(
    capacity: int,
    weights: list[int],
    values: list[int],
    allow_repetition: bool,
) -> int:
    """Iterative dynamic programming version of the knapsack problem."""
    n = len(weights)
    dp = [0] * (capacity + 1)

    if allow_repetition:
        # Unbounded knapsack
        for cap in range(1, capacity + 1):
            for i in range(n):
                if weights[i] <= cap:
                    dp[cap] = max(dp[cap], dp[cap - weights[i]] + values[i])
    else:
        # 0-1 knapsack
        for i in range(n):
            for cap in range(capacity, weights[i] - 1, -1):
                dp[cap] = max(dp[cap], dp[cap - weights[i]] + values[i])

    return dp[capacity]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
