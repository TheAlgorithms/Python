class Node:
    """A node in the Fibonacci heap.

    Each node maintains references to its key, degree (number of children),
    marked status, parent, child, and circular linked list references (left/right).

    Attributes:
        key: The key value stored in the node
        degree: Number of children of the node
        marked: Boolean indicating if the node is marked
        parent: Reference to parent node
        child: Reference to one child node
        left: Reference to left sibling in circular list
        right: Reference to right sibling in circular list

    Examples:
        >>> node = Node(5)
        >>> node.key
        5
        >>> node.degree
        0
        >>> node.marked
        False
        >>> node.left == node
        True
        >>> node.right == node
        True
    """

    def __init__(self, key) -> None:
        self.key = key or None
        self.degree = 0
        self.marked = False
        self.parent = Node(None)
        self.child = Node(None)
        self.left = self
        self.right = self


class FibonacciHeap:
    """Implementation of a Fibonacci heap using circular linked lists.

    A Fibonacci heap is a collection of trees satisfying the min-heap property.
    This implementation uses circular linked lists for both the root list and
    child lists of nodes.

    Attributes:
        min_node: Reference to the node with minimum key
        total_nodes: Total number of nodes in the heap

    Reference: Introduction to Algorithms (CLRS) Chapter 19
    https://en.wikipedia.org/wiki/Fibonacci_heap

    Examples:
        >>> heap = FibonacciHeap()
        >>> heap.is_empty()
        True
        >>> node = heap.insert(3)
        >>> node.key
        3
        >>> node2 = heap.insert(2)
        >>> node2.key
        2
        >>> heap.find_min()
        2
        >>> heap.extract_min()
        2
        >>> heap.find_min()
        3
    """

    def __init__(self) -> None:
        self.min_node = Node(None)
        self.total_nodes = 0

    def insert(self, key) -> Node:
        """Insert a new key into the heap.

        Args:
            key: The key value to insert

        Returns:
            Node: The newly created node

        Examples:
            >>> heap = FibonacciHeap()
            >>> node = heap.insert(5)
            >>> node.key
            5
            >>> heap.find_min()
            5
            >>> node2 = heap.insert(3)
            >>> node2.key
            3
            >>> heap.find_min()
            3
        """
        new_node = Node(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._insert_into_circular_list(self.min_node, new_node)
            if new_node.key < self.min_node.key:
                self.min_node = new_node
        self.total_nodes += 1
        return new_node

    def _insert_into_circular_list(self, base_node, node_to_insert) -> Node:
        """Insert node into circular linked list.

        Args:
            base_node: The reference node in the circular list
            node_to_insert: The node to insert into the list

        Returns:
            Node: The base node

        Examples:
            >>> heap = FibonacciHeap()
            >>> node1 = Node(1)
            >>> node2 = Node(2)
            >>> result = heap._insert_into_circular_list(node1, node2)
            >>> result == node1
            True
            >>> node1.right == node2
            True
            >>> node2.left == node1
            True
        """
        if base_node.key is None:
            return node_to_insert

        node_to_insert.right = base_node.right
        node_to_insert.left = base_node
        base_node.right.left = node_to_insert
        base_node.right = node_to_insert
        return base_node

    def extract_min(self) -> Node:
        """Remove and return the minimum key from the heap.

        This operation removes the node with the minimum key from the heap,
        adds all its children to the root list, and consolidates the heap
        to maintain the Fibonacci heap properties. This is one of the more
        complex operations with amortized time complexity of O(log n).

        Returns:
            Node: The minimum key value that was removed,
            or None if the heap is empty

        Example:
            >>> heap = FibonacciHeap()
            >>> node1 = heap.insert(3)
            >>> node2 = heap.insert(1)
            >>> node3 = heap.insert(2)
            >>> heap.extract_min()  # Removes and returns 1
            1
            >>> heap.extract_min()  # Removes and returns 2
            2
            >>> heap.extract_min()  # Removes and returns 3
            3
            >>> heap.extract_min()  # Heap is now empty

        Note:
            This operation may trigger heap consolidation to maintain
            the Fibonacci heap properties after removal of the minimum node.
        """
        if self.min_node is None:
            return Node(None)

        min_node = self.min_node

        if min_node.child:
            current_child = min_node.child
            last_child = min_node.child.left
            while True:
                next_child = current_child.right
                self._insert_into_circular_list(self.min_node, current_child)
                current_child.parent.key = None
                if current_child == last_child:
                    break
                current_child = next_child

        min_node.left.right = min_node.right
        min_node.right.left = min_node.left

        if min_node == min_node.right:
            self.min_node.key = None
        else:
            self.min_node = min_node.right
            self._consolidate()

        self.total_nodes -= 1
        return min_node.key

    def _consolidate(self):
        """Consolidate the heap after removing the minimum node.

        This internal method maintains the Fibonacci heap properties by combining
        trees of the same degree until no two roots have the same degree. This
        process is key to maintaining the efficiency of the data structure.

        The consolidation process works by:
        1. Creating a temporary array indexed by tree degree
        2. Processing each root node and combining trees of the same degree
        3. Reconstructing the root list and finding the new minimum

        Time complexity: O(log n) amortized

        Note:
            This is an internal method called by extract_min and should not be
            called directly from outside the class.
        """
        max_degree = int(self.total_nodes**0.5) + 1
        degree_table = [Node(None)] * max_degree

        roots = []
        if self.min_node:
            current_root = self.min_node
            while True:
                roots.append(current_root)
                if current_root.right == self.min_node:
                    break
                current_root = current_root.right

        for current_root in roots:
            root_node = current_root
            current_degree = root_node.degree

            while degree_table[current_degree] is not None:
                other_root = degree_table[current_degree]
                if root_node.key > other_root.key:
                    root_node, other_root = other_root, root_node

                other_root.left.right = other_root.right
                other_root.right.left = other_root.left

                if root_node.child.key is None:
                    root_node.child = other_root
                    other_root.right = other_root
                    other_root.left = other_root
                else:
                    self._insert_into_circular_list(root_node.child, other_root)

                other_root.parent = root_node
                root_node.degree += 1
                other_root.marked = False

                degree_table[current_degree] = Node(None)
                current_degree += 1

            degree_table[current_degree] = root_node

        self.min_node.key = None
        for degree in range(max_degree):
            if degree_table[degree] is not None and (
                self.min_node is None or (degree_table[degree] < self.min_node.key)
            ):
                self.min_node = degree_table[degree]

    def decrease_key(self, node, new_key):
        """Decrease the key value of a given node.

        This operation updates the key of a node to a new, smaller value and
        maintains the min-heap property by potentially cutting the node from
        its parent and performing cascading cuts up the tree.

        Args:
            node: The node whose key should be decreased
            new_key: The new key value, must be smaller than the current key

        Example:
            >>> heap = FibonacciHeap()
            >>> node1 = heap.insert(5)
            >>> heap.decrease_key(node, 3)
            >>> node.key
            3
            >>> heap.find_min()
            3
            >>> heap.decrease_key(node, 1)
            >>> node.key
            1
            >>> heap.find_min()
            1
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")

        node.key = new_key
        parent_node = node.parent

        if parent_node.key is not None and node.key < parent_node.key:
            self._cut(node, parent_node)
            self._cascading_cut(parent_node)

        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, child_node, parent_node):
        """Cut a node from its parent and add it to the root list.

        This is a helper method used in decrease_key operations. When a node's key
        becomes smaller than its parent's key, it needs to be cut from its parent
        and added to the root list to maintain the min-heap property.

        Args:
            child_node: The node to be cut from its parent
            parent_node: The parent node from which to cut

        Note:
            This is an internal method that maintains heap properties during
            decrease_key operations. It should not be called directly from
            outside the class.
        """
        if child_node.right == child_node:
            parent_node.child = Node(None)
        else:
            parent_node.child = child_node.right
            child_node.right.left = child_node.left
            child_node.left.right = child_node.right

        parent_node.degree -= 1

        self._insert_into_circular_list(self.min_node, child_node)
        child_node.parent = Node(None)
        child_node.marked = False

    def _cascading_cut(self, current_node) -> None:
        """Perform cascading cut operation.

        Args:
            current_node: The node to start cascading cut from
        """
        if (parent_node := current_node.parent) is not None:
            if not current_node.marked:
                current_node.marked = True
            else:
                self._cut(current_node, parent_node)
                self._cascading_cut(parent_node)

    def delete(self, node) -> None:
        """Delete a node from the heap.

        This operation removes a given node from the heap by first decreasing
        its key to negative infinity (making it the minimum) and then extracting
        the minimum.

        Args:
            node: The node to be deleted from the heap

        Example:
            >>> heap = FibonacciHeap()
            >>> node1 = heap.insert(3)
            >>> node2 = heap.insert(2)
            >>> heap.delete(node1)
            >>> heap.find_min()
            2
            >>> heap.total_nodes
            1

        Note:
            This operation has an amortized time complexity of O(log n)
            as it combines decrease_key and extract_min operations.
        """
        self.decrease_key(node, float("-inf"))
        self.extract_min()

    def find_min(self) -> float:
        """Return the minimum key without removing it from the heap.

        This operation provides quick access to the minimum key in the heap
        without modifying the heap structure.

        Returns:
            float | None: The minimum key value, or None if the heap is empty

        Example:
            >>> heap = FibonacciHeap()
            >>> heap.find_min() is None
            True
            >>> node1 = heap.insert(3)
            >>> heap.find_min()
            3
        """
        return self.min_node.key if self.min_node else Node(None)

    def is_empty(self) -> bool:
        """Check if heap is empty.

        Returns:
            bool: True if heap is empty, False otherwise

        Examples:
            >>> heap = FibonacciHeap()
            >>> heap.is_empty()
            True
            >>> node = heap.insert(1)
            >>> heap.is_empty()
            False
        """
        return self.min_node.key is None

    def merge(self, other_heap) -> None:
        """Merge another Fibonacci heap into this one.

        This operation combines two Fibonacci heaps by concatenating their
        root lists and updating the minimum pointer if necessary. The other
        heap is effectively consumed in this process.

        Args:
            other_heap: Another FibonacciHeap instance to merge into this one

        Example:
            >>> heap1 = FibonacciHeap()
            >>> node1 = heap1.insert(3)
            >>> heap2 = FibonacciHeap()
            >>> node2 = heap2.insert(2)
            >>> heap1.merge(heap2)
            >>> heap1.find_min()
            2
            >>> heap1.total_nodes
            2
        """
        if other_heap.min_node.key is None:
            return
        if self.min_node.key is None:
            self.min_node = other_heap.min_node
        else:
            self.min_node.right.left = other_heap.min_node.left
            other_heap.min_node.left.right = self.min_node.right
            self.min_node.right = other_heap.min_node
            other_heap.min_node.left = self.min_node

            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node

        self.total_nodes += other_heap.total_nodes


if __name__ == "__main__":
    import doctest

    doctest.testmod()
