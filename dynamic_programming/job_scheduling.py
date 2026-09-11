"""
Weighted Job Scheduling Problem
Given jobs with start time, end time, and profit, find the maximum profit
subset of non-overlapping jobs.
https://en.wikipedia.org/wiki/Weighted_interval_scheduling
"""

from bisect import bisect_right


def job_scheduling(jobs: list[tuple[int, int, int]]) -> int:
    """
    >>> jobs = [(1, 3, 50), (3, 5, 20), (0, 6, 100), (4, 6, 70), (3, 8, 60)]
    >>> job_scheduling(jobs)
    120
    >>> jobs = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]
    >>> job_scheduling(jobs)
    250
    """
    if not jobs:
        return 0

    jobs.sort(key=lambda job: job[1])
    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]
    end_times = [job[1] for job in jobs]

    for i in range(1, n):
        profit_incl = jobs[i][2]
        index = bisect_right(end_times, jobs[i][0]) - 1  # allow adjacent jobs
        if index != -1:
            profit_incl += dp[index]
        dp[i] = max(profit_incl, dp[i - 1])

    return dp[-1]
