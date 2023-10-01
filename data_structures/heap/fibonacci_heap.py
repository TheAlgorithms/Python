from math import log


class FibonacciNode:
    """
    Node in a Fibonacci Heap, containing:
    - value
    - degree (number of children)
    - child (a child node)
    - left and right pointers to neighboring nodes
    - parent (pointer to the parent node)
    - mark (boolean flag to indicate if the node has lost a child)
    """

    def __init__(self, val):
        """
        Initialize a FibonacciNode with the given value.
        """
        self.val = val
        self.degree = 0
        self.child = None
        self.left = self
        self.right = self
        self.parent = None
        self.mark = False

    def add_child(self, child):
        """
        Add a child to this node.
        """
        if self.child is None:
            self.child = child
        else:
            child.right = self.child
            child.left = self.child.left
            self.child.left.right = child
            self.child.left = child
        child.parent = self
        self.degree += 1

    def remove_child(self, child):
        """
        Remove a child from this node's children.
        """
        if child == self.child:
            if child.right == child:
                self.child = None
            else:
                self.child = child.right
        child.left.right = child.right
        child.right.left = child.left
        child.parent = None
        child.mark = False
        self.degree -= 1


class FibonacciHeap:
    """
    Min-oriented priority queue implemented with the Fibonacci Heap data structure.
    It supports:
    - Insert element: O(1)
    - Find minimum: O(1)
    - Merge (meld) heaps: O(1)
    - Delete minimum: Amortized O(log n)
    - Decrease key: Amortized O(1)
    - Delete node: Amortized O(log n)

    For more details, refer to the Wikipedia page on [Fibonacci Heap](https://en.wikipedia.org/wiki/Fibonacci_heap).
    """

    def __init__(self):
        """
        Initialize an empty Fibonacci Heap.
        """
        self.min_node = None
        self.root_list = []
        self.size = 0

    def insert(self, val):
        """
        Insert a new element with the given value into the Fibonacci Heap.
        """
        new_node = FibonacciNode(val)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if val < self.min_node.val:
                self.min_node = new_node
        self.root_list.append(new_node)
        self.size += 1

    def _link(self, min_node, new_node):
        """
        Link two nodes in the Fibonacci Heap.
        """
        min_node.add_child(new_node)

    def find_min(self):
        """
        Find the minimum element in the Fibonacci Heap.
        """
        if self.min_node is None:
            raise Exception("Heap is empty")
        return self.min_node.val

    def _consolidate(self):
        """
        Consolidate nodes with the same degree in the Fibonacci Heap.
        """
        max_degree = int(2 * log(self.size) / log(1.618))
        degree_table = [None] * (max_degree + 1)

        current = self.root_list[:]
        for node in current:
            degree = node.degree
            while degree_table[degree]:
                other = degree_table[degree]
                if node.val > other.val:
                    node, other = other, node
                self._link(other, node)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        self.min_node = None
        for node in degree_table:
            if node and (self.min_node is None or node.val < self.min_node.val):
                self.min_node = node

    def delete_min(self):
        """
        Delete the minimum element from the Fibonacci Heap.
        """
        if self.min_node is None:
            return None

        min_val = self.min_node.val

        if self.min_node.child:
            children = self.min_node.child
            while True:
                next_child = children.right
                children.parent = None
                self.root_list.append(children)
                if next_child == self.min_node.child:
                    break
                children = next_child

        self.root_list.remove(self.min_node)
        self._consolidate()
        self._update_min_node()
        self.size -= 1

        return min_val

    def decrease_key(self, node, new_val):
        """
        Decrease the key of a node in the Fibonacci Heap.
        """
        if new_val > node.val:
            raise ValueError("New value is greater than current value")
        node.val = new_val
        parent = node.parent
        if parent and node.val < parent.val:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.val < self.min_node.val:
            self.min_node = node

    def _cut(self, node, parent):
        """
        Cut a node from its parent in the Fibonacci Heap.
        """
        parent.remove_child(node)
        self.root_list.append(node)
        node.mark = False

    def _cascading_cut(self, node):
        """
        Perform a cascading cut operation in the Fibonacci Heap.
        """
        parent = node.parent
        if parent:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def delete_node(self, node):
        """
        Delete a specific node from the Fibonacci Heap.
        """
        self.decrease_key(node, float("-inf"))
        self.delete_min()

    def _update_min_node(self):
        """
        Update the minimum node in the Fibonacci Heap.
        """
        if not self.root_list:
            self.min_node = None
            return

        min_val = min(node.val for node in self.root_list)
        self.min_node = next(
            node for node in self.root_list if node.val == min_val)

    def __str__(self):
        """
        Return a string representation of the Fibonacci Heap.
        """
        if self.min_node is None:
            return "Fibonacci Heap (Empty)"
        return f"Fibonacci Heap (Minimum: {self.min_node.val})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
