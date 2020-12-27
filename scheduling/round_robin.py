"""
Round Robin is a scheduling algorithm.
In Round Robin each process is assigned a fixed time slot in a cyclic way.
https://en.wikipedia.org/wiki/Round-robin_scheduling
"""
from statistics import mean
from typing import List


def calculate_waiting_times(burst_times: List[int]) -> List[int]:
    """
    Calculate the waiting times of a list of processes that have a specified duration.

    Return: The waiting time for each process.
    >>> calculate_waiting_times([10, 5, 8])
    [13, 10, 13]
    >>> calculate_waiting_times([4, 6, 3, 1])
    [5, 8, 9, 6]
    >>> calculate_waiting_times([12, 2, 10])
    [12, 2, 12]
    """
    quantum = 2
    rem_burst_times = list(burst_times)
    waiting_times = [0] * len(burst_times)
    t = 0
    while True:
        done = True
        for i, burst_time in enumerate(burst_times):
            if rem_burst_times[i] > 0:
                done = False
                if rem_burst_times[i] > quantum:
                    t += quantum
                    rem_burst_times[i] -= quantum
                else:
                    t += rem_burst_times[i]
                    waiting_times[i] = t - burst_time
                    rem_burst_times[i] = 0
        if done is True:
            return waiting_times


def calculate_turn_around_times(
    burst_times: List[int], waiting_times: List[int]
) -> List[int]:
    """
    >>> calculate_turn_around_times([1, 2, 3, 4], [0, 1, 3])
    [1, 3, 6]
    >>> calculate_turn_around_times([10, 3, 7], [10, 6, 11])
    [20, 9, 18]
    """
    return [burst + waiting for burst, waiting in zip(burst_times, waiting_times)]


if __name__ == "__main__":
    burst_times = [3, 5, 7]
    waiting_times = calculate_waiting_times(burst_times)
    turn_around_times = calculate_turn_around_times(burst_times, waiting_times)
    print("Process ID \tBurst Time \tWaiting Time \tTurnaround Time")
    for i, burst_time in enumerate(burst_times):
        print(
            f"  {i + 1}\t\t  {burst_time}\t\t  {waiting_times[i]}\t\t  "
            f"{turn_around_times[i]}"
        )
    print(f"\nAverage waiting time = {mean(waiting_times):.5f}")
    print(f"Average turn around time = {mean(turn_around_times):.5f}")
