"""

This is a Python implementation for questions involving task assignments between people.
Here Bitmasking and DP are used for solving this.

Question :-
We have N tasks and M people. Each person in M can do only certain of these tasks. Also
a person can do only one task and a task is performed only by one person.
Find the total no of ways in which the tasks can be distributed.
"""

from collections import defaultdict


class AssignmentUsingBitmask:
    def __init__(self, task_performed, total):
        self.total_tasks = total  # total no of tasks (N)

        # DP table will have a dimension of (2^M)*N
        # initially all values are set to -1
        self.dp = [
            [-1 for i in range(total + 1)] for j in range(2 ** len(task_performed))
        ]

        self.task = defaultdict(list)  # stores the list of persons for each task

        # final_mask is used to check if all persons are included by setting all bits
        # to 1
        self.final_mask = (1 << len(task_performed)) - 1

    def count_ways_until(self, mask, task_no):
        # if mask == self.finalmask all persons are distributed tasks, return 1
        if mask == self.final_mask:
            return 1

        # if not everyone gets the task and no more tasks are available, return 0
        if task_no > self.total_tasks:
            return 0

        # if case already considered
        if self.dp[mask][task_no] != -1:
            return self.dp[mask][task_no]

        # Number of ways when we don't this task in the arrangement
        total_ways_util = self.count_ways_until(mask, task_no + 1)

        # now assign the tasks one by one to all possible persons and recursively
        # assign for the remaining tasks.
        if task_no in self.task:
            for p in self.task[task_no]:
                # if p is already given a task
                if mask & (1 << p):
                    continue

                # assign this task to p and change the mask value. And recursively
                # assign tasks with the new mask value.
                total_ways_util += self.count_ways_until(mask | (1 << p), task_no + 1)

        # save the value.
        self.dp[mask][task_no] = total_ways_util

        return self.dp[mask][task_no]

    def count_no_of_ways(self, task_performed):
        # Store the list of persons for each task
        for i in range(len(task_performed)):
            for j in task_performed[i]:
                self.task[j].append(i)

        # call the function to fill the DP table, final answer is stored in dp[0][1]
        return self.count_ways_until(0, 1)


if __name__ == "__main__":
    total_tasks = 5  # total no of tasks (the value of N)

    # the list of tasks that can be done by M persons.
    task_performed = [[1, 3, 4], [1, 2, 5], [3, 4]]
    print(
        AssignmentUsingBitmask(task_performed, total_tasks).count_no_of_ways(
            task_performed
        )
    )
    """
    For the particular example the tasks can be distributed as
    (1,2,3), (1,2,4), (1,5,3), (1,5,4), (3,1,4),
    (3,2,4), (3,5,4), (4,1,3), (4,2,3), (4,5,3)
    total 10
    """
