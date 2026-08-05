"""
Author  : Abhiraj Mandal
Date    : October 3, 2025

Weighted Interval Scheduling (Dynamic Programming) implementation in Python.

Problem:
Given a set of intervals with start time, end time, and weight,
find a subset of non-overlapping intervals with the maximum total weight.
"""

from __future__ import annotations

from typing import NamedTuple


class Interval(NamedTuple):
    start: int
    end: int
    weight: int


def weighted_interval_scheduling(intervals: list[Interval]) -> int:
    """
    Compute the maximum total weight of non-overlapping intervals.

    >>> intervals = [Interval(1, 3, 5), Interval(2, 5, 6), Interval(4, 6, 5)]
    >>> weighted_interval_scheduling(intervals)
    10
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x.end)

    p = [0] * len(intervals)
    for j in range(len(intervals)):
        p[j] = -1
        for i in range(j - 1, -1, -1):
            if intervals[i].end <= intervals[j].start:
                p[j] = i
                break

    n = len(intervals)
    dp = [0] * n
    for j in range(n):
        incl = intervals[j].weight
        if p[j] != -1:
            incl += dp[p[j]]
        dp[j] = max(incl, dp[j - 1] if j > 0 else 0)

    return dp[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All doctests passed!")

    # Manual test suite
    test_cases = [
        ([Interval(1, 3, 5), Interval(2, 5, 6), Interval(4, 6, 5)], 10),
        ([Interval(1, 2, 50)], 50),
        ([Interval(1, 4, 5), Interval(2, 5, 6), Interval(3, 6, 5)], 6),
        ([Interval(1, 2, 10), Interval(3, 4, 20), Interval(5, 6, 30)], 60),
        (
            [
                Interval(1, 2, 50),
                Interval(3, 5, 20),
                Interval(6, 19, 100),
                Interval(2, 100, 200),
            ],
            250,
        ),
    ]

    for idx, (intervals, expected) in enumerate(test_cases, 1):
        result = weighted_interval_scheduling(intervals)
        print(f"Testcase {idx}: Expected={expected}, Got={result}")
        assert result == expected, f"Testcase {idx} failed!"

    print("\nAll manual test cases successfully passed!")
