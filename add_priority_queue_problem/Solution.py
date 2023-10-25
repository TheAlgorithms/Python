import heapq

def process_tasks(tasks):
    # Create a priority queue using a min-heap
    priority_queue = []
    for task in tasks:
        heapq.heappush(priority_queue, (task[1], task[0]))

    # Process tasks in priority order
    while priority_queue:
        priority, task_name = heapq.heappop(priority_queue)
        print(f"Processing {task_name} with priority {priority}")

# Example usage:
tasks = [("Task1", 3), ("Task2", 1), ("Task3", 2), ("Task4", 1)]
process_tasks(tasks)
