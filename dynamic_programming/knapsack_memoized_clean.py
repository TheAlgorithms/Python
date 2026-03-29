from functools import cache


def knapsack_memoized(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Solve 0/1 knapsack using memoization without global state.

    Args:
        weights: list of item weights
        values: list of item values
        capacity: maximum capacity of knapsack

    Returns:
        Maximum achievable value

    >>> knapsack_memoized([1, 3, 4], [10, 20, 30], 4)
    30
    >>> knapsack_memoized([1, 2, 3], [10, 15, 40], 6)
    65
    >>> knapsack_memoized([], [], 5)
    0
    """

    if len(weights) != len(values):
        raise ValueError("weights and values must be of same length")

    n = len(weights)

    @cache
    def dp(i: int, remaining: int) -> int:
        if i == n or remaining == 0:
            return 0

        if weights[i] > remaining:
            return dp(i + 1, remaining)

        return max(
            dp(i + 1, remaining),
            values[i] + dp(i + 1, remaining - weights[i]),
        )

    return dp(0, capacity)
