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

Reference: https://en.wikipedia.org/wiki/Interval_scheduling#Weighted_interval_scheduling
"""


def find_last_non_conflicting_job(
    jobs: list[tuple[int, int, int]], current_job_index: int
) -> int:
    """
    Binary search to find the last job that doesn't overlap with the current job.

    Args:
        jobs: List of jobs sorted by finish time, each job is
            (start_time, end_time, profit)
        current_job_index: Index of the current job for which we need to find
            non-conflicting jobs    Returns:
        Index of the last non-conflicting job, or -1 if no such job exists

    Examples:
        >>> jobs = [(1, 3, 50), (2, 4, 10), (3, 5, 40)]
        >>> find_last_non_conflicting_job(jobs, 2)
        0
        >>> find_last_non_conflicting_job(jobs, 1)
        -1
    """
    low, high = 0, current_job_index - 1
    last_non_conflicting_index = -1

    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[current_job_index][0]:
            last_non_conflicting_index = mid
            low = mid + 1
        else:
            high = mid - 1

    return last_non_conflicting_index


def weighted_job_scheduling_with_maximum_profit(
    jobs: list[tuple[int, int, int]],
) -> int:
    """
    Find the maximum profit from a set of jobs without overlapping intervals.

    Args:
        jobs: List of tuples where each tuple represents (start_time, end_time, profit)

    Returns:
        Maximum profit achievable without overlapping jobs

    Raises:
        ValueError: If jobs list is empty or contains invalid job data

    Examples:
        >>> jobs1 = [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]
        >>> weighted_job_scheduling_with_maximum_profit(jobs1)
        120
        >>> jobs2 = [(1, 2, 10), (2, 3, 20), (3, 4, 30)]
        >>> weighted_job_scheduling_with_maximum_profit(jobs2)
        60
        >>> weighted_job_scheduling_with_maximum_profit([(1, 4, 100), (2, 3, 50)])
        100
        >>> weighted_job_scheduling_with_maximum_profit([])
        0
        >>> weighted_job_scheduling_with_maximum_profit([(1, 1, 10)])
        Traceback (most recent call last):
        ...
        ValueError: Invalid job: start time must be less than end time
    """
    if not jobs:
        return 0

    # Validate job data
    for start_time, end_time, profit in jobs:
        if (
            not isinstance(start_time, int)
            or not isinstance(end_time, int)
            or not isinstance(profit, int)
        ):
            raise ValueError("Job times and profit must be integers")
        if start_time >= end_time:
            raise ValueError("Invalid job: start time must be less than end time")
        if profit < 0:
            raise ValueError("Job profit cannot be negative")

    # Sort jobs by their finish time
    sorted_jobs_by_finish_time = sorted(jobs, key=lambda job: job[1])
    number_of_jobs = len(sorted_jobs_by_finish_time)

    # Dynamic programming array to store maximum profit up to each job
    maximum_profit_up_to_job = [0] * number_of_jobs
    maximum_profit_up_to_job[0] = sorted_jobs_by_finish_time[0][2]

    # Fill the DP array
    for current_job_index in range(1, number_of_jobs):
        # Profit including current job
        current_job_profit = sorted_jobs_by_finish_time[current_job_index][2]

        # Find the last non-conflicting job
        last_non_conflicting_index = find_last_non_conflicting_job(
            sorted_jobs_by_finish_time, current_job_index
        )

        profit_including_current_job = current_job_profit
        if last_non_conflicting_index != -1:
            profit_including_current_job += maximum_profit_up_to_job[
                last_non_conflicting_index
            ]

        # Maximum profit is either including current job or excluding it
        maximum_profit_up_to_job[current_job_index] = max(
            profit_including_current_job,
            maximum_profit_up_to_job[current_job_index - 1],
        )

    return maximum_profit_up_to_job[number_of_jobs - 1]


def demonstrate_weighted_job_scheduling_algorithm() -> None:
    """
    Demonstrate the weighted job scheduling algorithm with example test cases.

    Examples:
        >>> demonstrate_weighted_job_scheduling_algorithm()  # doctest: +ELLIPSIS
        Weighted Job Scheduling Algorithm Demonstration
        ...
        Maximum Profit: 120
    """
    print("Weighted Job Scheduling Algorithm Demonstration")
    print("=" * 50)

    # Example jobs: (start_time, end_time, profit)
    example_jobs = [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]

    print(f"Input Jobs: {example_jobs}")
    maximum_profit = weighted_job_scheduling_with_maximum_profit(example_jobs)
    print(f"Maximum Profit: {maximum_profit}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    demonstrate_weighted_job_scheduling_algorithm()
