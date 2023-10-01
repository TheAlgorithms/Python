class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.marked = False
        self.degree = 0
        self.next = self
        self.prev = self


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key):
        new_node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def extract_min(self):
        min_node = self.min_node
        if min_node:
            if min_node.child:
                child = min_node.child
                while True:
                    next_child = child.next
                    child.prev = min_node.prev
                    child.next = min_node.next
                    min_node.prev.next = child
                    min_node.next.prev = child
                    if next_child == min_node.child:
                        break
                    child = next_child
                min_node.child = None
            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev
            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()
            self.num_nodes -= 1
        return min_node.key if min_node else None

    def _link(self, min1, min2):
        min1.next.prev = min2
        min2.next.prev = min1
        min1.next, min2.next = min2.next, min1.next
        if min2.key < min1.key:
            min1.key, min2.key = min2.key, min1.key
        if not min1.child:
            min1.child = min2
        else:
            child = min1.child
            while child.next != min1.child:
                child = child.next
            child.next = min2
            min2.prev = child
        min2.parent = min1
        min1.degree += 1
        min2.marked = False

    def _consolidate(self):
        max_degree = int(self.num_nodes**0.5) + 1
        degree_list = [None] * max_degree
        nodes = [self.min_node]
        current = self.min_node.next
        while current != self.min_node:
            nodes.append(current)
            current = current.next
        for node in nodes:
            degree = node.degree
            while degree_list[degree]:
                other = degree_list[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(node, other)
                degree_list[degree] = None
                degree += 1
            degree_list[degree] = node
        self.min_node = None
        for node in degree_list:
            if node:
                if self.min_node is None:
                    self.min_node = node
                elif node.key < self.min_node.key:
                    self.min_node = node


# Example usage:
fib_heap = FibonacciHeap()
fib_heap.insert(5)
fib_heap.insert(2)
fib_heap.insert(9)
fib_heap.insert(1)
print(fib_heap.extract_min())  # Output: 1
print(fib_heap.extract_min())  # Output: 2
