from collections import deque


# ---------------- FCFS ----------------
def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Turnaround time = waiting + burst
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n
    return waiting_time, turnaround_time, avg_wt, avg_tat


if __name__ == "__main__":
    processes = [1, 2, 3]
    burst_time = [5, 9, 6]

    print("FCFS:", fcfs(processes, burst_time))
