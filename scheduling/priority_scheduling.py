"""
Implementation of Priority Scheduling

https://en.wikipedia.org/wiki/Scheduling_(computing)#Priority_scheduling
"""

from operator import attrgetter

"""

Creating a class process which will have
all required attributes

"""


class process:
    def __init__(self, process_name, arrival_time, burst_time, priority):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = None
        self.turn_around_time = None


if __name__ == "__main__":

    n = int(input("Enter number of processes: ").strip())
    processes = []

    for i in range(n):
        process_name = input("Enter process name: ").strip()
        arrival_time = int(input("Enter arrival time: ").strip())
        burst_time = int(input("Enter burst time: ").strip())
        priority = int(input("Enter Priority: ").strip())

        processes.append(process(process_name, arrival_time, burst_time, priority))

    """
    Executed processes from the original array will be deleted
    and will be appended to the array below
    """
    executed_processes = []

    """
    Linear Runtime of the Scheduling
    """
    current_time = 0

    """
    As long as there exists at least one element in the original array,
    Priority Scheduling will keep running in loop
    """
    while len(processes) > 0:

        """
        To deal with more than one process with same priority level,
        the following array is created
        """
        processes_with_highest_priority = []

        """
        Retrieves current highest priority in the original array
        """
        highest_priority = max(processes, key=attrgetter("priority")).priority

        """
        To counter issues where the processes with
        the highest priority has not entered the queue yet
        """
        while len(processes_with_highest_priority) == 0:

            for process in processes:
                if (
                    process.priority == highest_priority
                    and process.arrival_time <= current_time
                ):
                    processes_with_highest_priority.append(process)

            """
            In case no process of the highest priority was found waiting in the queue,
            it will move to the priority one step lower
            """
            if len(processes_with_highest_priority) == 0:
                highest_priority -= 1

        """
        In case of more than one process with the same priority level,
        appyling FCFS algorithm
        """
        process_to_execute = min(
            processes_with_highest_priority, key=attrgetter("arrival_time")
        )
        k = processes.index(process_to_execute)

        """
        Calculating arrival time and turn around time of the executed process
        and removing it from the original array
        """
        process_to_execute.waiting_time = current_time - process_to_execute.arrival_time
        process_to_execute.turn_around_time = (
            process_to_execute.waiting_time + process_to_execute.burst_time
        )
        executed_processes.append(process_to_execute)

        current_time += processes[k].burst_time
        del processes[k]

    """
    Printing Process names in executed order, along with waiting time
    and turn around time
    """
    print("Process Name\tWaiting Time\t Turn Around Time")
    for process in executed_processes:
        print(
            process.process_name
            + "\t\t"
            + str(process.waiting_time)
            + "\t\t"
            + str(process.turn_around_time)
        )
