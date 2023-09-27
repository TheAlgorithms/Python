class Node:
    """
    The Node class represents a node in a Fibonacci heap.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.mark = False


class FibonacciHeap:
    """
    FibonacciHeap is a implementation of Fibonacci heap.
    """

    def __init__(self) -> None:
        self.min = None
        self.num_nodes = 0

    def insert(self, key: int) -> None:
        """
        Inserts a new node to the heap.
        """
        node = Node(key)
        if self.min is None:
            self.min = node
        else:
            self._insert_node(node)
            if node.key < self.min.key:
                self.min = node
        self.num_nodes += 1

    def _insert_node(self, node: Node) -> None:
        node.left = self.min
        node.right = self.min.right
        self.min.right = node
        node.right.left = node

    def get_min(self) -> int:
        """Return min node's key."""
        return self.min.key

    def extract_min(self) -> int:
        """Extract (delete) the min node from the heap."""
        if self.min is None:
            return None
        min_node = self.min
        if min_node.child is not None:
            child = min_node.child
            while True:
                next_node = child.right
                self._insert_node(child)
                child.parent = None
                child = next_node
                if child == min_node.child:
                    break
        min_node.left.right = min_node.right
        min_node.right.left = min_node.left
        if min_node == min_node.right:
            self.min = None
        else:
            self.min = min_node.right
            self._consolidate()
        self.num_nodes -= 1
        return min_node.key

    def union(self, other_heap: "FibonacciHeap") -> "FibonacciHeap":
        """Union (merge) two fibonacci heaps."""
        new_heap = FibonacciHeap()

        new_heap.min = self.min
        if self.min is not None and other_heap.min is not None:
            self.min.right.left = other_heap.min.left
            other_heap.min.left.right = self.min.right
            self.min.right = other_heap.min
            other_heap.min.left = self.min
            if other_heap.min.key < self.min.key:
                self.min = other_heap.min
        elif other_heap.min is not None:
            self.min = other_heap.min

        new_heap.num_nodes = self.num_nodes + other_heap.num_nodes

        self.min = None
        self.num_nodes = 0
        other_heap.min = None
        other_heap.num_nodes = 0

        return new_heap

    def _consolidate(self) -> None:
        aux = [None] * self.num_nodes
        nodes = self._get_nodes()
        for node in nodes:
            degree = node.degree
            while aux[degree] is not None:
                other = aux[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                aux[degree] = None
                degree += 1
            aux[degree] = node
        self.min = None
        for node in aux:
            if node is not None:
                if self.min is None:
                    self.min = node
                else:
                    self._insert_node(node)
                    if node.key < self.min.key:
                        self.min = node

    def _link(self, y: Node, x: Node) -> None:
        y.left.right = y.right
        y.right.left = y.left
        y.parent = x
        if x.child is None:
            x.child = y
            y.right = y
            y.left = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right = y
            y.right.left = y
        x.degree += 1

    def decrease_key(self, node: Node, new_key: int) -> None:
        """Modify the key of some node in the heap."""
        if new_key > node.key:
            return
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min.key:
            self.min = node

    def _cut(self, x: Node, y: Node) -> None:
        x.left.right = x.right
        x.right.left = x.left
        y.degree -= 1
        if x == x.right:
            y.child = None
        elif y.child == x:
            y.child = x.right
        x.parent = None
        x.mark = False
        self._insert_node(x)

    def _cascading_cut(self, y: Node) -> None:
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _get_nodes(self) -> list:
        nodes = []
        if self.min is not None:
            node = self.min
            while True:
                nodes.append(node)
                node = node.right
                if node == self.min:
                    break
        return nodes


def test_fibonacci_heap() -> None:
    """
    >>> h = FibonacciHeap()
    >>> h.insert(10)
    >>> h.insert(5)
    >>> h.insert(7)
    >>> h.get_min()
    5
    >>> h.insert(3)
    >>> h.extract_min()
    3
    >>> h.get_min()
    5
    >>> h.decrease_key(h.min, 2)
    >>> h.get_min()
    2
    >>> h2 = FibonacciHeap()
    >>> h2.insert(8)
    >>> h2.insert(6)
    >>> h2.insert(4)
    >>> h2.get_min()
    4
    >>> h3 = h.union(h2)
    >>> h3.get_min()
    2
    """


if __name__ == "__main__":
    import doctest

    # run doc test
    doctest.testmod()
