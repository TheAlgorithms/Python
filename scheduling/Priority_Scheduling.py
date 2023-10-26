# Implementation of Priority Based scheduling algorithm
from __future__ import annotations

# Define a class to represent a process with priority
class Process:
    def __init__(self, id, priority, burst):
        self.id = id  # Process ID
        self.priority = priority  # Priority
        self.burst = burst  # Burst time

# Priority Scheduling algorithm
def priority_scheduling(processes):
    # Sort processes by priority (lower number indicates higher priority)
    processes.sort(key=lambda x: x.priority)
    
    # Initialize waiting times and turnaround times
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    
    # Calculate waiting times and turnaround times
    waiting_times[0] = 0
    for i in range(1, len(processes)):
        waiting_times[i] = waiting_times[i - 1] + processes[i - 1].burst
    for i in range(len(processes)):
        turnaround_times[i] = waiting_times[i] + processes[i].burst
    
    # Calculate average waiting time and average turnaround time
    average_waiting_time = sum(waiting_times) / len(processes)
    average_turnaround_time = sum(turnaround_times) / len(processes)
    
    # Print the results
    print("Process ID\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(processes):
        print(
            f"{process.id}\t\t{process.priority}\t\t{process.burst}\t\t"
            f"{waiting_times[i]}\t\t{turnaround_times[i}"
        )
    print(f"Average Waiting Time = {average_waiting_time}")
    print(f"Average Turnaround Time = {average_turnaround_time}")

if __name__ == "__main__":
    # List of processes with priority and burst time
    processes = [Process(1, 2, 10), Process(2, 1, 6), Process(3, 3, 8)]
    
    # Run the Priority Scheduling algorithm
    priority_scheduling(processes)
