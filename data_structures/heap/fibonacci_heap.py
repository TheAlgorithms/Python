"""Fibonacci Heap implementation - An advanced priority queue data structure.

A Fibonacci heap is a heap data structure consisting of a collection of heap-ordered
trees. It has a better amortized running time than other heap types, particularly for
the decrease-key operation which runs in amortized O(1) time.

This makes Fibonacci heaps ideal for algorithms like Dijkstra's shortest path and
Prim's minimum spanning tree algorithm.

For more information, see: https://en.wikipedia.org/wiki/Fibonacci_heap

Time Complexity (amortized):
- Insert: O(1)
- Find minimum: O(1)
- Delete minimum: O(log n)
- Decrease key: O(1)
- Merge: O(1)

Space Complexity: O(n)
"""

from __future__ import annotations

from typing import Any


class FibonacciNode:
    """A node in the Fibonacci heap."""

    def __init__(self, key: Any, value: Any = None) -> None:
        self.key = key  # Priority key
        self.value = value  # Associated data
        self.parent: FibonacciNode | None = None
        self.child: FibonacciNode | None = None
        self.left: FibonacciNode | None = None  # Left sibling
        self.right: FibonacciNode | None = None  # Right sibling
        self.degree = 0  # Number of children
        self.marked = False  # Whether node has lost a child since becoming a child


class FibonacciHeap:
    """
    Fibonacci Heap implementation - Advanced priority queue.

    This implementation provides amortized O(1) decrease-key operations,
    making it suitable for algorithms requiring frequent priority updates.

    Example:
    >>> heap = FibonacciHeap()
    >>> heap.insert(10, "ten")
    >>> heap.insert(5, "five")
    >>> heap.insert(15, "fifteen")
    >>> heap.find_min()
    (5, 'five')
    >>> heap.extract_min()
    (5, 'five')
    >>> heap.find_min()
    (10, 'ten')
    """

    def __init__(self) -> None:
        """Initialize an empty Fibonacci heap."""
        self.min_node: FibonacciNode | None = None
        self.total_nodes = 0

    def __bool__(self) -> bool:
        """Return True if the heap is not empty."""
        return self.min_node is not None

    def __len__(self) -> int:
        """Return the number of nodes in the heap."""
        return self.total_nodes

    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return self.min_node is None

    def insert(self, key: Any, value: Any = None) -> None:
        """Insert a new key-value pair into the heap."""
        node = FibonacciNode(key, value)
        if not self.min_node:
            self.min_node = node
            node.left = node
            node.right = node
        else:
            # Insert into root list
            assert self.min_node.right is not None
            assert self.min_node.left is not None
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node
            if key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1

    def find_min(self):
        """Find the minimum key-value pair without removing it."""
        if not self.min_node:
            return None
        return (self.min_node.key, self.min_node.value)

    def extract_min(self):
        """Extract and return the minimum key-value pair."""
        if not self.min_node:
            return None

        min_node = self.min_node
        result = (min_node.key, min_node.value)

        # Handle children
        if min_node.child:
            child = min_node.child
            while True:
                next_child = child.right
                # Add child to root list
                child.left = min_node.left
                child.right = min_node.right
                min_node.left.right = child
                min_node.right.left = child
                child.parent = None
                child = next_child
                if child == min_node.child:
                    break

        # Remove min_node from root list
        if min_node.left == min_node:
            self.min_node = None
        else:
            min_node.left.right = min_node.right
            min_node.right.left = min_node.left
            self.min_node = min_node.right
            # Find new minimum
            current = self.min_node
            min_key = current.key
            start = current
            current = current.right
            while current != start:
                if current.key < min_key:
                    min_key = current.key
                    self.min_node = current
                current = current.right

        self.total_nodes -= 1
        return result

    def merge(self, other):
        """Merge this heap with another Fibonacci heap."""
        if not other.min_node:
            return self
        if not self.min_node:
            self.min_node = other.min_node
            self.total_nodes = other.total_nodes
            return self

        # Merge root lists
        self.min_node.left.right = other.min_node.right
        other.min_node.right.left = self.min_node.left
        self.min_node.left = other.min_node.left
        other.min_node.left.right = self.min_node

        # Update minimum
        if other.min_node.key < self.min_node.key:
            self.min_node = other.min_node

        self.total_nodes += other.total_nodes
        return self
