class MaxHeap:
    def __init__(self):
        self.items = [0] * 100
        self.size = 0

    def swap(self, a, b):
        self.items[a], self.items[b] = self.items[b], self.items[a]

    def heapify_up(self, index):
        while index > 0 and self.items[(index - 1) // 2] < self.items[index]:
            self.swap((index - 1) // 2, index)
            index = (index - 1) // 2

    def heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < self.size and self.items[left_child] > self.items[largest]:
            largest = left_child
        if right_child < self.size and self.items[right_child] > self.items[largest]:
            largest = right_child

        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)

    def insert(self, value):
        if self.size >= 100:
            print("Heap is full. Cannot insert.")
            return
        self.items[self.size] = value
        self.size += 1
        self.heapify_up(self.size - 1)

    def delete_max(self):
        if self.size == 0:
            print("Heap is empty. Cannot delete.")
            return -1
        deleted_item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down(0)
        return deleted_item

def heap_sort(arr):
    heap = MaxHeap()

    # Inserting elements into the max heap
    for i in range(len(arr)):
        heap.insert(arr[i])

    # Deleting elements from the max heap and storing them in sorted order
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = heap.delete_max()

    return arr

arr = [4, 10, 3, 5, 1]
arr = heap_sort(arr)

# Displaying sorted array
print("Sorted array:", arr)