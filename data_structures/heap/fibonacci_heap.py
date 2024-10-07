class Node:
    def __init__(self, key):
        self.key = key  # The key value of the node
        self.degree = 0  # The degree of the node (number of children)
        self.parent = None  # Pointer to the parent node
        self.child = None  # Pointer to the child node
        self.is_marked = False  # Indicates if the node is marked
        self.next = self  # Pointer to the next node in the circular list
        self.prev = self  # Pointer to the previous node in the circular list


class FibonacciHeap:
    def __init__(self):
        self.min_node = None  # Pointer to the minimum node
        self.num_nodes = 0  # Number of nodes in the heap

    def insert(self, key):
        """Insert a new node with the given key."""
        new_node = Node(key)
        self._insert_to_root_list(new_node)
        if self.min_node is None or key < self.min_node.key:
            self.min_node = new_node
        self.num_nodes += 1

    def _insert_to_root_list(self, node):
        """Insert a node to the root list of the heap."""
        if self.min_node is None:
            self.min_node = node
        else:
            # Add node to the root list
            node.prev = self.min_node.prev
            node.next = self.min_node
            self.min_node.prev.next = node
            self.min_node.prev = node

    def extract_min(self):
        """Remove and return the node with the minimum key."""
        min_node = self.min_node
        if min_node is not None:
            # Remove min_node from the root list
            if min_node.child is not None:
                # Add children of min_node to the root list
                child = min_node.child
                while True:
                    next_child = child.next
                    self._insert_to_root_list(child)
                    child.parent = None
                    if next_child == min_node.child:
                        break
                    child = next_child

            # Remove min_node from root list
            if min_node == min_node.next:
                self.min_node = None  # Heap is now empty
            else:
                min_node.prev.next = min_node.next
                min_node.next.prev = min_node.prev
                self.min_node = min_node.next

            self.num_nodes -= 1
            if self.min_node is not None:
                self._consolidate()
        return min_node.key if min_node else None

    def _consolidate(self):
        """Consolidate trees of equal degree in the root list."""
        degree_list = [None] * (self.num_nodes + 1)
        current = self.min_node
        nodes = []

        # Store all nodes in a list
        while True:
            nodes.append(current)
            current = current.next
            if current == self.min_node:
                break

        for node in nodes:
            degree = node.degree
            while degree_list[degree] is not None:
                other = degree_list[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                degree_list[degree] = None
                degree += 1
            degree_list[degree] = node

        self.min_node = None
        for node in degree_list:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                elif node.key < self.min_node.key:
                    self.min_node = node

    def _link(self, node1, node2):
        """Link node1 as a child of node2."""
        node1.prev.next = node1.next
        node1.next.prev = node1.prev
        node1.parent = node2
        if node2.child is None:
            node2.child = node1
            node1.next = node1
            node1.prev = node1
        else:
            # Insert node1 into the child list of node2
            node1.prev = node2.child.prev
            node1.next = node2.child
            node2.child.prev.next = node1
            node2.child.prev = node1
        node2.degree += 1
        node1.is_marked = False

    def decrease_key(self, node, new_key):
        """Decrease the key of a given node."""
        if new_key > node.key:
            raise ValueError("New key is greater than current key")

        node.key = new_key
        parent = node.parent

        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._insert_to_root_list(node)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, node, parent):
        """Cut the node from its parent and add it to the root list."""
        if node == parent.child:
            parent.child = node.next if node.next != node else None
        if parent.child is None:
            parent.degree -= 1
        else:
            parent.degree -= 1
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = self.min_node.prev
        node.next = self.min_node
        self.min_node.prev.next = node
        self.min_node.prev = node
        node.parent = None
        node.is_marked = False

    def delete(self, node):
        """Delete a node from the heap."""
        self.decrease_key(node, float("-inf"))  # Decrease the key to -infinity
        self.extract_min()  # Extract the minimum node

    def is_empty(self):
        """Check if the heap is empty."""
        return self.min_node is None

    def size(self):
        """Return the number of nodes in the heap."""
        return self.num_nodes

    def min(self):
        """Return the minimum key without removing it."""
        return self.min_node.key if self.min_node else None


# Example Usage
if __name__ == "__main__":
    fib_heap = FibonacciHeap()
    fib_heap.insert(10)
    fib_heap.insert(2)
    fib_heap.insert(5)
    fib_heap.insert(7)

    print("Minimum:", fib_heap.min())  # Output: Minimum: 2
    print("Extracted Min:", fib_heap.extract_min())  # Output: Extracted Min: 2
    print("New Minimum:", fib_heap.min())  # Output: New Minimum: 5
