# Reference - https://en.wikipedia.org/wiki/Fixed-priority_pre-emptive_scheduling

from __future__ import annotations


def calculate_waiting_times(
    duration_times: list[int], priorities: list[int]
) -> list[int]:
    """
    This function calculates the waiting time of some processes that have a
    specified duration time and priority.
        Return: The waiting time for each process.
    """
    waiting_times = [0] * len(duration_times)
    sorted_processes = sorted(enumerate(duration_times), key=lambda x: priorities[x[0]])

    for i in range(1, len(sorted_processes)):
        process_id, duration_time = sorted_processes[i]
        waiting_times[process_id] = (
            waiting_times[sorted_processes[i - 1][0]] + sorted_processes[i - 1][1]
        )

    return waiting_times


def calculate_turnaround_times(
    duration_times: list[int], waiting_times: list[int]
) -> list[int]:
    """
    This function calculates the turnaround time of some processes.
        Return: The time difference between the completion time and the
                arrival time.
                Practically waiting_time + duration_time
    """
    return [
        duration_time + waiting_times[i]
        for i, duration_time in enumerate(duration_times)
    ]


def calculate_average_turnaround_time(turnaround_times: list[int]) -> float:
    """
    This function calculates the average of the turnaround times
        Return: The average of the turnaround times.
    """
    return sum(turnaround_times) / len(turnaround_times)


def calculate_average_waiting_time(waiting_times: list[int]) -> float:
    """
    This function calculates the average of the waiting times
        Return: The average of the waiting times.
    """
    return sum(waiting_times) / len(waiting_times)


if __name__ == "__main__":
    # process id's
    processes = [1, 2, 3]

    # ensure that we actually have processes
    if len(processes) == 0:
        print("Zero amount of processes")
        raise SystemExit(0)

    # duration time and priority of all processes
    duration_times = [19, 8, 9]
    priorities = [2, 1, 3]

    # ensure we can match each id to a duration time and priority
    if len(duration_times) != len(processes) or len(priorities) != len(processes):
        print("Unable to match all id's with their duration time or priority")
        raise SystemExit(0)

    # get the waiting times and the turnaround times
    waiting_times = calculate_waiting_times(duration_times, priorities)
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
