"""
Given a list of tasks, each with a deadline and reward, calculate which tasks can be
completed to yield the maximum reward.  Each task takes one unit of time to complete,
and we can only work on one task at a time.  Once a task has passed its deadline, it
can no longer be scheduled.

Example :
tasks_info = [(4, 20), (1, 10), (1, 40), (1, 30)]
max_tasks will return (2, [2, 0]) -
Scheduling these tasks would result in a reward of 40 + 20

This problem can be solved using the concept of "GREEDY ALGORITHM".
Time Complexity - O(n log n)
https://medium.com/@nihardudhat2000/job-sequencing-with-deadline-17ddbb5890b5
"""
from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Task:
    task_id: int
    deadline: int
    reward: int


def max_tasks(tasks_info: list[tuple[int, int]]) -> list[int]:
    """
    Create a list of Task objects that are sorted so the highest rewards come first.
    Return a list of those task ids that can be completed before i becomes too high.
    >>> max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)])
    [2, 0]
    >>> max_tasks([(1, 10), (2, 20), (3, 30), (2, 40)])
    [3, 2]
    >>> max_tasks([(9, 10)])
    [0]
    >>> max_tasks([(-9, 10)])
    []
    >>> max_tasks([])
    []
    >>> max_tasks([(0, 10), (0, 20), (0, 30), (0, 40)])
    []
    >>> max_tasks([(-1, 10), (-2, 20), (-3, 30), (-4, 40)])
    []
    """
    tasks = sorted(
        (
            Task(task_id, deadline, reward)
            for task_id, (deadline, reward) in enumerate(tasks_info)
        ),
        key=attrgetter("reward"),
        reverse=True,
    )
    return [task.task_id for i, task in enumerate(tasks, start=1) if task.deadline >= i]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)]) = }")
    print(f"{max_tasks([(1, 10), (2, 20), (3, 30), (2, 40)]) = }")
