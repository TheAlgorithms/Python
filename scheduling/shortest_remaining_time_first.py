"""
Shortest Remaining Time First (SRTF) Scheduling Algorithm.
SRTF is the preemptive version of Shortest Job First (SJF).
At every moment, the process with the smallest remaining burst time is executed.
https://en.wikipedia.org/wiki/Shortest_remaining_time
"""

from __future__ import annotations
from statistics import mean


def calculate_waiting_times(
    burst_times: list[int], arrival_times: list[int]
) -> list[int]:
    """
    Calculate the waiting times of processes using SRTF scheduling.

    Args:
        burst_times: List of burst times for each process.
        arrival_times: List of arrival times for each process.

    Returns:
        A list containing waiting time for each process.

    Examples:
    >>> calculate_waiting_times([6, 8, 7, 3], [0, 1, 2, 3])
    [9, 15, 10, 0]
    >>> calculate_waiting_times([5, 4, 2, 1], [0, 1, 2, 3])
    [6, 3, 1, 0]
    """
    n = len(burst_times)
    remaining_times = burst_times.copy()
    waiting_times = [0] * n
    complete = 0
    t = 0
    min_remaining = float("inf")
    shortest = 0
    check = False
    finish_time = 0

    while complete != n:
        # Find process with minimum remaining time at current time
        for j in range(n):
            if (
                arrival_times[j] <= t
                and remaining_times[j] < min_remaining
                and remaining_times[j] > 0
            ):
                min_remaining = remaining_times[j]
                shortest = j
                check = True

        if not check:
            t += 1
            continue

        # Reduce remaining time of current process
        remaining_times[shortest] -= 1
        min_remaining = remaining_times[shortest]
        if min_remaining == 0:
            min_remaining = float("inf")

        # If a process finishes
        if remaining_times[shortest] == 0:
            complete += 1
            check = False
            finish_time = t + 1
            waiting_times[shortest] = (
                finish_time - burst_times[shortest] - arrival_times[shortest]
            )
            if waiting_times[shortest] < 0:
                waiting_times[shortest] = 0

        t += 1

    return waiting_times


def calculate_turn_around_times(
    burst_times: list[int], waiting_times: list[int]
) -> list[int]:
    """
    Calculate turn-around times for each process.

    >>> calculate_turn_around_times([6, 8, 7, 3], [9, 15, 10, 0])
    [15, 23, 17, 3]
    """
    return [burst + waiting for burst, waiting in zip(burst_times, waiting_times)]


if __name__ == "__main__":
    burst_times = [6, 8, 7, 3]
    arrival_times = [0, 1, 2, 3]
    waiting_times = calculate_waiting_times(burst_times, arrival_times)
    turn_around_times = calculate_turn_around_times(burst_times, waiting_times)

    print("Process ID \tArrival Time \tBurst Time \tWaiting Time \tTurnaround Time")
    for i, burst_time in enumerate(burst_times):
        print(
            f"  {i + 1}\t\t  {arrival_times[i]}\t\t  {burst_time}\t\t  {waiting_times[i]}\t\t  {turn_around_times[i]}"
        )
    print(f"\nAverage waiting time = {mean(waiting_times):.5f}")
    print(f"Average turn around time = {mean(turn_around_times):.5f}")
