"""

This is a Python implementation for questions involving task assignments between people.
Here Bitmasking and DP are used for solving this.

Question :-
We have N tasks and M people. Each person in M can do only certain of these tasks. Also
a person can do only one task and a task is performed only by one person.
Find the total no of ways in which the tasks can be distributed.
"""
from collections import defaultdict
from typing import List, Dict


class TaskAssignment:
    def __init__(self, task_performed: List[List[int]], total_tasks: int) -> None:
        """
        Initialize the TaskAssignment class.

        Parameters:
        task_performed (List[List[int]]): List of lists where each inner list represents
            the tasks that can be performed by a person.
        total_tasks (int): The total number of tasks to be assigned.
        """
        self.total_tasks = total_tasks
        self.dp = [
            [-1 for _ in range(total_tasks + 1)]
            for _ in range(1 << len(task_performed))
        ]
        self.task: Dict[int, List[int]] = defaultdict(list)
        self.final_mask: int = (1 << len(task_performed)) - 1

    def count_ways_until(self, mask: int, task_no: int) -> int:
        """
        Recursively count the number of ways to assign tasks to people.

        Parameters:
        mask (int): Bitmask representing the tasks assigned to people.
        task_no (int): The current task number being considered.

        Returns:
        int: The number of ways to assign tasks.
        """
        if mask == self.final_mask:
            return 1
        if task_no > self.total_tasks:
            return 0
        if self.dp[mask][task_no] != -1:
            return self.dp[mask][task_no]

        total_ways_util: int = self.count_ways_until(mask, task_no + 1)

        if task_no in self.task:
            for person in self.task[task_no]:
                if mask & (1 << person):
                    continue
                total_ways_util += self.count_ways_until(
                    mask | (1 << person), task_no + 1
                )

        self.dp[mask][task_no] = total_ways_util
        return self.dp[mask][task_no]

    def count_total_ways(self, task_performed: List[List[int]]) -> int:
        """
        Count the total number of ways to distribute tasks to people.

        Parameters:
        task_performed (List[List[int]]): List of lists where each inner list represents
            the tasks that can be performed by a person.

        Returns:
        int: The total number of ways to distribute tasks.
        """
        for person, tasks in enumerate(task_performed):
            for task in tasks:
                self.task[task].append(person)

        return self.count_ways_until(0, 1)


if __name__ == "__main__":
    total_tasks = 5
    task_performed = [[1, 3, 4], [1, 2, 5], [3, 4]]

    assignment = TaskAssignment(task_performed, total_tasks)
    total_ways = assignment.count_total_ways(task_performed)

    print("Total number of ways to distribute tasks:", total_ways)

    """
    For the particular example the tasks can be distributed as
    (1,2,3), (1,2,4), (1,5,3), (1,5,4), (3,1,4),
    (3,2,4), (3,5,4), (4,1,3), (4,2,3), (4,5,3)
    total 10
    """
