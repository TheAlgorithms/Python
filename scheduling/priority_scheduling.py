"""
Priority Scheduling assigns a priority to each process. The CPU is allocated
to the process with the highest priority (lowest number). It can be preemptive
or non-preemptive.
https://en.wikipedia.org/wiki/Priority_scheduling
"""

from statistics import mean


def calculate_priority_waiting_time(arrival: list, burst: list, priority: list) -> list:
    """
    Calculate waiting time for each process using preemptive priority scheduling.

    >>> calculate_priority_waiting_time([0, 1, 2, 3], [10, 1, 2, 1], [3, 1, 4, 2])
    [2, 0, 10, 0]
    """
    n = len(arrival)
    remaining = burst.copy()
    waiting = [0] * n
    complete = 0
    t = 0

    while complete < n:
        idx = -1
        highest_pri = float("inf")
        for i in range(n):
            if arrival[i] <= t and remaining[i] > 0 and priority[i] < highest_pri:
                highest_pri = priority[i]
                idx = i

        if idx == -1:
            t += 1
            continue

        remaining[idx] -= 1
        t += 1

        if remaining[idx] == 0:
            complete += 1
            waiting[idx] = t - arrival[idx] - burst[idx]

    return waiting


def calculate_priority_turnaround_time(burst: list, waiting: list) -> list:
    """
    Calculate turn around time for each process using waiting time.

    >>> calculate_priority_turnaround_time([10, 1, 2, 1], [3, 0, 5, 1])
    [13, 1, 7, 2]
    """
    return [burst[i] + waiting[i] for i in range(len(burst))]


if __name__ == "__main__":
    arrival_time = [0, 1, 2, 3]
    burst_time = [10, 1, 2, 1]
    priority = [3, 1, 4, 2]

    waiting_time = calculate_priority_waiting_time(arrival_time, burst_time, priority)
    turnaround_time = calculate_priority_turnaround_time(burst_time, waiting_time)

    print("PID\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
    for i in range(len(arrival_time)):
        print(
            f"P{i + 1}\t{arrival_time[i]}\t{burst_time[i]}\t{priority[i]}\t\t{waiting_time[i]}\t{turnaround_time[i]}"
        )

    print(f"Average Waiting Time: {mean(waiting_time):.2f}")
    print(f"Average Turnaround Time: {mean(turnaround_time):.2f}")
