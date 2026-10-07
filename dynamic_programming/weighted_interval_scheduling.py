"""
Weighted Interval Scheduling Problem (Dynamic Programming with Binary Search).

Given a set of intervals (tasks/activities), each characterized by a start time,
an end time, and an associated weight (value/profit), the goal is to select a subset
of mutually compatible (non-overlapping) intervals that maximizes the total weight.

Unlike the unweighted interval scheduling (activity selection) problem which can be
optimally solved using a greedy strategy (earliest finish time first), the weighted
variant requires dynamic programming because higher-value intervals might conflict
with earlier-finishing intervals.

Algorithm:
1. Sort intervals by their finish times in non-decreasing order.
2. For each interval j, compute p(j), the index of the latest compatible interval
   that finishes at or before the start time of interval j. This can be found in
   O(log n) time using binary search (bisect_right).
3. Compute the maximum weight subset using the recurrence:
   OPT(j) = max(OPT(j - 1), weight(j) + OPT(p(j)))
4. Backtrack through the DP array to reconstruct the optimal set of intervals.

Complexity:
- Time Complexity: O(n log n) due to sorting and n binary searches.
- Space Complexity: O(n) for the DP table and output list.

Reference:
- Kleinberg, J., & Tardos, É. (2006). Algorithm Design. Chapter 6.1:
  Weighted Interval Scheduling. Addison-Wesley.
- https://en.wikipedia.org/wiki/Interval_scheduling#Weighted_interval_scheduling
"""

from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass


@dataclass(frozen=True)
class Interval:
    """
    Represents a task or activity with start time, end time, and weight.

    Attributes:
        start: Start time of the interval.
        end: End time of the interval (must be strictly greater than start).
        weight: Value, priority, or profit of the interval (must be non-negative).
    """

    start: float
    end: float
    weight: float

    def __post_init__(self) -> None:
        if self.start >= self.end:
            msg = (
                f"Start time ({self.start}) must be strictly less than "
                f"end time ({self.end})."
            )
            raise ValueError(msg)
        if self.weight < 0:
            msg = f"Weight ({self.weight}) must be non-negative."
            raise ValueError(msg)


def weighted_interval_scheduling(
    intervals: list[Interval],
) -> tuple[float, list[Interval]]:
    """
    Finds the subset of compatible intervals yielding maximum total weight.

    Args:
        intervals: A list of Interval objects.

    Returns:
        A tuple (max_weight, selected_intervals) where:
        - max_weight is the maximum sum of weights achievable.
        - selected_intervals is the list of non-overlapping Interval objects selected.

    Examples:
        >>> intervals = [
        ...     Interval(0, 3, 3),
        ...     Interval(1, 5, 4),
        ...     Interval(4, 6, 2),
        ...     Interval(6, 8, 5),
        ... ]
        >>> max_weight, selected = weighted_interval_scheduling(intervals)
        >>> max_weight
        10.0
        >>> [(i.start, i.end, i.weight) for i in selected]
        [(0, 3, 3), (4, 6, 2), (6, 8, 5)]

        >>> # Classic case where greedy choice fails:
        >>> intervals = [
        ...     Interval(1, 4, 10),
        ...     Interval(3, 6, 12),
        ...     Interval(5, 8, 10),
        ... ]
        >>> max_weight, selected = weighted_interval_scheduling(intervals)
        >>> max_weight
        20.0
        >>> [(i.start, i.end, i.weight) for i in selected]
        [(1, 4, 10), (5, 8, 10)]

        >>> # Empty input
        >>> weighted_interval_scheduling([])
        (0.0, [])

        >>> # Single interval
        >>> max_weight, selected = weighted_interval_scheduling([Interval(2, 5, 7.5)])
        >>> max_weight
        7.5
        >>> [(i.start, i.end, i.weight) for i in selected]
        [(2, 5, 7.5)]

        >>> # Completely overlapping intervals: picks the highest weight
        >>> overlapping = [
        ...     Interval(1, 10, 5),
        ...     Interval(2, 9, 15),
        ...     Interval(3, 8, 8),
        ... ]
        >>> max_weight, selected = weighted_interval_scheduling(overlapping)
        >>> max_weight
        15.0
        >>> [(i.start, i.end, i.weight) for i in selected]
        [(2, 9, 15)]

        >>> # Invalid intervals raise ValueError
        >>> Interval(5, 2, 10)
        Traceback (most recent call last):
            ...
        ValueError: Start time (5) must be strictly less than end time (2).

        >>> Interval(1, 5, -3)
        Traceback (most recent call last):
            ...
        ValueError: Weight (-3) must be non-negative.
    """
    if not intervals:
        return 0.0, []

    # Sort intervals by finish times in non-decreasing order
    sorted_intervals = sorted(intervals, key=lambda item: item.end)
    n = len(sorted_intervals)

    # Extract finish times for binary search
    end_times = [item.end for item in sorted_intervals]

    # predecessors[j] stores count of compatible intervals ending <= start of j
    predecessors: list[int] = [0] * n
    for j in range(n):
        idx = bisect_right(end_times, sorted_intervals[j].start)
        predecessors[j] = idx

    # dp[j] stores max weight using a subset of the first j sorted intervals
    dp: list[float] = [0.0] * (n + 1)
    for j in range(1, n + 1):
        incl_weight = sorted_intervals[j - 1].weight + dp[predecessors[j - 1]]
        excl_weight = dp[j - 1]
        dp[j] = max(incl_weight, excl_weight)

    # Backtracking to reconstruct the optimal set of intervals
    selected: list[Interval] = []
    curr = n
    while curr > 0:
        incl_weight = sorted_intervals[curr - 1].weight + dp[predecessors[curr - 1]]
        if incl_weight > dp[curr - 1]:
            selected.append(sorted_intervals[curr - 1])
            curr = predecessors[curr - 1]
        else:
            curr -= 1

    selected.reverse()
    return dp[n], selected


if __name__ == "__main__":
    import doctest

    doctest.testmod()
