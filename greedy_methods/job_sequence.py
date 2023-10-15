"""
Given a list of tasks, each with a deadline and reward,
The maximum number of tasks that can be scheduled to maximize reward.
We can only complete one task at a time, and each task takes 1 unit
of time to complete. Once a task has passed its deadline, it can no
longer be scheduled.

Example :
tasks_info = [(4, 20), (1, 10), (1, 40), (1, 30)]
max_tasks will return (2, [2, 0]) -
which is by scheduling the tasks with rewards 40, 20

This problem can be solved using the concept of "GREEDY ALGORITHM".
Time Complexity - O(n log n)

URL : https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A648%2F1*fCm4EwGIm_KFvHrniNR_yw.jpeg&tbnid=YzfEiVyu7FIWQM&vet=12ahUKEwjFi5i2rPeBAxV7a2wGHbghCd8QMygCegQIARBh..i&imgrefurl=https%3A%2F%2Fmedium.com%2F%40nihardudhat2000%2Fjob-sequencing-with-deadline-17ddbb5890b5&docid=wcDisrtMy41SsM&w=648&h=328&q=job%20sequence&client=firefox-b-d&ved=2ahUKEwjFi5i2rPeBAxV7a2wGHbghCd8QMygCegQIARBh

We iterate over the tasks array once, sorting it in descending order of reward.
Then we iterate over the sorted tasks array once more, scheduling each
task if its deadline is greater than the current time.The greedy choice at
each point is to either schedule the current task if its deadline is greater
than the current time, or skip it otherwise.
"""
from typing import Any
from dataclasses import dataclass


@dataclass
class Task:
    task_id: Any
    deadline: int
    reward: int

def max_tasks(tasks_info: list[tuple[int, int]]) -> list:
    """
    >>> max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)])
    [2, 0]
    >>> max_tasks([(1, 10), (2, 20), (3, 30), (2, 40)])
    [3, 2]

    """
    tasks = [Task(i, d, p) for i, (d, p) in enumerate(tasks_info)]

    tasks.sort(key=lambda task: task.reward, reverse=True)

    schedule = [
        task.task_id
        for current_time, task in enumerate(tasks, start=1)
        if task.deadline >= current_time
    ]

    return schedule


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)]))
