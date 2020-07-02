"""
Round Robin is a CPU scheduling algorithm.
In Round Robin each process is assigned a fixed time slot in a cyclic way.
https://en.wikipedia.org/wiki/Round-robin_scheduling
"""


def calculate_waiting_time(processes, n, burst_time, waiting_time, quantum):
    """
    Calculate the waiting time of some processes that have a
    specified duration time.
        Return: The waiting time for each process.
    >>> calculate_waiting_time([5, 10, 15])
    [0, 5, 15]
    >>> calculate_waiting_times([1, 2, 3, 4, 5])
    [0, 1, 3, 6, 10]
    >>> calculate_waiting_times([10, 3])
    [0, 10]
    """
    rem_burst_time = [0] * n
    for i in range(n):
        rem_burst_time[i] = burst_time[i]
    t = 0
    while 1:
        done = True
        for i in range(n):
            if rem_burst_time[i] > 0:
                done = False
                if rem_burst_time[i] > quantum:
                    t += quantum
                    rem_burst_time[i] -= quantum
                else:
                    t = t + rem_burst_time[i]
                    waiting_time[i] = t - burst_time[i]
                    rem_burst_time[i] = 0
        if done is True:
            break


def calculate_turn_around_time(
    processes, n, burst_time, waiting_time, turn_around_time
):

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

    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]


def calculate_avg_time(processes, n, burst_time, quantum):
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
    waiting_time = [0] * n
    turn_around_time = [0] * n
    calculate_waiting_time(processes, n, burst_time, waiting_time, quantum)
    calculate_turn_around_time(processes, n, burst_time, waiting_time, turn_around_time)
    print("Processes    Burst Time     Waiting Time    Turn-Around Time")
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(n):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
        print(
            " ",
            i + 1,
            "\t\t",
            burst_time[i],
            "\t\t",
            waiting_time[i],
            "\t\t",
            turn_around_time[i],
        )
    print("\nAverage waiting time = %.5f " % (total_waiting_time / n))
    print("Average turn around time = %.5f " % (total_turn_around_time / n))


if __name__ == "__main__":
    # Process id
    processes = [1, 2, 3]
    n = 3
    burst_time = [10, 5, 8]
    quantum = 2
    calculate_avg_time(processes, n, burst_time, quantum)
