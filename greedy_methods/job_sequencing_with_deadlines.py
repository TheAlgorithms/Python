# Job Sequencing Problem with Deadlines
# Each job has a deadline and a profit associated with it.
# Jobs need to be executed within their respective deadlines to maximize the total profit.


def job_sequence_with_deadlines(jobs):
    # Sort jobs based on their profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    max_deadline = max(jobs, key=lambda x: x[1])[
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

    return [job for job in result if job != -1]  # Return the sequence of selected jobs


# Example usage
if __name__ == "__main__":
    # Each job represented as (job_id, deadline, profit)
    jobs = [(1, 4, 70), (2, 1, 80), (3, 1, 30), (4, 1, 100), (5, 3, 60)]

    selected_jobs = job_sequence_with_deadlines(jobs)
    print("Job sequence with deadlines:", selected_jobs)
