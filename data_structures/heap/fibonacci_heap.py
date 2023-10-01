class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.marked = False
        self.parent = None
        self.child = None
        self.prev = self
        self.next = self


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key):
        # Create a new node and initialize it with the given key
        new_node = FibonacciNode(key)

        # If the heap is empty, set the new node as the minimum
        if self.min_node is None:
            self.min_node = new_node
        else:
            # Insert the new node into the root list
            self._link(self.min_node, new_node)
            if key < self.min_node.key:
                self.min_node = new_node

        # Increment the number of nodes in the heap
        self.num_nodes += 1

    def _link(self, root1, root2):
        # Link two nodes together in the root list
        root1.next.prev = root2
        root2.next.prev = root1
        root1.next, root2.next = root2.next, root1.next
        root1.child = root2
        root2.parent = root1
        root1.degree += 1
        root2.marked = False

    def _consolidate(self):
        max_degree = int(self.num_nodes**0.5)
        nodes = [None] * (max_degree + 1)
        current = self.min_node

        while True:
            degree = current.degree
            next_node = current.next

            while nodes[degree] is not None:
                other = nodes[degree]
                if current.key > other.key:
                    current, other = other, current
                self._link(current, other)
                nodes[degree] = None
                degree += 1

            nodes[degree] = current
            current = next_node
            if current == self.min_node:
                break

        self.min_node = None
        for node in nodes:
            if node is not None:
                if self.min_node is None or node.key < self.min_node.key:
                    self.min_node = node

    def extract_min(self):
        if self.min_node is None:
            return None

        min_node = self.min_node
        if min_node.child is not None:
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

        min_node.prev.next = min_node.next
        min_node.next.prev = min_node.prev
        if min_node == min_node.next:
            self.min_node = None
        else:
            self.min_node = min_node.next
            self._consolidate()

        self.num_nodes -= 1
        return min_node.key


# Example usage:
fib_heap = FibonacciHeap()

fib_heap.insert(3)
fib_heap.insert(1)
fib_heap.insert(4)
fib_heap.insert(2)

print("Extracting min:", fib_heap.extract_min())  # Should print 1
print("Extracting min:", fib_heap.extract_min())  # Should print 2
