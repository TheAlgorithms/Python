class Node:
    def __init__(self, key: int) -> None:
        """
        Initialize a Fibonacci heap node.

        :param key: The key value of the node.
        """
        self.key = key
        self.degree = 0
        self.is_marked = False
        self.parent = None
        self.next = self  # Pointer to the next node in the circular list
        self.prev = self  # Pointer to the previous node in the circular list
        self.child = None  # Pointer to the first child node


class FibonacciHeap:
    def __init__(self) -> None:
        """
        Initialize a Fibonacci heap.
        """
        self.min_node = None  # Pointer to the minimum node
        self.num_nodes = 0  # Number of nodes in the heap

    def insert(self, key: int) -> None:
        """
        Insert a new key into the Fibonacci heap.

        :param key: The key value to be inserted.

        >>> heap = FibonacciHeap()
        >>> heap.insert(10)
        >>> heap.min_node.key
        10
        >>> heap.insert(5)
        >>> heap.min_node.key
        5
        """
        new_node = Node(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._insert_to_root_list(new_node)
            if new_node.key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def _insert_to_root_list(self, node: Node) -> None:
        """
        Insert a node into the root list of the Fibonacci heap.

        :param node: The node to be inserted.

        >>> heap = FibonacciHeap()
        >>> node1 = Node(10)
        >>> heap._insert_to_root_list(node1)
        >>> heap.min_node = node1
        >>> node2 = Node(5)
        >>> heap._insert_to_root_list(node2)
        >>> heap.min_node.next.key
        10
        """
        # Linking the new node into the root list
        node.prev = self.min_node.prev
        node.next = self.min_node
        self.min_node.prev.next = node
        self.min_node.prev = node

    def extract_min(self) -> int:
        """
        Extract the minimum key from the Fibonacci heap.

        :return: The minimum key in the heap.

        >>> heap = FibonacciHeap()
        >>> heap.insert(10)
        >>> heap.insert(5)
        >>> heap.extract_min()
        5
        >>> heap.extract_min()
        10
        >>> heap.extract_min()
        >>> heap.is_empty()
        True
        """
        if (min_node := self.min_node) is not None:
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
                # Remove min_node from root list
                min_node.prev.next = min_node.next
                min_node.next.prev = min_node.prev
                self.min_node = min_node.next  # Update min_node to next node
                self._consolidate()
            self.num_nodes -= 1
            return min_node.key
        return None

    def _consolidate(self) -> None:
        """
        Consolidate the trees in the Fibonacci heap.
        """
        if self.min_node is None:
            return

        # Create an array to hold the trees by degree
        max_degree = self.num_nodes
        degree_array = [None] * (max_degree + 1)

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
            while degree_array[degree] is not None:
                other = degree_array[degree]
                # Link the trees
                if node.key > other.key:
                    node, other = other, node
                self._link(node, other)
                degree_array[degree] = None
                degree += 1
            degree_array[degree] = node

        # Find the new minimum
        self.min_node = None
        for node in degree_array:
            if node is not None:
                if self.min_node is None or node.key < self.min_node.key:
                    self.min_node = node

    def _link(self, node1: Node, node2: Node) -> None:
        """
        Link two trees of equal degree.

        :param node1: The first node to link.
        :param node2: The second node to link.
        """
        # Linking logic
        if node1.key > node2.key:
            node1, node2 = node2, node1
        node2.prev.next = node2.next
        node2.next.prev = node2.prev
        node2.parent = node1
        if node1.child is None:
            node1.child = node2
            node2.next = node2
            node2.prev = node2
        else:
            self._insert_to_root_list(node2)
        node1.degree += 1
        node2.is_marked = False

    def decrease_key(self, node: Node, new_key: int) -> None:
        """
        Decrease the key of a given node.

        :param node: The node to decrease the key for.
        :param new_key: The new key value to set.

        >>> heap = FibonacciHeap()
        >>> heap.insert(10)
        >>> node = Node(20)
        >>> heap.insert(20)
        >>> heap.decrease_key(node, 5)
        >>> heap.min_node.key
        5
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        parent = node.parent

        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._insert_to_root_list(node)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, node: Node, parent: Node) -> None:
        """
        Cut a node from its parent.

        :param node: The node to cut.
        :param parent: The parent node.
        """
        # Remove node from the parent's child list
        if parent.child == node:
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

    def size(self) -> int:
        """
        Return the number of nodes in the Fibonacci heap.

        :return: The number of nodes in the heap.

        >>> heap = FibonacciHeap()
        >>> heap.size()
        0
        >>> heap.insert(10)
        >>> heap.size()
        1
        """
        return self.num_nodes

    def min(self) -> int:
        """
        Return the minimum key in the Fibonacci heap.

        :return: The minimum key.

        >>> heap = FibonacciHeap()
        >>> heap.insert(10)
        >>> heap.insert(5)
        >>> heap.min()
        5
        """
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
