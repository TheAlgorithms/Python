"""
Fibonacci Heap
A more efficient priority queue implementation that provides amortized time bounds
that are better than those of the binary and binomial heaps.
reference: https://en.wikipedia.org/wiki/Fibonacci_heap

Operations supported:
- Insert: O(1) amortized
- Find minimum: O(1)
- Delete minimum: O(log n) amortized
- Decrease key: O(1) amortized
- Merge: O(1)
"""

class Node:
    """
    A node in a Fibonacci heap.

    Args:
        val: The value stored in the node.

    Attributes:
        val: The value stored in the node.
        parent: Reference to parent node.
        child: Reference to one child node.
        left: Reference to left sibling.
        right: Reference to right sibling.
        degree: Number of children.
        mark: Boolean indicating if node has lost a child.
    """
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

    def add_sibling(self, node):
        """
        Adds a node as a sibling to the current node.

        Args:
            node: The node to add as a sibling.
        """
        node.left = self
        node.right = self.right
        self.right.left = node
        self.right = node

    def add_child(self, node):
        """
        Adds a node as a child of the current node.

        Args:
            node: The node to add as a child.
        """
        node.parent = self
        if not self.child:
            self.child = node
        else:
            self.child.add_sibling(node)
        self.degree += 1

    def remove(self):
        """Removes this node from its sibling list."""
        self.left.right = self.right
        self.right.left = self.left


class FibonacciHeap:
    """
    A Fibonacci heap implementation providing
    amortized efficient priority queue operations.

    This implementation provides the following time complexities:
        - Insert: O(1) amortized
        - Find minimum: O(1)
        - Delete minimum: O(log n) amortized
        - Decrease key: O(1) amortized
        - Merge: O(1)

    Example:
    >>> heap = FibonacciHeap()
    >>> node1 = heap.insert(3)
    >>> node2 = heap.insert(2)
    >>> node3 = heap.insert(15)
    >>> heap.peek()
    2
    >>> heap.delete_min()
    2
    >>> heap.peek()
    3
    >>> other_heap = FibonacciHeap()
    >>> node4 = other_heap.insert(1)
    >>> heap.merge_heaps(other_heap)
    >>> heap.peek()
    1
    """

    def __init__(self):
        """Initializes an empty Fibonacci heap."""
        self.min_node = None
        self.size = 0

    def is_empty(self):
        """
        Checks if the heap is empty.

        Returns:
            bool: True if heap is empty, False otherwise.
        """
        return self.min_node is None

    def insert(self, val):
        """
        Inserts a new value into the heap.

        Args:
            val: Value to insert.

        Returns:
            Node: The newly created node.
        """
        node = Node(val)
        if not self.min_node:
            self.min_node = node
        else:
            self.min_node.add_sibling(node)
            if node.val < self.min_node.val:
                self.min_node = node
        self.size += 1
        return node

    def peek(self):
        """
        Returns the minimum value without removing it.

        Returns:
            The minimum value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.min_node:
            raise IndexError("Heap is empty")
        return self.min_node.val

    def merge_heaps(self, other):
        """
        Merges another Fibonacci heap into this one.

        Args:
            other: Another FibonacciHeap instance to merge with this one.
        """
        if not other.min_node:
            return
        if not self.min_node:
            self.min_node = other.min_node
        else:
            # Merge root lists
            self.min_node.right.left = other.min_node.left
            other.min_node.left.right = self.min_node.right
            self.min_node.right = other.min_node
            other.min_node.left = self.min_node

            if other.min_node.val < self.min_node.val:
                self.min_node = other.min_node

        self.size += other.size

    def __link_trees(self, node1, node2):
        """
        Links two trees of same degree.

        Args:
            node1: First tree's root node.
            node2: Second tree's root node.
        """
        node1.remove()
        if node2.child:
            node2.child.add_sibling(node1)
        else:
            node2.child = node1
        node1.parent = node2
        node2.degree += 1
        node1.mark = False

    def delete_min(self):
        """
        Removes and returns the minimum value from the heap.

        Returns:
            The minimum value that was removed.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.min_node:
            raise IndexError("Heap is empty")

        min_val = self.min_node.val

        # Add all children to root list
        if self.min_node.child:
            curr = self.min_node.child
            while True:
                next_node = curr.right
                curr.parent = None
                curr.mark = False
                self.min_node.add_sibling(curr)
                if curr.right == self.min_node.child:
                    break
                curr = next_node

        # Remove minimum node
        if self.min_node.right == self.min_node:
            self.min_node = None
        else:
            self.min_node.remove()
            self.min_node = self.min_node.right
            self.__consolidate()

        self.size -= 1
        return min_val

    def __consolidate(self):
        """
        Consolidates the trees in the heap after a delete_min operation.

        This is an internal method that maintains the heap's structure.
        """
        max_degree = int(self.size ** 0.5) + 1
        degree_table = [None] * max_degree

        # Collect all roots
        roots = []
        curr = self.min_node
        while True:
            roots.append(curr)
            curr = curr.right
            if curr == self.min_node:
                break

        # Consolidate trees
        for root in roots:
            degree = root.degree
            while degree_table[degree]:
                other = degree_table[degree]
                if root.val > other.val:
                    root, other = other, root
                self.__link_trees(other, root)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = root

        # Find new minimum
        self.min_node = None
        for degree in range(max_degree):
            if degree_table[degree]:
                if not self.min_node:
                    self.min_node = degree_table[degree]
                    self.min_node.left = self.min_node
                    self.min_node.right = self.min_node
                else:
                    self.min_node.add_sibling(degree_table[degree])
                    if degree_table[degree].val < self.min_node.val:
                        self.min_node = degree_table[degree]

    def decrease_key(self, node, new_val):
        """
        Decreases the value of a node.

        Args:
            node: The node whose value should be decreased.
            new_val: The new value for the node.

        Raises:
            ValueError: If new value is greater than current value.
        """
        if new_val > node.val:
            raise ValueError("New value is greater than current value")

        node.val = new_val
        parent = node.parent

        if parent and node.val < parent.val:
            self.__cut(node, parent)
            self.__cascading_cut(parent)

        if node.val < self.min_node.val:
            self.min_node = node

    def __cut(self, node, parent):
        """
        Cuts a node from its parent

        Args:
            node: Node to be cut.
            parent: Parent of the node to be cut.
        """

        parent.degree -= 1
        if parent.child == node:
            parent.child = node.right if node.right != node else None
        node.remove()
        node.left = node
        node.right = node
        node.parent = None
        node.mark = False
        self.min_node.add_sibling(node)

    def __cascading_cut(self, node):
        """
        Performs cascading cut operation.

        Args:
            node: Starting node for cascading cut.
        """

        parent = node.parent
        if parent:
            if not node.mark:
                node.mark = True
            else:
                self.__cut(node, parent)
                self.__cascading_cut(parent)

    def __str__(self):
        """
        Returns a string representation of the heap.

        Returns:
            str: A string showing the heap structure.
        """
        if not self.min_node:
            return "Empty heap"

        def print_tree(node, level=0):
            result = []
            curr = node
            while True:
                result.append("-" * level + str(curr.val))
                if curr.child:
                    result.extend(print_tree(curr.child, level + 1))
                curr = curr.right
                if curr == node:
                    break
            return result

        return "\n".join(print_tree(self.min_node))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
