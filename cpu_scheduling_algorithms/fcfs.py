"""
Simple Implementation of the FCFS CPU scheduling algorithm
FCFS is a non-preemptive CPU scheduling algorithm that
schedules processes based on their arrival time.
https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/
Author: [Madhav Goyal](https://github.com/mdhvg)
"""


def fcfs(processes: list[tuple[int, int, int]]) -> None:
    """
    Function to implement the FCFS CPU scheduling algorithm

    processes: list of tuples where each tuple contains the
    process_id, arrival_time and burst_time of each process

    >>> processes = [(1, 0, 3), (2, 2, 7), (3, 1, 4), (4, 5, 2)]
    >>> fcfs(processes)
    Average Waiting Time: 6.0
    *---*----*-------*--
    1   3    2       4
    """
    total_processes = len(processes)
    processes.sort(key=lambda process: process[1])
    waiting_times = [0] * total_processes
    total_waiting_time = 0

    for i in range(1, total_processes):
        waiting_times[i] = processes[i - 1][2] + waiting_times[i - 1]
        total_waiting_time += waiting_times[i]

    print(f"Average Waiting Time: {total_waiting_time / total_processes}")

    """
    Printing the Gantt Chart for the processes in the FCFS order
    The - and * symbols are used to represent the burst time and
    idle time respectively for each process.
    """
    last_burst = 0
    for i in range(total_processes):
        print("-" * last_burst, end="")
        print("*", end="")
        last_burst = processes[i][2]
    print("-" * last_burst, end="")
    print("\n", end="")

    last_burst = 0
    for i in range(total_processes):
        print(" " * last_burst, end="")
        print(f"{processes[i][0]}", end="")
        last_burst = processes[i][2]
    print("\n", end="")


def main() -> None:
    """
    Main function to demonstrate the FCFS CPU scheduling algorithm
    pass an array of (process_id, arrival_time, burst_time) to fcfs
    >>> processes = [(1, 0, 3), (2, 1, 5), (3, 2, 2), (4, 3, 7), (5, 2, 2)]
    >>> fcfs(processes)
    Average Waiting Time: 6.6
    *---*-----*--*--*-------
    1   2     3  5  4
    """
    processes = [(1, 0, 3), (2, 1, 5), (3, 2, 2), (4, 3, 7), (5, 2, 2)]
    fcfs(processes)


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod()
