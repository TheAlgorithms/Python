# Implementation of a Fibonacci Heap based on the concepts described in "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein.
# Reference: https://en.wikipedia.org/wiki/Fibonacci_heap

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, Generic, TypeVar

T = TypeVar("T", bound=int)


class FibonacciNode(Generic[T]):
    def __init__(self, key: T) -> None:
        """
        Create a new FibonacciNode with the given key.

        Args:
            key (T): The key value associated with the node.
        """
        self.key: T = key
        self.degree: int = 0
        self.parent: FibonacciNode[T] | None = None
        self.child: FibonacciNode[T] | None = None
        self.is_marked: bool = False
        self.next: FibonacciNode[T] = self
        self.prev: FibonacciNode[T] = self


class FibonacciHeap(Generic[T]):
    def __init__(self) -> None:
        """
        Create a new Fibonacci Heap.

        The Fibonacci Heap is initialized as an empty heap.
        """
        self.min_node: FibonacciNode[T] | None = None
        self.num_nodes: int = 0

    def insert(self, key: T) -> None:
        """
        Insert a new node with the given key into the Fibonacci Heap.

        Args:
            key (T): The key value to insert.

        >>> fh = FibonacciHeap()
        >>> fh.insert(5)
        >>> fh.insert(3)
        >>> fh.insert(8)
        >>> fh.extract_min()
        3
        >>> fh.extract_min()
        5
        >>> fh.extract_min()
        8
        """
        new_node = FibonacciNode(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._link_nodes(self.min_node, new_node)
            if key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def _link_nodes(
        self, min_node: FibonacciNode[T], new_node: FibonacciNode[T]
    ) -> None:
        """
        Link two nodes together in the Fibonacci Heap.

        Args:
            min_node (FibonacciNode): The minimum node.
            new_node (FibonacciNode): The new node to be linked.

        >>> fh = FibonacciHeap()
        >>> node1 = FibonacciNode(3)
        >>> node2 = FibonacciNode(5)
        >>> fh._link_nodes(node1, node2)
        >>> node1.next == node2 and node2.prev == node1
        True
        """
        new_node.next = min_node.next
        min_node.next = new_node
        new_node.prev = min_node
        new_node.next.prev = new_node

    def _consolidate(self) -> None:
        """
        Consolidate the heap by combining trees with the same degree.

        This is an internal method used to maintain the Fibonacci Heap's properties.

        >>> fh = FibonacciHeap()
        >>> fh.insert(5)
        >>> fh.insert(3)
        >>> fh.insert(8)
        >>> fh._consolidate()
        >>> fh.min_node.key
        3
        """
        max_degree = int(self.num_nodes**0.5) + 1
        degree_buckets: list[FibonacciNode[T] | None] = [None] * max_degree

        current_node = self.min_node
        nodes_to_visit = [current_node]
        while True:
            current_node = current_node.next
            if current_node == self.min_node:
                break
            nodes_to_visit.append(current_node)

        for node in nodes_to_visit:
            degree = node.degree
            while degree_buckets[degree]:
                other = degree_buckets[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link_nodes(node, other)
                degree_buckets[degree] = None
                degree += 1
            degree_buckets[degree] = node

        self.min_node = None
        for node in degree_buckets:
            if node:
                if self.min_node is None or node.key < self.min_node.key:
                    self.min_node = node

    def extract_min(self) -> T | None:
        """
        Extract the minimum element from the Fibonacci Heap.

        Returns:
            T | None: The minimum element, or None if the heap is empty.

        >>> fh = FibonacciHeap()
        >>> fh.insert(5)
        >>> fh.insert(3)
        >>> fh.insert(8)
        >>> fh.extract_min()
        3
        >>> fh.extract_min()
        5
        >>> fh.extract_min()
        8
        >>> fh.extract_min()
        """
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
                    min_node.child = None
                    if next_child == min_node.child:
                        break
                    child = next_child
            self._remove_node(min_node)
            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()
            self.num_nodes -= 1
        return min_node.key if min_node else None

    def _remove_node(self, node: FibonacciNode[T]) -> None:
        """
        Remove a node from the doubly linked list of nodes.

        Args:
            node (FibonacciNode): The node to remove.

        >>> fh = FibonacciHeap()
        >>> node1 = FibonacciNode(3)
        >>> fh._remove_node(node1)
        >>> node1.next == node1.prev == node1
        True
        """
        node.prev.next = node.next
        node.next.prev = node.prev


if __name__ == "__main__":
    import doctest

    doctest.testmod()
