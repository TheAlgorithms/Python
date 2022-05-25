# SJF
"""
Non-preemptive Shortest Job First
Shortest execution time process is chosen for the next execution.
https://www.guru99.com/shortest-job-first-sjf-scheduling.html
https://en.wikipedia.org/wiki/Shortest_job_next
"""


from __future__ import annotations

from statistics import mean


def calculate_waitingtime(
        arrival_time: list[int], burst_time: list[int], no_of_processes: int
) -> list[int]:
    # Arrival_time : 도착 시간을 담은 리스트
    # Burst_time : 수행시간
    # No_of_processes : 프로세스의 개수, the number of processes

    """
    Calculate the waiting time of each processes

    Return: The waiting time for each process.
    >>> calculate_waitingtime([0,1,2], [10, 5, 8], 3)
    [0, 9, 13]
    >>> calculate_waitingtime([1,2,2,4], [4, 6, 3, 1], 4)
    [0, 7, 4, 1]
    >>> calculate_waitingtime([0,0,0], [12, 2, 10],3)
    [12, 0, 2]
    """

    # waiting_time : 대기 시간
    # remaining_time : 남은 수행 시간
    waiting_time = [0] * no_of_processes
    remaining_time = [0] * no_of_processes

    """
    Initialize remaining_time to waiting_time.
    남은 수행 시간을 수행 시간으로 초기화한다.
    """
    for i in range(no_of_processes):
        remaining_time[i] = burst_time[i]
    ready_process = []

    # completed : 수행 완료된 프로세스의 수, The number of processes completed
    # total_time : 프로세스와 무관하게 진행되는 시간
    completed = 0
    total_time = 0

    """
    수행할 프로세스가 남아 있을 때,
        도착 시간이 지났고 남아 있는 수행 시간이 있는 프로세스는 ready_process에 들어간다.
        ready_process에서 가장 짧은 프로세스인 target_process가 실행된다.

    When processes are not completed,
        A process whose arrival time has passed \
        and has remaining execution time is put into the ready_process.
        The shortest process in the ready_process, target_process is executed.
    """
    while completed != no_of_processes:
        ready_process = []
        target_process = -1

        for i in range(no_of_processes):
            if (arrival_time[i] <= total_time) & (remaining_time[i] > 0):
                ready_process.append(i)

        if len(ready_process) > 0:
            target_process = ready_process[0]
            for i in ready_process:
                if remaining_time[i] < remaining_time[target_process]:
                    target_process = i
            total_time += burst_time[target_process]
            completed += 1
            remaining_time[target_process] = 0
            waiting_time[target_process] = \
                total_time - arrival_time[target_process]\
                - burst_time[target_process]
        else:
            total_time += 1

    return waiting_time


def calculate_turnaroundtime(
        burst_time: list[int], no_of_processes: int, waiting_time: list[int]
) -> list[int]:
    """
    Calculate the turnaround time of each Processes

    Return: The turnaround time for each process.
    >>> calculate_turnaroundtime([0,1,2], 3, [0, 10, 15])
    [0, 11, 17]
    >>> calculate_turnaroundtime([1,2,2,4], 4, [1, 8, 5, 4])
    [2, 10, 7, 8]
    >>> calculate_turnaroundtime([0,0,0], 3, [12, 0, 2])
    [12, 0, 2]
    """

    turn_around_time = [0] * no_of_processes
    for i in range(no_of_processes):
        turn_around_time[i] = burst_time[i] \
            + waiting_time[i]
    return turn_around_time


if __name__ == "__main__":
    print("[TEST CASE 01]")

    no_of_processes = 4
    burst_time = [2, 5, 3, 7]
    arrival_time = [0, 0, 0, 0]
    processes = list(range(1, 5))
    waiting_time = calculate_waitingtime(arrival_time,
                                         burst_time, no_of_processes)
    turn_around_time = calculate_turnaroundtime(burst_time,
                                                no_of_processes, waiting_time)

    # Printing the Result
    print("PID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for i, processes in enumerate(processes):
        print(
            f"{processes}\t{burst_time[i]}\t\t\t{arrival_time[i]}\t\t\t\t"
            f"{waiting_time[i]}\t\t\t\t{turn_around_time[i]}"
        )
    print(f"\nAverage waiting time = {mean(waiting_time):.5f}")
    print(f"Average turnaround time = {mean(turn_around_time):.5f}")
