class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.marked = False
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
            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev
            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()
            self.num_nodes -= 1
        return min_node

    def _link(self, min_node, new_node):
        new_node.prev = min_node
        new_node.next = min_node.next
        min_node.next.prev = new_node
        min_node.next = new_node

    def _consolidate(self):
        max_degree = int(self.num_nodes ** 0.5) + 1
        degree_table = [None] * max_degree

        current = self.min_node
        nodes = []
        while True:
            nodes.append(current)
            current = current.next
            if current == self.min_node:
                break

        for node in nodes:
            degree = node.degree
            while degree_table[degree]:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(node, other)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        self.min_node = None
        for node in degree_table:
            if node:
                if self.min_node is None:
                    self.min_node = node
                elif node.key < self.min_node.key:
                    self.min_node = node

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than the current key.")
        node.key = new_key
        parent = node.parent
        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, child, parent):
        child.prev.next = child.next
        child.next.prev = child.prev
        parent.degree -= 1
        if parent.child == child:
            parent.child = child.next
        if parent.degree == 0:
            parent.child = None
        child.prev = self.min_node
        child.next = self.min_node.next
        self.min_node.next.prev = child
        self.min_node.next = child
        child.parent = None
        child.marked = False

    def _cascading_cut(self, node):
        parent = node.parent
        if parent:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

if __name__ == "__main__":
    fib_heap = FibonacciHeap()
    fib_heap.insert(5)
    fib_heap.insert(2)
    fib_heap.insert(9)
    fib_heap.insert(1)
    
    print(fib_heap.extract_min().key)  # Output: 1
