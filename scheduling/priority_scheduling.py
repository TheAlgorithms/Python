"""
Priority Scheduling
Please note arrival time, burst, priority
Please use spaces to separate inputs entered.
"""
from __future__ import annotations

import pandas as pd
import doctest

def calculate_waitingtime(
    arrival_time: list[int],
    burst_time: list[int],
    priority: list[int],
    no_of_processes: int
) -> list[int]:
    """
    Calculate the waiting time of each processes
    Return: List of waiting times.
    >>> calculate_waitingtime([1,2,3,4], [3,5,2,4], [3,2,4,1], 4)
    [9, 4, 10, 0]
    >>> calculate_waitingtime([2,0,4], [6,6,8], [2,2,1], 3)
    [12, 8, 0]
    >>> calculate_waitingtime([1,3], [4,2], [2,1], 2)
    [2, 0]
    """
    remaining_time = [0] * no_of_processes
    waiting_time = [0] * no_of_processes
    # Copy the burst time into remaining_time[]
    for i in range(no_of_processes):
        remaining_time[i] = burst_time[i]

    complete = 0
    increment_time = 0
    min_arrival_time = 999999999
    selected = 0
    check = False

    # Process until all processes are completed
    while complete != no_of_processes:
        min_priority = 999999999
        min_arrival_time = 0
        for j in range(no_of_processes):
            if arrival_time[j] <= increment_time:
                if remaining_time[j] > 0:
                    if priority[j] <= min_priority:
                        # If processes have equal priority, then First Come First Served
                        if priority[j] == min_priority:
                            if arrival_time[j] < min_arrival_time:
                                min_arrival_time = arrival_time[j]
                                selected = j
                                check = True
                        else:
                            min_priority = priority[j]
                            min_arrival_time = arrival_time[j]
                            selected = j
                            check = True

        if not check:
            increment_time += 1
            continue

        remaining_time[selected] -= 1

        if remaining_time[selected] == 0:
            complete += 1
            check = False

            # Find finish time of current process
            finish_time = increment_time + 1

            # Calculate waiting time
            finar = finish_time - arrival_time[selected]
            waiting_time[selected] = finar - burst_time[selected]

            if waiting_time[selected] < 0:
                waiting_time[selected] = 0

        # Increment time
        increment_time += 1
    return waiting_time


def calculate_turnaroundtime(
    burst_time: list[int], no_of_processes: int, waiting_time: list[int]
) -> list[int]:
    """
    Calculate the turn around time of each Processes
    Return: list of turn around times.
    >>> calculate_turnaroundtime([3,3,5,1], 4, [0,3,5,0])
    [3, 6, 10, 1]
    >>> calculate_turnaroundtime([3,3], 2, [0,3])
    [3, 6]
    >>> calculate_turnaroundtime([8,10,1], 3, [1,0,3])
    [9, 10, 4]
    """
    turn_around_time = [0] * no_of_processes
    for i in range(no_of_processes):
        turn_around_time[i] = burst_time[i] + waiting_time[i]
    return turn_around_time


def calculate_average_times(
    waiting_time: list[int], turn_around_time: list[int], no_of_processes: int
) -> None:
    """
    This function calculates the average of the waiting & turnaround times
    Prints: Average Waiting time & Average Turn Around Time
    >>> calculate_average_times([0,3,5,0],[3,6,10,1],4)
    Average waiting time = 2.0
    Average turn around time = 5.0
    >>> calculate_average_times([2,3],[3,6],2)
    Average waiting time = 2.5
    Average turn around time = 4.5
    >>> calculate_average_times([10,4,3],[2,7,6],3)
    Average waiting time = 5.666666666666667
    Average turn around time = 5.0
    """
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(no_of_processes):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
    print(f"Average waiting time = {total_waiting_time / no_of_processes}")
    print(f"Average turn around time = {total_turn_around_time / no_of_processes}")


if __name__ == "__main__":
    print("Enter how many process you want to analyze")
    no_of_processes = int(input())
    burst_time = [0] * no_of_processes
    arrival_time = [0] * no_of_processes
    priority = [0] * no_of_processes
    processes = list(range(1, no_of_processes + 1))

    for i in range(no_of_processes):
        print(
            f"Enter the arrival time and burst time and priority for process:--{str(i + 1)}"
        )
        arrival_time[i], burst_time[i], priority[i] = map(int, input().split())

    waiting_time = calculate_waitingtime(
        arrival_time, burst_time, priority, no_of_processes
    )

    bt = burst_time
    n = no_of_processes
    wt = waiting_time
    turn_around_time = calculate_turnaroundtime(bt, n, wt)

    calculate_average_times(waiting_time, turn_around_time, no_of_processes)

    fcfs = pd.DataFrame(
        list(
            zip(
                processes,
                burst_time,
                arrival_time,
                priority,
                waiting_time,
                turn_around_time
            )
        ),
        columns=[
            "Process",
            "BurstTime",
            "ArrivalTime",
            "Priority",
            "WaitingTime",
            "TurnAroundTime",
        ],
    )

    # Printing the dataFrame
    pd.set_option("display.max_rows", fcfs.shape[0] + 1)
    print(fcfs)
    doctest.testmod()
