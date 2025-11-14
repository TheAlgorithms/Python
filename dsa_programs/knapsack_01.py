"""0/1 knapsack using dynamic programming."""

from typing import Iterable, List, Sequence, Tuple

Item = Tuple[int, int]  # (weight, value)


def knapsack_01(items: Sequence[Item], capacity: int) -> int:
    if capacity < 0:
        raise ValueError("Capacity must be non-negative")
    dp: List[int] = [0] * (capacity + 1)
    for weight, value in items:
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity], dp[current_capacity - weight] + value
            )
    return dp[capacity]
