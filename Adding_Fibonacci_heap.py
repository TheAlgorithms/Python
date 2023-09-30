from typing import Any

class FibonacciHeapNode:
    def __init__(self, key: int):
        self.key = key
        self.degree = 0
        self.parent: Any = None
        self.child: Any = None
        self.left = self
        self.right = self
        self.mark = False

class FibonacciHeapPairing:
    def __init__(self):
        self.min: FibonacciHeapNode | None = None
        self.num_nodes: int = 0

    def insert(self, key: int):
        node = FibonacciHeapNode(key)
        if self.min is None:
            self.min = node
        else:
            self._insert_node(node)
            if node.key < self.min.key:
                self.min = node
        self.num_nodes += 1

    def _insert_node(self, node: FibonacciHeapNode):
        node.left = self.min
        node.right = self.min.right
        self.min.right = node
        node.right.left = node

   

class FibonacciHeap:
    def __init__(self):
        self.pairing_heap = FibonacciHeapPairing()

    def insert(self, key: int):
        self.pairing_heap.insert(key)

    def get_min(self):
        return self.pairing_heap.min.key if self.pairing_heap.min else None

  

if __name__ == "__main__":
    fib_heap = FibonacciHeap()
    fib_heap.insert(5)
    fib_heap.insert(2)
    fib_heap.insert(9)
    fib_heap.insert(1)

    print(fib_heap.get_min())  # Output: 1
