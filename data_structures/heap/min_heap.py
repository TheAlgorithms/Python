# Min heap data structure
# with decrease key functionality - in O(log(n)) time


class Node:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.val})"

    def __lt__(self, other):
        return self.val < other.val


class MinHeap:
    """
    >>> r = Node("R", -1)
    >>> b = Node("B", 6)
    >>> a = Node("A", 3)
    >>> x = Node("X", 1)
    >>> e = Node("E", 4)
    >>> print(b)
    Node(B, 6)
    >>> myMinHeap = MinHeap([r, b, a, x, e])
    >>> myMinHeap.decrease_key(b, -17)
    >>> print(b)
    Node(B, -17)
    >>> myMinHeap["B"]
    -17
    """

    def __init__(self, array):
        self.idx_of_element = {}
        self.heap_dict = {}
        self.heap = self.build_heap(array)

    def __getitem__(self, key):
        return self.get_value(key)

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        return idx * 2 + 2

    def get_value(self, key):
        return self.heap_dict[key]

    def build_heap(self, array):
        last_idx = len(array) - 1
        start_from = self.get_parent_idx(last_idx)

        for idx, i in enumerate(array):
            self.idx_of_element[i] = idx
            self.heap_dict[i.name] = i.val

        for i in range(start_from, -1, -1):
            self.sift_down(i, array)
        return array

    # this is min-heapify method
    def sift_down(self, idx, array):
        while True:
            l = self.get_left_child_idx(idx)  # noqa: E741
            r = self.get_right_child_idx(idx)

            smallest = idx
            if l < len(array) and array[l] < array[idx]:
                smallest = l
            if r < len(array) and array[r] < array[smallest]:
                smallest = r

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                (
                    self.idx_of_element[array[idx]],
                    self.idx_of_element[array[smallest]],
                ) = (
                    self.idx_of_element[array[smallest]],
                    self.idx_of_element[array[idx]],
                )
                idx = smallest
            else:
                break

    def sift_up(self, idx):
        p = self.get_parent_idx(idx)
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            p = self.get_parent_idx(idx)

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
        self.sift_down(0, self.heap)
        return x

    def insert(self, node):
        self.heap.append(node)
        self.idx_of_element[node] = len(self.heap) - 1
        self.heap_dict[node.name] = node.val
        self.sift_up(len(self.heap) - 1)

    def is_empty(self):
        return True if len(self.heap) == 0 else False

    def decrease_key(self, node, new_value):
        assert (
            self.heap[self.idx_of_element[node]].val > new_value
        ), "newValue must be less that current value"
        node.val = new_value
        self.heap_dict[node.name] = new_value
        self.sift_up(self.idx_of_element[node])


# USAGE

r = Node("R", -1)
b = Node("B", 6)
a = Node("A", 3)
x = Node("X", 1)
e = Node("E", 4)

# Use one of these two ways to generate Min-Heap

# Generating Min-Heap from array
my_min_heap = MinHeap([r, b, a, x, e])

# Generating Min-Heap by Insert method
# myMinHeap.insert(a)
# myMinHeap.insert(b)
# myMinHeap.insert(x)
# myMinHeap.insert(r)
# myMinHeap.insert(e)

# Before
print("Min Heap - before decrease key")
for i in my_min_heap.heap:
    print(i)

print("Min Heap - After decrease key of node [B -> -17]")
my_min_heap.decrease_key(b, -17)

# After
for i in my_min_heap.heap:
    print(i)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
