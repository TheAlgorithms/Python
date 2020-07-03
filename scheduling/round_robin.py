"""
Round Robin is a CPU scheduling algorithm.
In Round Robin each process is assigned a fixed time slot in a cyclic way.
https://en.wikipedia.org/wiki/Round-robin_scheduling
"""


def calculate_waiting_time(burst_time: int) -> int:
    """
    Calculate the waiting time of some processes that have a
    specified duration time.
        Return: The waiting time for each process.
    >>> calculate_waiting_time([10, 5, 8])
    [13, 10, 13]
    >>> calculate_waiting_time([4, 6, 3, 1])
    [4, 7, 8]
    >>> calculate_waiting_time([12, 2, 10])
    [12, 2, 12]
    """
    n = 3
    waiting_time = [0] * n
    quantum = 2
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
            return waiting_time


def calculate_turn_around_time(burst_time: int, waiting_time: int) -> int:

    """
    Calculate the turnaround time of some processes.
        Return: The time difference between the completion time and the
                arrival time.
                Practically waiting_time + duration_time
    >>> calculate_turn_around_time([5, 10, 15], [8, 13, 15])
    [13, 23, 30]
    >>> calculate_turn_around_time([1, 2, 3, 4], [0, 1, 3])
    [1, 3, 6]
    >>> calculate_turn_around_time([10, 3, 7], [10, 6, 11])
    [20, 9, 18]
    """
    n = 3
    turn_around_time = [0] * n
    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]
    return turn_around_time


def calculate_avg_waiting_time(waiting_time: int) -> float:
    """
    This function calculates the average of the waiting times
        Return: The average of the waiting times.
    >>> calculate_avg_waiting_time([10, 6, 11])
    9.0
    >>> calculate_avg_waiting_time([12, 2, 10])
    8.0
    >>> calculate_avg_waiting_time([4, 7, 8])
    6.333333333333333
    """
    return sum(waiting_time) / len(waiting_time)


def calculate_avg_turnaround_time(turn_around_time: int) -> float:
    """
    This function calculates the average of the waiting times
        Return: The average of the waiting times.
    >>> calculate_avg_turnaround_time([25, 41, 23])
    29.666666666666668
    >>> calculate_avg_turnaround_time([10, 3, 7])
    6.666666666666667
    >>> calculate_avg_turnaround_time([18, 21, 12])
    17.0
    """
    return sum(turn_around_time) / len(turn_around_time)


if __name__ == "__main__":
    # Process id
    processes = [1, 2, 3]
    n = 3
    burst_time = [3, 5, 7]
    quantum = 2
    waiting_time = calculate_waiting_time(burst_time)
    turn_around_time = calculate_turn_around_time(burst_time, waiting_time)
    avg_wating_time = 0
    avg_turn_around_time = 0
    avg_waiting_time = calculate_avg_waiting_time(waiting_time)
    avg_turn_around_time = calculate_avg_turnaround_time(turn_around_time)
    print("Process ID \tBurst Time \tWaiting Time \tTurnaround Time")
    for i in range(n):
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
    print("\nAverage waiting time = %.5f " % (avg_waiting_time))
    print("Average turn around time = %.5f " % (avg_turn_around_time))
