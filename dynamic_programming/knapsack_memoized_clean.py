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
    >>> knapsack_memoized([2, 3, 4], [4, 5, 6], 0)
    0
    """

    if len(weights) != len(values):
        raise ValueError("weights and values must be of same length")

    n = len(weights)

    @cache
    def dp(index: int, remaining: int) -> int:
        """
        Recursive helper function for knapsack memoization.

        Args:
            index: current item index
            remaining: remaining capacity of knapsack

        Returns:
            Maximum value achievable from current state

        Note:
            This function is internally tested via knapsack_memoized doctests.
        """
        if index == n or remaining == 0:
            return 0

        if weights[index] > remaining:
            return dp(index + 1, remaining)

        return max(
            dp(index + 1, remaining),
            values[index] + dp(index + 1, remaining - weights[index]),
        )

    return dp(0, capacity)
