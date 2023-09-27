"""
All about Fibonacci heap: https://en.wikipedia.org/wiki/Fibonacci_heap
"""
from typing import Any


class Node:
    """
    The Node class represents a node in a Fibonacci heap.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.degree = 0
        self.parent: Any = None
        self.child: Any = None
        self.left = self
        self.right = self
        self.mark = False


class FibonacciHeap:
    """
    FibonacciHeap is a implementation of Fibonacci heap.
    """

    def __init__(self) -> None:
        self.min: Node | Any = None
        self.num_nodes: int = 0

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

    def extract_min(self) -> int | None:
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
        aux: list[Node | Any] = [None] * self.num_nodes
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

    def _link(self, other: Node, node: Node) -> None:
        other.left.right = other.right
        other.right.left = other.left
        other.parent = node
        if node.child is None:
            node.child = other
            other.right = other
            other.left = other
        else:
            other.left = node.child
            other.right = node.child.right
            node.child.right = other
            other.right.left = other
        node.degree += 1

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

    def _cut(self, current_node: Node, parent_node: Node) -> None:
        current_node.left.right = current_node.right
        current_node.right.left = current_node.left
        parent_node.degree -= 1
        if current_node == current_node.right:
            parent_node.child = None
        elif parent_node.child == current_node:
            parent_node.child = current_node.right
        current_node.parent = None
        current_node.mark = False
        self._insert_node(current_node)

    def _cascading_cut(self, node: Node) -> None:
        if (parent := node.parent) is not None:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def _get_nodes(self) -> list[Node]:
        nodes: list[Node] = []
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
