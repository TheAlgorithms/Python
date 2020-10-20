"""
First come first serve(FCFS) scheduling algorithm, as the name suggests,
the process which arrives first, gets executed first, or we can say
that the process which requests the CPU first, gets the CPU allocated first.
"""

def find_waiting_time(processes, n, bt, wt) -> None:
    """
    Find the waiting time
    n = number of processes
    wt = waiting time
    bt = burst time
    """
    """
    waiting time for  
    first process is 0 
    """
    wt[0] = 0
    """
    calculating waiting time
    waiting time = burst time[previous process]+waiting time[previous process]
    """
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def find_turn_around_time(processes, n, bt, wt, tat) -> None:
    """
    tat= turn around time
    turnaround time = waiting_time + burst_time
    """
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def find_avg_time(processes, n, bt) -> None:
    """
    average waiting time = total_waiting_time / no_of_processes

    average turnaround time = total_turn_around_time / no_of_processes.
    """
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    find_waiting_time(processes, n, bt, wt)

    find_turn_around_time(processes, n,bt, wt, tat)

    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
              str(bt[i]) + "\t " +
              str(wt[i]) + "\t\t " +
              str(tat[i]))

    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))


if __name__ == "__main__":
    processes = [0, 1, 2]
    n = len(processes)
    burst_time = [5, 15, 10]
    find_avg_time(processes, n, burst_time)
