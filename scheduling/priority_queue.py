# Implementation of Priority Queue scheduling algorithm (without preemption)
# In this Algorithm we only care about the order that the processes arrived
# without caring about their duration time
# https://en.wikipedia.org/wiki/Scheduling_(computing)#Priority_scheduling
from __future__ import annotations


def sort_processes_by_priority(
    processes: list[int], duration_times: list[int], priorities: list[int]
) -> list[int]:
    """
    This function will sort the processes and their data for use as arguments
    for other functions in a single list.
        Return: The process id and duration time for each process sorted by priority.
    >>> sort processes_by_priority([11, 12, 13], [3, 8, 5], [2, 1, 3])
    [(12, 11, 13), (8, 3, 5)]
    >>> sort processes_by_priority([11, 12, 13, 14], [13, 2, 1, 10], [3, 2, 1, 4])
    [(13, 12, 11, 14), (1, 2, 13, 10)]
    >>> sort processes_by_priority([101, 110], [10, 5], [4, 5])
    [(101, 110), (10, 5)]
    """
    prioritized_queue = []
    sorted_processes, sorted_duration_times = [], []
    for process, duration_time, priority in zip(processes, duration_times, priorities):
        prioritized_queue.append((process, duration_time, priority))
    prioritized_queue = sorted(prioritized_queue, key=lambda x: (x[2]))
    priorities = priorities.sort()

    for process, duration_time, priority in prioritized_queue:
        sorted_processes.append(process)
        sorted_duration_times.append(duration_time)
    return sorted_processes, sorted_duration_times


def calculate_waiting_times(duration_times: list[int]) -> list[int]:
    """
    This function calculates the waiting time of processes using their
    duration time.
        Return: The waiting time for each process.
    >>> calculate_waiting_times([3, 8, 10])
    [0, 3, 11]
    >>> calculate_waiting_times([1, 2, 3, 4, 5])
    [0, 1, 3, 6, 10]
    >>> calculate_waiting_times([15, 2])
    [0, 15]
    """
    waiting_times = [0] * len(duration_times)
    for i in range(1, len(duration_times)):
        waiting_times[i] = duration_times[i - 1] + waiting_times[i - 1]
    return waiting_times


def calculate_turnaround_times(
    duration_times: list[int], waiting_times: list[int]
) -> list[int]:
    """
    This function calculates the turnaround time of the processes.
        Return: The time difference between the completion time and the
                arrival time.
    >>> calculate_turnaround_times([3, 8, 10], [0, 3, 11])
    [3, 11, 21]
    >>> calculate_turnaround_times([1, 2, 3, 4, 5], [0, 1, 3, 6, 10])
    [1, 3, 6, 10, 15]
    >>> calculate_turnaround_times([15, 2], [0, 15])
    [15, 17]
    """
    return [
        duration_time + waiting_times[i]
        for i, duration_time in enumerate(duration_times)
    ]


def calculate_average_turnaround_time(turnaround_times: list[int]) -> float:
    """
    This function calculates the average of the turnaround times
        Return: The average of the turnaround times.
    >>> calculate_average_turnaround_time([0, 8, 13])
    7.0
    >>> calculate_average_turnaround_time([1, 4, 9, 12])
    6.5
    >>> calculate_average_turnaround_time([14, 20])
    17.0
    """
    return sum(turnaround_times) / len(turnaround_times)


def calculate_average_waiting_time(waiting_times: list[int]) -> float:
    """
    This function calculates the average of the waiting times
        Return: The average of the waiting times.
    >>> calculate_average_waiting_time([0, 8, 13])
    7.0
    >>> calculate_average_waiting_time([1, 4, 9, 12])
    6.5
    >>> calculate_average_waiting_time([14, 20])
    17.0
    """
    return sum(waiting_times) / len(waiting_times)


if __name__ == "__main__":
    # process id's
    processes = [1, 2, 3]

    # checking if we have processes to work with
    if len(processes) == 0:
        print("Zero amount of processes")
        exit()

    # duration time of all processes
    duration_times = [19, 8, 9]

    # arrival time of all processes
    arrival_times = [0, 5, 6]

    # priorities of all processes
    priorities = [2, 1, 3]

    # ensure we can match each id to a duration time
    if len(duration_times) != len(processes):
        print("Unable to match all id's with their duration time")
        exit()

    # ensure we can match each id to an arrival time
    if len(arrival_times) != len(processes):
        print("Unable to match all id's with their arrival time")
        exit()

    # ensure we can match each id to its priority
    if len(priorities) != len(processes):
        print("Unable to match all id's with their priorities")
        exit()

    # sort processes and their data by priority
    processes, arrival_times = sort_processes_by_priority(
        processes, duration_times, priorities
    )

    # get the waiting times and the turnaround times
    waiting_times = calculate_waiting_times(duration_times)
    turnaround_times = calculate_turnaround_times(duration_times, waiting_times)

    # get the average times
    average_waiting_time = calculate_average_waiting_time(waiting_times)
    average_turnaround_time = calculate_average_turnaround_time(turnaround_times)

    # print all the results
    print("Process ID\tDuration Time\tWaiting Time\tTurnaround Time\tPriority")
    for i, process in enumerate(processes):
        print(
            f"{process}\t\t{duration_times[i]}\t\t{waiting_times[i]}\t\t"
            f"{turnaround_times[i]}\t\t{priorities[i]}"
        )
    print(f"Average waiting time = {average_waiting_time}")
    print(f"Average turn around time = {average_turnaround_time}")
