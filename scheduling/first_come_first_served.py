# Implementation of First Come First Served CPU scheduling Algorithm
# In this Algorithm we just care about the order that the processes arrived
# without carring about their duration time
# https://en.wikipedia.org/wiki/Scheduling_(computing)#First_come,_first_served
from typing import List
from functools import reduce


def calculate_waiting_time(
    number_of_processes: int, duration_time: List[int]
) -> List[int]:
    """
    This function calculates the waiting time of some processes that have a specified duration time.
        Return: The waiting time for each process.
    >>> calculate_waiting_time(3, [5,10,15])
    [0, 5, 15]
    >>> calculate_waiting_time(5, [1,2,3,4,5])
    [0, 1, 3, 6, 10]
    >>> calculate_waiting_time(2, [10, 3])
    [0, 10]
    """
    # Initialize the result of the waiting time to all zeroes
    waiting_time: List[int] = [0] * number_of_processes
    # calculating waiting time. First item should always be 0 so the iteration starts from index 1
    for i in range(1, number_of_processes):
        waiting_time[i] = duration_time[i - 1] + waiting_time[i - 1]
    return waiting_time


def calculate_turnaround_time(
    number_of_processes: int, duration_time: List[int], waiting_time: List[int]
) -> List[int]:
    """
    This function calculates the turnaround time of some processes.
        Return: The time difference between the completion time and the arrival time.
                Practically waiting_time + duration_time
    >>> calculate_turnaround_time(3, [5, 10, 15], [0, 5, 15])
    [5, 15, 30]
    >>> calculate_turnaround_time(5, [1, 2, 3, 4, 5], [0, 1, 3, 6, 10])
    [1, 3, 6, 10, 15]
    >>> calculate_turnaround_time(2, [10, 3], [0, 10])
    [10, 13]
    """
    # Initialize the result of the waiting time to all zeroes
    turnaround_time: List[int] = [0] * number_of_processes
    for i in range(number_of_processes):
        turnaround_time[i] = duration_time[i] + waiting_time[i]
    return turnaround_time


def calculate_average_turnaround_time(number_of_processes, turnaround_time) -> float:
    """
    This function calculates the average of the turnaround times
        Return: The average of the turnaround times.
    >>> calculate_average_turnaround_time(3, [0, 5, 16])
    7.0
    >>> calculate_average_turnaround_time(4, [1, 5, 8, 12])
    6.5
    >>> calculate_average_turnaround_time(2, [10, 24])
    17.0
    """
    total_turnaround_time: List[int] = reduce(lambda x, y: x + y, turnaround_time, 0)
    return total_turnaround_time / number_of_processes


def calculate_average_waiting_time(number_of_processes, waiting_time) -> float:
    """
    This function calculates the average of the waiting times
        Return: The average of the waiting times.
    >>> calculate_average_waiting_time(3, [0, 5, 16])
    7.0
    >>> calculate_average_waiting_time(4, [1, 5, 8, 12])
    6.5
    >>> calculate_average_waiting_time(2, [10, 24])
    17.0
    """
    total_waiting_time: List[int] = reduce(lambda x, y: x + y, waiting_time, 0)
    return total_waiting_time / number_of_processes


if __name__ == "__main__":

    # process id's
    processes = [1, 2, 3]

    # ensure that we actually have prosecces
    if len(processes) == 0:
        print("Zero amount of processes")
        exit()

    # duration time of all processes
    duration_time = [19, 8, 9]

    # ensure we can match each id to a duration time
    if len(duration_time) != len(processes):
        print("Unable to match all id's with their duration time")
        exit()

    # get the waiting times and the turnaround times
    waiting_time = calculate_waiting_time(len(processes), duration_time)
    turnaround_time = calculate_turnaround_time(
        len(processes), duration_time, waiting_time
    )

    # get the average times
    average_waiting_time = calculate_average_waiting_time(len(processes), waiting_time)
    average_turnaround_time = calculate_average_turnaround_time(
        len(processes), turnaround_time
    )

    # print all the results
    print("Process ID\tDuration Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(
            f"{processes[i]}\t\t{duration_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}"
        )
    print(f"Average waiting time = {average_waiting_time}")
    print(f"Average turn around time = {average_turnaround_time}")