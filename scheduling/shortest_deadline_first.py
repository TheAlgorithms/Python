"""
Earliest Deadline First (EDF) Scheduling Algorithm

This code implements the Earliest Deadline First (EDF)
scheduling algorithm, which schedules processes based on their deadlines.
If a process cannot meet its deadline, it is marked as "Idle."

Reference:
https://www.geeksforgeeks.org/
earliest-deadline-first-edf-cpu-scheduling-algorithm/

Author: Arunkumar
Date: 14th October 2023
"""


def earliest_deadline_first_scheduling(
    processes: list[tuple[str, int, int, int]]
) -> list[str]:
    """
    Perform Earliest Deadline First (EDF) scheduling.

    Args:
        processes (List[Tuple[str, int, int, int]]): A list of
        processes with their names,
        arrival times, deadlines, and execution times.

    Returns:
        List[str]: A list of process names in the order they are executed.

    Examples:
        >>> processes = [("A", 1, 5, 2), ("B", 2, 8, 3), ("C", 3, 4, 1)]
        >>> execution_order = earliest_deadline_first_scheduling(processes)
        >>> execution_order
        ['Idle', 'A', 'C', 'B']

    """
    result = []
    current_time = 0

    while processes:
        available_processes = [
            process for process in processes if process[1] <= current_time
        ]

        if not available_processes:
            result.append("Idle")
            current_time += 1
        else:
            next_process = min(
                available_processes, key=lambda tuple_values: tuple_values[2]
            )
            name, _, deadline, execution_time = next_process

            if current_time + execution_time <= deadline:
                result.append(name)
                current_time += execution_time
                processes.remove(next_process)
            else:
                result.append("Idle")
                current_time += 1

    return result


if __name__ == "__main__":
    processes = [("A", 1, 5, 2), ("B", 2, 8, 3), ("C", 3, 4, 1)]
    execution_order = earliest_deadline_first_scheduling(processes)
    for i, process in enumerate(execution_order):
        print(f"Time {i}: Executing process {process}")
