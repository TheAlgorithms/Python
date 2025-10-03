"""
Shortest Remaining Time First (SRTF) scheduling is a preemptive version of Shortest Job First (SJF).
At every unit of time, it selects the process with the smallest remaining burst time
among the processes that have arrived.
https://en.wikipedia.org/wiki/Shortest_job_next#Preemptive_SJF_(SRTF)
"""

from statistics import mean
from typing import List


def calculate_srtf_waiting_time(arrival: List[int], burst: List[int]) -> List[int]:
    """
    Calculate waiting time for each process using Shortest Remaining Time First (SRTF).

    Args:
        arrival: List of arrival times of processes.
        burst: List of burst times of processes.

    Returns:
        List of waiting times for each process.

    >>> calculate_srtf_waiting_time([0, 1, 2, 3], [8, 4, 9, 5])
    [9, 0, 15, 2]
    """
    n = len(arrival)
    remaining = burst.copy()
    waiting = [0] * n
    completed = 0
    t = 0
    last_executed = -1
    completion_time = [0] * n

    while completed < n:
        # Find process with smallest remaining time that has arrived
        idx = -1
        min_remaining = float("inf")
        for i in range(n):
            if arrival[i] <= t and remaining[i] > 0 and remaining[i] < min_remaining:
                min_remaining = remaining[i]
                idx = i

        if idx == -1:
            t += 1  # No process ready, advance time
            continue

        # Execute process for 1 unit of time
        remaining[idx] -= 1
        t += 1

        # If process finished, record completion and calculate waiting
        if remaining[idx] == 0:
            completed += 1
            completion_time[idx] = t
            waiting[idx] = completion_time[idx] - arrival[idx] - burst[idx]

    return waiting


def calculate_srtf_turnaround_time(
    arrival: List[int], burst: List[int], waiting: List[int]
) -> List[int]:
    """
    Calculate turnaround time for each process using waiting time.

    Args:
        arrival: List of arrival times.
        burst: List of burst times.
        waiting: List of waiting times.

    Returns:
        List of turnaround times.

    >>> calculate_srtf_turnaround_time([0,1,2,3],[8,4,9,5],[6,0,12,0])
    [14, 4, 21, 5]
    """
    return [burst[i] + waiting[i] for i in range(len(burst))]


if __name__ == "__main__":
    arrival_time = [0, 1, 2, 3]
    burst_time = [8, 4, 9, 5]

    waiting_time = calculate_srtf_waiting_time(arrival_time, burst_time)
    turnaround_time = calculate_srtf_turnaround_time(
        arrival_time, burst_time, waiting_time
    )

    print("PID\tArrival\tBurst\tWaiting\tTurnaround")
    for i in range(len(arrival_time)):
        print(
            f"P{i + 1}\t{arrival_time[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}"
        )

    print(f"Average Waiting Time: {mean(waiting_time):.2f}")
    print(f"Average Turnaround Time: {mean(turnaround_time):.2f}")
