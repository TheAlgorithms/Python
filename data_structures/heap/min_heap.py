# Min head data structure
# with decrease key functionality - in O(log(n)) time


class MinHeap:
    def __init__(self, array):
        self.idx_of_element = {}
        self.heap = self.buildHeap(array)

    def getParentIdx(self, idx):
        return (idx - 1) // 2

    def getLeftChildIdx(self, idx):
        return idx * 2 + 1

    def getRightChildIdx(self, idx):
        return idx * 2 + 2

    def buildHeap(self, array):
        lastIdx = len(array) - 1
        startFrom = self.getParentIdx(lastIdx)

        for idx, i in enumerate(array):
            self.idx_of_element[i] = idx

        for i in range(startFrom, -1, -1):
            self.siftDown(i, array)
        return array

    # this is min-heapify method
    def siftDown(self, idx, array):
        while True:
            l = self.getLeftChildIdx(idx)
            r = self.getRightChildIdx(idx)

            smallest = idx
            if l < len(array) and array[l] < array[idx]:
                smallest = l
            if r < len(array) and array[r] < array[smallest]:
                smallest = r

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                self.idx_of_element[array[idx]], self.idx_of_element[
                    array[smallest]
                ] = (
                    self.idx_of_element[array[smallest]],
                    self.idx_of_element[array[idx]],
                )
                idx = smallest
            else:
                break

    def siftUp(self, idx):
        p = self.getParentIdx(idx)
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            p = self.getParentIdx(idx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0]], self.idx_of_element[self.heap[-1]] = (
            self.idx_of_element[self.heap[-1]],
            self.idx_of_element[self.heap[0]],
        )

        x = self.heap.pop()
        del self.idx_of_element[x]
        self.siftDown(0, self.heap)
        return x

    def insert(self, value):
        self.heap.append(value)
        self.idx_of_element[value] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1)

    def isEmpty(self):
        return True if len(self.heap) == 0 else False

    def decreaseKey(self, key, newValue):
        assert (
            self.heap[self.idx_of_element[key]].val > newValue
        ), "newValue must be less that current value"
        key.val = newValue
        self.siftUp(self.idx_of_element[key])


class Node:
    def __init__(self, val, name):
        self.val = val
        self.name = name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.val < other.val


## USAGE

r = Node(-1, "R")
b = Node(6, "B")
a = Node(3, "A")
x = Node(1, "X")
e = Node(4, "E")

arr = [r, b, a, x, e]

# Use one of these two ways to generate Min-Heap

# Generating Min-Heap from array
myMinHeap = MinHeap(arr)

# Generating Min-Heap by Insert method
# myMinHeap.insert(a)
# myMinHeap.insert(b)
# myMinHeap.insert(x)
# myMinHeap.insert(r)
# myMinHeap.insert(e)

# Before
print("Min Heap - before decrease key")
for i in myMinHeap.heap:
    print(i, i.val)

print("Min Heap - After decrease key of node [B -> -17]")
myMinHeap.decreaseKey(b, -17)

# After
for i in myMinHeap.heap:
    print(i, i.val)
