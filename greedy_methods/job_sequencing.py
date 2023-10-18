from typing import List, Tuple


def job_sequence_with_deadlines(jobs: List[Tuple[int, int, int]]) -> List[int]:
    """
    Solve the Job Sequencing Problem with Deadlines.

    Args:
        jobs (List[Tuple[int, int, int]]): A list of jobs represented as tuples (job_id, deadline, profit).

    Returns:
        List[int]: A list containing the sequence of selected jobs' IDs.
    """
    # Sort jobs based on their profits in descending order
    jobs.sort(key=lambda job: job[2], reverse=True)

    n = len(jobs)
    max_deadline = max(jobs, key=lambda job: job[1])[
        1
    ]  # Find the maximum deadline among all jobs

    # Initialize result list and time slots
    result = [-1] * max_deadline  # Result array to store job sequence
    slots = [False] * max_deadline  # Array to track time slots

    # Iterate through sorted jobs and fill the result list
    for i in range(n):
        deadline = jobs[i][1]  # Deadline of the current job
        # Find a time slot before the deadline
        while deadline > 0 and slots[deadline - 1]:
            deadline -= 1
        # If a time slot is available, assign the job to that slot
        if deadline > 0:
            result[deadline - 1] = jobs[i][0]  # Assign job index to the result list
            slots[deadline - 1] = True  # Mark the slot as occupied

    return [
        job_id for job_id in result if job_id != -1
    ]  # Return the sequence of selected jobs
