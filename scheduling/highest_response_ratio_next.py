"""
Highest response ratio next (HRRN) scheduling is a non-preemptive discipline.
It was developed as modification of shortest job next or shortest job first (SJN or SJF)
to mitigate the problem of process starvation.
https://en.wikipedia.org/wiki/Highest_response_ratio_next
"""

from statistics import mean

import numpy as np


def calculate_turn_around_time(
    process_name: list, arrival_time: list, burst_time: list, no_of_process: int
) -> list:
    """
    Calculate the turn around time of each processes

    Return: The turn around time time for each process.
    >>> calculate_turn_around_time(["A", "B", "C"], [3, 5, 8], [2, 4, 6], 3)
    [2, 4, 7]
    >>> calculate_turn_around_time(["A", "B", "C"], [0, 2, 4], [3, 5, 7], 3)
    [3, 6, 11]
    """

    current_time = 0
    # Number of processes finished
    finished_process_count = 0
    # Displays the finished process.
    # If it is 0, the performance is completed if it is 1, before the performance.
    finished_process = [0] * no_of_process
    # List to include calculation results
    turn_around_time = [0] * no_of_process

    # Sort by arrival time.
    burst_time = [burst_time[i] for i in np.argsort(arrival_time)]
    process_name = [process_name[i] for i in np.argsort(arrival_time)]
    arrival_time.sort()

    while no_of_process > finished_process_count:
        """
        If the current time is less than the arrival time of
        the process that arrives first among the processes that have not been performed,
        change the current time.
        """
        i = 0
        while finished_process[i] == 1:
            i += 1
        if current_time < arrival_time[i]:
            current_time = arrival_time[i]

        response_ratio = 0
        # Index showing the location of the process being performed
        loc = 0
        # Saves the current response ratio.
        temp = 0
        for i in range(no_of_process):
            if finished_process[i] == 0 and arrival_time[i] <= current_time:
                temp = (burst_time[i] + (current_time - arrival_time[i])) / burst_time[
                    i
                ]
            if response_ratio < temp:
                response_ratio = temp
                loc = i

        # Calculate the turn around time
        turn_around_time[loc] = current_time + burst_time[loc] - arrival_time[loc]
        current_time += burst_time[loc]
        # Indicates that the process has been performed.
        finished_process[loc] = 1
        # Increase finished_process_count by 1
        finished_process_count += 1

    return turn_around_time


def calculate_waiting_time(
    process_name: list,  # noqa: ARG001
    turn_around_time: list,
    burst_time: list,
    no_of_process: int,
) -> list:
    """
    Calculate the waiting time of each processes.

    Return: The waiting time for each process.
    >>> calculate_waiting_time(["A", "B", "C"], [2, 4, 7], [2, 4, 6], 3)
    [0, 0, 1]
    >>> calculate_waiting_time(["A", "B", "C"], [3, 6, 11], [3, 5, 7], 3)
    [0, 1, 4]
    """

    waiting_time = [0] * no_of_process
    for i in range(no_of_process):
        waiting_time[i] = turn_around_time[i] - burst_time[i]
    return waiting_time


if __name__ == "__main__":
    no_of_process = 5
    process_name = ["A", "B", "C", "D", "E"]
    arrival_time = [1, 2, 3, 4, 5]
    burst_time = [1, 2, 3, 4, 5]

    turn_around_time = calculate_turn_around_time(
        process_name, arrival_time, burst_time, no_of_process
    )
    waiting_time = calculate_waiting_time(
        process_name, turn_around_time, burst_time, no_of_process
    )

    print("Process name \tArrival time \tBurst time \tTurn around time \tWaiting time")
    for i in range(no_of_process):
        print(
            f"{process_name[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t"
            f"{turn_around_time[i]}\t\t\t{waiting_time[i]}"
        )

    print(f"average waiting time : {mean(waiting_time):.5f}")
    print(f"average turn around time : {mean(turn_around_time):.5f}")
