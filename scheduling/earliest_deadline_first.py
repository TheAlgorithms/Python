"""
Earliest Deadline First (EDF) scheduling algorithm
In EDF, the process with the earliest deadline is selected for execution.
https://en.wikipedia.org/wiki/Earliest_deadline_first_scheduling
Author: KelvinPuyam
"""

from __future__ import annotations


def calculate_waiting_times(
    arrival_times: list[int], burst_times: list[int], deadlines: list[int]
) -> list[int]:
    """
    Calculate the waiting times of processes using EDF algorithm.
    Return: List of waiting times for each process.
    """
    n = len(arrival_times)
    waiting_times = [0] * n
    remaining_times = burst_times.copy()

    current_time = 0
    process_executed = 0
    while process_executed < n:
        min_deadline = float("inf")
        selected_process = -1
        for i in range(n):
            if (
                arrival_times[i] <= current_time
                and remaining_times[i] > 0
                and deadlines[i] < min_deadline
            ):
                min_deadline = deadlines[i]
                selected_process = i

        if selected_process == -1:
            current_time += 1
            continue

        waiting_times[selected_process] = current_time - arrival_times[selected_process]
        current_time += burst_times[selected_process]
        remaining_times[selected_process] = 0
        process_executed += 1

    return waiting_times


def calculate_turnaround_times(
    burst_times: list[int], waiting_times: list[int]
) -> list[int]:
    """
    Calculate the turnaround times of processes.
    Return: List of turnaround times for each process.
    """
    return [burst_times[i] + waiting_times[i] for i in range(len(burst_times))]


def calculate_average_turnaround_time(turnaround_times: list[int]) -> float:
    """
    Calculate the average turnaround time.
    Return: The average turnaround time.
    """
    return sum(turnaround_times) / len(turnaround_times)


def calculate_average_waiting_time(waiting_times: list[int]) -> float:
    """
    Calculate the average waiting time.
    Return: The average waiting time.
    """
    return sum(waiting_times) / len(waiting_times)


if __name__ == "__main__":
    arrival_times = [0, 1, 2]
    burst_times = [3, 5, 2]
    deadlines = [5, 7, 6]

    waiting_times = calculate_waiting_times(arrival_times, burst_times, deadlines)
    turnaround_times = calculate_turnaround_times(burst_times, waiting_times)

    average_waiting_time = calculate_average_waiting_time(waiting_times)
    average_turnaround_time = calculate_average_turnaround_time(turnaround_times)

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(arrival_times)):
        print(f"{i+1}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

    print(f"Average waiting time: {average_waiting_time}")
    print(f"Average turnaround time: {average_turnaround_time}")
