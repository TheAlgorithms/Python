# Implementation of Weighted Interval Scheduling algorithm
# In this algorithm, we are given a list of jobs with start and end times,
# and each job has a specific weight.
# The goal is to find the maximum weight subset of non-overlapping jobs.
# https://en.wikipedia.org/wiki/Interval_scheduling

from __future__ import annotations


def latest_non_conflict(jobs: list[tuple[int, int, int]], indx: int) -> int:
    """
    This function finds the latest job that does not conflict with
    the current job at index `n`.
    The jobs are given as (start_time, end_time, weight), and the
    jobs should be sorted by end time.
    It returns the index of the latest job that finishes before the
    current job starts.
        Return: The index of the latest non-conflicting job.
    >>> latest_non_conflict([(1, 3, 50), (2, 5, 20), (4, 6, 30)], 2)
    0
    >>> latest_non_conflict([(1, 3, 50), (3, 4, 60), (5, 9, 70)], 2)
    1
    """
    for j in range(indx - 1, -1, -1):
        if jobs[j][1] <= jobs[indx][0]:
            return j
    return -1


def find_max_weight(jobs: list[tuple[int, int, int]]) -> int:
    """
    This function calculates the maximum weight of non-overlapping jobs
    using dynamic programming.
    Each job is represented by a tuple (start_time, end_time, weight).
    The function builds a DP table where each entry `dp[i]` represents
    the maximum weight achievable
    using jobs from index 0 to i.
        Return: The maximum achievable weight without overlapping jobs.
    >>> find_max_weight([(1, 3, 50), (2, 5, 20), (4, 6, 30)])
    80
    >>> find_max_weight([(1, 3, 10), (2, 5, 100), (6, 8, 15)])
    115
    >>> find_max_weight([(1, 3, 20), (3, 5, 30), (6, 19, 60), (2, 100, 200)])
    200
    """
    # Sort jobs based on their end times
    jobs.sort(key=lambda ele: ele[1])

    # Initialize dp array to store the maximum weight up to each job
    length = len(jobs)
    dp = [0] * length
    dp[0] = jobs[0][2]  # The weight of the first job is the initial value

    for i in range(1, length):
        # Include the current job
        include_weight = jobs[i][2]
        latest_job = latest_non_conflict(jobs, i)
        if latest_job != -1:
            include_weight += dp[latest_job]

        # Exclude the current job, and take the maximum of including or
        # excluding
        dp[i] = max(include_weight, dp[i - 1])

    return dp[-1]  # The last entry contains the maximum weight


if __name__ == "__main__":
    # Example list of jobs (start_time, end_time, weight)
    jobs = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]

    # Ensure we have jobs to process
    if len(jobs) == 0:
        print("No jobs available to process")
        raise SystemExit(0)

    # Calculate the maximum weight for non-overlapping jobs
    max_weight = find_max_weight(jobs)

    # Print the result
    print(f"The maximum weight of non-overlapping jobs is {max_weight}")
