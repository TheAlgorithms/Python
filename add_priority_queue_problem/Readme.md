Problem:

You are given a list of tasks, each represented by a tuple (task_name, priority). You need to implement a function process_tasks(tasks) that processes these tasks in priority order. The tasks should be processed in such a way that tasks with higher priority are processed first. If two tasks have the same priority, process them in the order they appear in the list.

Implement the function process_tasks(tasks):

'''py

import heapq

def process_tasks(tasks):
    # Your code here
    pass

# Example usage:
tasks = [("Task1", 3), ("Task2", 1), ("Task3", 2), ("Task4", 1)]
process_tasks(tasks)

'''