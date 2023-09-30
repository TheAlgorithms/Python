class FibonacciHeapNode:
    def __init__(self, key):
        """
        Initialize a Fibonacci Heap Node with a given key.

        Args:
            key: The key associated with the node.
        """
        self.key = key  # The value associated with the node
        self.degree = 0  # Number of children
        self.parent = None  # Parent node in the heap
        self.child = None  # One of the children (a pointer to any child)
        self.marked = False  # Flag indicating whether the node has lost a child
        self.next = self  # Next node in the circular doubly linked list
        self.prev = self  # Previous node in the circular doubly linked list


class FibonacciHeap:
    def __init__(self):
        """
        Initialize an empty Fibonacci Heap.
        """
        self.min_node = None  # Pointer to the minimum node in the heap
        self.num_nodes = 0  # Number of nodes in the heap

    def insert(self, key):
        """
        Insert a new node with the given key into the Fibonacci Heap.

        Args:
            key: The key to be inserted.
        """
        new_node = FibonacciHeapNode(key)
        if self.min_node is None:
            # If the heap is empty, set the new node as the minimum node
            self.min_node = new_node
        else:
            # Insert new node into the root list and update minimum node if necessary
            new_node.next = self.min_node
            new_node.prev = self.min_node.prev
            self.min_node.prev.next = new_node
            self.min_node.prev = new_node
            if key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def extract_min(self):
        """
        Extract and return the node with the minimum key from the Fibonacci Heap.
        """
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                # Move children of the minimum node to the root list
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
            # Remove the minimum node from the root list
            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev
            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()  # Consolidate the heap to ensure proper structure
            self.num_nodes -= 1
        return min_node.key

    def _consolidate(self):
        """
        Consolidate the Fibonacci Heap by combining trees with the same degree.
        """
        max_degree = int(self.num_nodes**0.5)
        degrees = [None] * (max_degree + 1)  # Dynamically resize the degrees list

        current = self.min_node
        unvisited = [current]
        while True:
            current = current.next
            if current == self.min_node:
                break
            unvisited.append(current)

        for node in unvisited:
            degree = node.degree
            while degrees[degree] is not None:
                other = degrees[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                degrees[degree] = None
                degree += 1
            degrees[degree] = node

    def _link(self, child, parent):
        """
        Link two nodes in the Fibonacci Heap.
        The node with the smaller key becomes the child of the other.

        Args:
            child: The node to be linked as a child.
            parent: The node to be linked as a parent.
        """
        child.next = child.prev = child
        child.parent = parent
        if parent.child is None:
            parent.child = child
        else:
            child.next = parent.child
            child.prev = parent.child.prev
            parent.child.prev.next = child
            parent.child.prev = child
        parent.degree += 1
        child.marked = False

    def decrease_key(self, node, new_key):
        """
        Decrease the key of a node in the Fibonacci Heap.

        Args:
            node: The node whose key should be decreased.
            new_key: The new key for the node.
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, child, parent):
        """
        Cut a node from its parent in the Fibonacci Heap.

        Args:
            child: The child node to be cut.
            parent: The parent node from which the child is cut.
        """
        if child.next == child:
            parent.child = None
        else:
            child.next.prev = child.prev
            child.prev.next = child.next
            if parent.child == child:
                parent.child = child.next
        parent.degree -= 1
        self.min_node.prev.next = child
        child.prev = self.min_node.prev
        self.min_node.prev = child
        child.next = self.min_node
        child.parent = None
        child.marked = False

    def _cascading_cut(self, node):
        """
        Perform cascading cuts on a node in the Fibonacci Heap.

        Args:
            node: The node on which cascading cuts are performed.
        """
        if (parent := node.parent) is not None:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def delete(self, node):
        """
        Delete a node from the Fibonacci Heap.

        Args:
            node: The node to be deleted.
        """
        self.decrease_key(node, float("-inf"))
        self.extract_min()


if __name__ == "__main__":
    # Example usage
    fibonacci_heap = FibonacciHeap()

    fibonacci_heap.insert(5)
    fibonacci_heap.insert(3)
    fibonacci_heap.insert(8)
    fibonacci_heap.insert(2)

    print("Extracted minimum:", fibonacci_heap.extract_min())

    node_to_decrease = fibonacci_heap.min_node.child
    fibonacci_heap.decrease_key(node_to_decrease, 1)

    print("Extracted minimum:", fibonacci_heap.extract_min())
