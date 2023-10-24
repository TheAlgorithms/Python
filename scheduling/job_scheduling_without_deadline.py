def job_scheduling_without_deadline(num_jobs: int, jobs: list) -> list:
    """
    Function to find the maximum profit by doing jobs without any deadline

    Args:
        num_jobs [int]: Number of jobs
        jobs [list]: A list of tuples of (job_id, profit)

    Returns:
        max_profit [int]: Maximum profit that can be earned by doing jobs
        without any deadline

    Examples:
    >>> job_scheduling_without_deadline(4, [(1, 20), (2, 10), (3, 40), (4, 30)])
    [3, 80]
    >>> job_scheduling_without_deadline(5, [(1, 100), (2, 19), (3, 27), (4, 25), (5, 15)])
    [5, 186]
    """

    # Sort the jobs in descending order of profit
    jobs = sorted(jobs, key=lambda value: value[1], reverse=True)

    # Finding the maximum profit and the count of jobs
    count = 0
    max_profit = 0
    for job in jobs:
        count += 1
        max_profit += job[1]

    return [count, max_profit]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
