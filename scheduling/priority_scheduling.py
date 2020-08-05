"""
A Priority Scheduling algorithm

https://en.wikipedia.org/wiki/Scheduling_(computing)#Priority_scheduling
"""

from operator import attrgetter
from typing import List


class Process:
    def __init__(self, name: str, arrival_time: int, burst_time: int, priority: int):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time: int = 0
        self.turn_around_time: int = 0

    def __repr__(self):
        """
        >>> Process("Name", 1, 2, 3)
        Process(name='Name', arrival_time=1, burst_time=2, priority=3)
        """
        return (
            f"{self.__class__.__qualname__}(name='{self.name}', "
            f"arrival_time={self.arrival_time}, burst_time={self.burst_time}, "
            f"priority={self.priority})"
        )

    def __str__(self):
        r"""
        >>> str(Process("Name", 1, 2, 3))
        'Name\t\t0\t\t0'
        """
        return f"{self.name}\t\t{self.waiting_time}\t\t{self.turn_around_time}"


def create_processes(number_of_processes: int = 0) -> List[Process]:
    def get_data_for_process(process_number: int) -> Process:
        return Process(
            name=str(
                input(f"Enter Name of process {process_number}: ").strip()
                or process_number
            ),
            arrival_time=int(input("Enter Arrival time: ").strip() or process_number),
            burst_time=int(input("Enter Burst time: ").strip() or process_number),
            priority=int(input("Enter Priority: ").strip() or process_number),
        )

    number_of_processes = number_of_processes or int(
        input("Enter number of processes: ").strip() or 3
    )
    return [get_data_for_process(i) for i in range(number_of_processes)]


def priority_schedule(processes: List[Process]) -> List[Process]:
    """
    >>> [process.name for process in priority_schedule([
    ...     Process("a", 1, 2, 3),
    ...     Process("b", 3, 2, 1),
    ...     Process("c", 2, 2, 2),
    ... ])]
    [a, b, c]

    Executed processes from the original array will be deleted
    and will be appended to the array below
    """
    executed_processes = []

    """
    Linear Runtime of the Scheduling
    """
    current_time = 0

    """
    As long as there exists atleast one element in the original array,
    Priority Scheduling will keep running in loop
    """
    while len(processes) > 0:

        """
        To deal with more than one process with same priority level,
        the following array is created
        """
        processes_with_highest_priority: List[Process] = []

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

    return executed_processes


if __name__ == "__main__":
    print("Priority schedule for processes:")
    processes = create_processes()
    print("\n".join(repr(process) for process in processes))

    print("\nPriority schedule:")
    print("Process Name\tWaiting Time\t Turn Around Time")
    print("\n".join(str(process) for process in processes))
