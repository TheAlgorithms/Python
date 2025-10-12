"""
Shortest Job Remaining First (Preemptive SJF)
---------------------------------------------
Please note arrival time and burst time.
Use spaces to separate times entered.
"""

from __future__ import annotations
import pandas as pd
import matplotlib.pyplot as plt


def calculate_waitingtime(
    arrival_time: list[int], burst_time: list[int], no_of_processes: int
) -> tuple[list[int], list[tuple[int, int, int]]]:
    """
    Calculate the waiting time for each process and record execution timeline for Gantt Chart.
    Returns: (waiting_time, timeline)
    timeline -> list of tuples: (start_time, end_time, process_id)
    """
    remaining_time = burst_time.copy()
    waiting_time = [0] * no_of_processes
    complete = 0
    increment_time = 0
    minm = float("inf")
    short = 0
    check = False

    timeline = []  # To store execution sequence for Gantt chart
    last_process = -1

    while complete != no_of_processes:
        for j in range(no_of_processes):
            if (
                arrival_time[j] <= increment_time
                and remaining_time[j] > 0
                and remaining_time[j] < minm
            ):
                minm = remaining_time[j]
                short = j
                check = True

        if not check:
            increment_time += 1
            continue

        # Record when process switches (for Gantt chart)
        if short != last_process:
            if timeline and timeline[-1][2] == last_process:
                timeline[-1] = (timeline[-1][0], increment_time, last_process)
            if short != -1:
                timeline.append((increment_time, None, short))
            last_process = short

        remaining_time[short] -= 1
        minm = remaining_time[short]
        if minm == 0:
            minm = float("inf")

        if remaining_time[short] == 0:
            complete += 1
            check = False
            finish_time = increment_time + 1
            finar = finish_time - arrival_time[short]
            waiting_time[short] = finar - burst_time[short]
            waiting_time[short] = max(waiting_time[short], 0)

        increment_time += 1

    # Close last ongoing process in timeline
    if timeline and timeline[-1][1] is None:
        timeline[-1] = (timeline[-1][0], increment_time, last_process)

    return waiting_time, timeline


def calculate_turnaroundtime(
    burst_time: list[int], no_of_processes: int, waiting_time: list[int]
) -> list[int]:
    """Calculate the turn around time for each process."""
    turn_around_time = [0] * no_of_processes
    for i in range(no_of_processes):
        turn_around_time[i] = burst_time[i] + waiting_time[i]
    return turn_around_time


def calculate_average_times(
    waiting_time: list[int], turn_around_time: list[int], no_of_processes: int
) -> tuple[float, float]:
    """Calculate and return average waiting and turnaround times."""
    avg_wait = sum(waiting_time) / no_of_processes
    avg_turn = sum(turn_around_time) / no_of_processes
    print(f"Average waiting time = {avg_wait:.5f}")
    print(f"Average turn around time = {avg_turn:.5f}")
    return avg_wait, avg_turn


def plot_gantt_chart(
    timeline: list[tuple[int, int, int]], processes: list[int]
) -> None:
    """Plot a Gantt chart for process execution."""
    fig, ax = plt.subplots(figsize=(10, 2))
    colors = plt.cm.tab10.colors  # Nice color set
    for start, end, pid in timeline:
        ax.barh(
            0,
            end - start,
            left=start,
            color=colors[pid % len(colors)],
            edgecolor="black",
            label=f"P{processes[pid]}",
        )
        ax.text(
            (start + end) / 2,
            0,
            f"P{processes[pid]}",
            ha="center",
            va="center",
            color="white",
            fontsize=9,
        )

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart - Shortest Job Remaining First (SJF Preemptive)")
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(
        by_label.values(), by_label.keys(), bbox_to_anchor=(1.05, 1), loc="upper left"
    )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Enter how many processes you want to analyze:")
    no_of_processes = int(input().strip())

    burst_time = [0] * no_of_processes
    arrival_time = [0] * no_of_processes
    processes = list(range(1, no_of_processes + 1))

    for i in range(no_of_processes):
        print(f"Enter the arrival time and burst time for process {i + 1}:")
        arrival_time[i], burst_time[i] = map(int, input().split())

    waiting_time, timeline = calculate_waitingtime(
        arrival_time, burst_time, no_of_processes
    )
    turn_around_time = calculate_turnaroundtime(
        burst_time, no_of_processes, waiting_time
    )
    calculate_average_times(waiting_time, turn_around_time, no_of_processes)

    # Display results table
    df = pd.DataFrame(
        list(zip(processes, arrival_time, burst_time, waiting_time, turn_around_time)),
        columns=[
            "Process",
            "ArrivalTime",
            "BurstTime",
            "WaitingTime",
            "TurnAroundTime",
        ],
    )
    pd.set_option("display.max_rows", df.shape[0] + 1)
    print("\n--- Process Table ---")
    print(df)

    # Plot Gantt chart
    plot_gantt_chart(timeline, processes)
