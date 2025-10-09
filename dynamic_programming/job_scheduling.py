"""
Weighted Job Scheduling Problem
Given jobs with start time, end time, and profit, find the maximum profit
subset of non-overlapping jobs.
"""

from bisect import bisect_right


def job_scheduling(jobs):
    """
    >>> jobs = [(1, 3, 50), (3, 5, 20), (0, 6, 100), (4, 6, 70), (3, 8, 60)]
    >>> job_scheduling(jobs)
    120
    >>> jobs = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]
    >>> job_scheduling(jobs)
    250
    """
    # Sort jobs by end time
    jobs = sorted(jobs, key=lambda x: x[1])
    n = len(jobs)
    # dp[i] stores max profit including jobs[i]
    dp = [0] * n
    dp[0] = jobs[0][2]

    # Store end times separately for binary search
    end_times = [job[1] for job in jobs]

    for i in range(1, n):
        profit_incl = jobs[i][2]
        # Find last non-conflicting job using binary search
        index = bisect_right(end_times, jobs[i][0] - 1) - 1
        if index != -1:
            profit_incl += dp[index]
        dp[i] = max(profit_incl, dp[i - 1])
    return dp[-1]
