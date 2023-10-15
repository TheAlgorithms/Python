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

We iterate over the tasks array once, sorting it in descending order of reward.
Then we iterate over the sorted tasks array once more, scheduling each
task if its deadline is greater than the current time.The greedy choice at
each point is to either schedule the current task if its deadline is greater
than the current time, or skip it otherwise.
"""


class Task:
    def __init__(self, id, deadline, reward):
        self.id = id
        self.deadline = deadline
        self.reward = reward


def max_tasks(tasks_info: list[tuple[int]]) -> int:
    """
    >>> max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)])
    (2, [2, 0])
    >>> max_tasks([(1, 10), (2, 20), (3, 30), (2, 40)])
    (2, [3, 2])
    """
    tasks = [Task(i, d, p) for i, (d, p) in enumerate(tasks_info)]

    tasks.sort(key=lambda task: task.reward, reverse=True)

    schedule = []
    current_time = 0

    for task in tasks:
        if task.deadline > current_time:
            schedule.append(task.id)
            current_time += 1

    return len(schedule), schedule


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)]))
