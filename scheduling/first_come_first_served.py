# Implementation of First Come First Served scheduling algorithm
# In this Algorithm we just care about the order that the processes arrived
# without carring about their duration time
# https://en.wikipedia.org/wiki/Scheduling_(computing)#First_come,_first_served
from typing import List


def calculate_waiting_times(duration_times: List[int]) -> List[int]:
    """
    This function calculates the waiting time of some processes that have a
    specified duration time.
        Return: The waiting time for each process.
    >>> calculate_waiting_times([5, 10, 15])
    [0, 5, 15]
    >>> calculate_waiting_times([1, 2, 3, 4, 5])
    [0, 1, 3, 6, 10]
    >>> calculate_waiting_times([10, 3])
    [0, 10]
    """
    waiting_times = [0] * len(duration_times)
    for i in range(1, len(duration_times)):
        waiting_times[i] = duration_times[i - 1] + waiting_times[i - 1]
    return waiting_times


def calculate_turnaround_times(
    duration_times: List[int], waiting_times: List[int]
) -> List[int]:
    """
    This function calculates the turnaround time of some processes.
        Return: The time difference between the completion time and the
                arrival time.
                Practically waiting_time + duration_time
    >>> calculate_turnaround_times([5, 10, 15], [0, 5, 15])
    [5, 15, 30]
    >>> calculate_turnaround_times([1, 2, 3, 4, 5], [0, 1, 3, 6, 10])
    [1, 3, 6, 10, 15]
    >>> calculate_turnaround_times([10, 3], [0, 10])
    [10, 13]
    """
    return [
        duration_time + waiting_times[i]
        for i, duration_time in enumerate(duration_times)
    ]


def calculate_average_turnaround_time(turnaround_times: List[int]) -> float:
    """
    This function calculates the average of the turnaround times
        Return: The average of the turnaround times.
    >>> calculate_average_turnaround_time([0, 5, 16])
    7.0
    >>> calculate_average_turnaround_time([1, 5, 8, 12])
    6.5
    >>> calculate_average_turnaround_time([10, 24])
    17.0
    """
    return sum(turnaround_times) / len(turnaround_times)


def calculate_average_waiting_time(waiting_times: List[int]) -> float:
    """
    This function calculates the average of the waiting times
        Return: The average of the waiting times.
    >>> calculate_average_waiting_time([0, 5, 16])
    7.0
    >>> calculate_average_waiting_time([1, 5, 8, 12])
    6.5
    >>> calculate_average_waiting_time([10, 24])
    17.0
    """
    return sum(waiting_times) / len(waiting_times)


if __name__ == "__main__":
    # process id's
    processes = [1, 2, 3]

    # ensure that we actually have processes
    if len(processes) == 0:
        print("Zero amount of processes")
        exit()

    # duration time of all processes
    duration_times = [19, 8, 9]

    # ensure we can match each id to a duration time
    if len(duration_times) != len(processes):
        print("Unable to match all id's with their duration time")
        exit()

    # get the waiting times and the turnaround times
    waiting_times = calculate_waiting_times(duration_times)
    turnaround_times = calculate_turnaround_times(duration_times, waiting_times)

    # get the average times
    average_waiting_time = calculate_average_waiting_time(waiting_times)
    average_turnaround_time = calculate_average_turnaround_time(turnaround_times)

    # print all the results
    print("Process ID\tDuration Time\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(processes):
        print(
            f"{process}\t\t{duration_times[i]}\t\t{waiting_times[i]}\t\t"
            f"{turnaround_times[i]}"
        )
    print(f"Average waiting time = {average_waiting_time}")
    print(f"Average turn around time = {average_turnaround_time}")
