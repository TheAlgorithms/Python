"""
Author  : Prince Kumar Prajapati
Date    : October 9, 2025

Weighted Job Scheduling Problem
--------------------------------
Given N jobs where every job has a start time, finish time, and profit,
find the maximum profit subset of jobs such that no two jobs overlap.

Approach:
- Sort all jobs by their finish time.
- For each job, find the last non-conflicting job using binary search.
- Use Dynamic Programming to build up the maximum profit table.

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""


def find_last_non_conflicting(jobs, index):
    """
    Binary search to find the last job that doesn't overlap
    with the current job (at index).
    """
    low, high = 0, index - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[index][0]:
            if mid + 1 < index and jobs[mid + 1][1] <= jobs[index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def weighted_job_scheduling(jobs):
    """
    Function to find the maximum profit from a set of jobs.

    Parameters:
        jobs (list of tuples): Each tuple represents (start_time, end_time, profit)
    Returns:
        int: Maximum profit achievable without overlapping jobs.
    """

    # Step 1: Sort jobs by their finish time
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    dp = [0] * n  # dp[i] will store the max profit up to job i
    dp[0] = jobs[0][2]  # First job profit is the base case

    # Step 2: Iterate through all jobs
    for i in range(1, n):
        # Include current job
        include_profit = jobs[i][2]

        # Find the last non-conflicting job
        j = find_last_non_conflicting(jobs, i)
        if j != -1:
            include_profit += dp[j]

        # Exclude current job (take previous best)
        dp[i] = max(include_profit, dp[i - 1])

    # Step 3: Return the maximum profit at the end
    return dp[-1]


# Example usage / Test case
if __name__ == "__main__":
    # Each job is represented as (start_time, end_time, profit)
    jobs = [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]

    print("Maximum Profit:", weighted_job_scheduling(jobs))
