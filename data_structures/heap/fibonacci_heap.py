"""
Fibonacci Heap
A more efficient priority queue implementation that provides amortized time bounds
that are better than those of the binary and binomial heaps.

Operations supported:
- Insert: O(1) amortized
- Find minimum: O(1)
- Delete minimum: O(log n) amortized
- Decrease key: O(1) amortized
- Merge: O(1)
"""


class Node:
    """
    Node in a Fibonacci heap containing:
        - value
        - parent, child, and sibling links
        - degree (number of children)
        - mark (whether the node has lost a child since
         becoming a child of its current parent)
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
        """Add node as a sibling"""
        node.left = self
        node.right = self.right
        self.right.left = node
        self.right = node

    def add_child(self, node):
        """Add node as a child"""
        node.parent = self
        if not self.child:
            self.child = node
        else:
            self.child.add_sibling(node)
        self.degree += 1

    def remove(self):
        """Remove this node from its sibling list"""
        self.left.right = self.right
        self.right.left = self.left


class FibonacciHeap:
    """
    Min-oriented Fibonacci heap implementation.

    Example:
    >>> heap = FibonacciHeap()
    >>> heap.insert(3)
    >>> heap.insert(2)
    >>> heap.insert(15)
    >>> heap.peek()
    2
    >>> heap.delete_min()
    2
    >>> heap.peek()
    3
    """

    def __init__(self):
        self.min_node = None
        self.size = 0

    def is_empty(self):
        """Return True if heap is empty"""
        return self.min_node is None

    def insert(self, val):
        """Insert a new key into the heap"""
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
        """Return minimum value without removing it"""
        if not self.min_node:
            raise IndexError("Heap is empty")
        return self.min_node.val

    def merge_heaps(self, other):
        """Merge another Fibonacci heap with this one"""
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
        """Link two trees of same degree"""
        node1.remove()
        if node2.child:
            node2.child.add_sibling(node1)
        else:
            node2.child = node1
        node1.parent = node2
        node2.degree += 1
        node1.mark = False

    def delete_min(self):
        """Remove and return the minimum value"""
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
        """Consolidate trees after delete_min"""
        max_degree = int(self.size**0.5) + 1
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
        """Decrease the value of a node"""
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
        """Cut a node from its parent"""
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
        """Perform cascading cut operation"""
        if parent := node.parent:
            if not node.mark:
                node.mark = True
            else:
                self.__cut(node, parent)
                self.__cascading_cut(parent)

    def __str__(self):
        """String representation of the heap"""
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
