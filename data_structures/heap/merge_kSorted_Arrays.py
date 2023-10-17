from queue import PriorityQueue

class Node:
    def __init__(self, data, row, col):
        self.data = data
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.data < other.data


def merge_k_sorted_arrays(k_arrays):
    pq = PriorityQueue()

    # Step 1: Insert the first element of all arrays into the priority queue
    for i in range(len(k_arrays)):
        if k_arrays[i]:  # Check if array is not empty
            pq.put(Node(k_arrays[i][0], i, 0))

    ans = []

    # Step 2: Process elements from the priority queue
    while not pq.empty():
        temp = pq.get()
        ans.append(temp.data)

        if temp.col + 1 < len(k_arrays[temp.row]):
            pq.put(Node(k_arrays[temp.row][temp.col + 1], temp.row, temp.col + 1))

    return ans


# Example usage
k_arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
print(merge_k_sorted_arrays(k_arrays))
