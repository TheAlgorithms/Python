"""
Fibonacci Heap Implementation in Python.

This module provides an implementation of a Fibonacci Heap, a data structure
that supports a priority queue with efficient operations.
Referenced from: https://en.wikipedia.org/wiki/Fibonacci_heap

Classes:
    - FibonacciHeapNode: Represents a node in the Fibonacci Heap.
    - FibonacciHeap: Represents the Fibonacci Heap itself.

Examples:
    >>> fh = FibonacciHeap()
    >>> n1 = fh.insert(10, "value1")
    >>> n2 = fh.insert(2, "value2")
    >>> n3 = fh.insert(15, "value3")
    >>> fh.find_min().key
    2
    >>> fh.decrease_key(n3, 1)
    >>> fh.find_min().key
    1
    >>> fh.extract_min().key
    1
    >>> fh.find_min().key
    2
"""

import math


class FibonacciHeapNode:
    """
    Represents a node in the Fibonacci Heap.

    Attributes:
        key (any): The key of the node.
        value (any): The value associated with the key.
        degree (int): The number of children of this node.
        parent (FibonacciHeapNode): The parent of this node.
        child (FibonacciHeapNode): The first child of this node.
        mark (bool): Whether this node has
            lost a child since it became a child of another node.
        next (FibonacciHeapNode): The next sibling in the circular doubly-linked list.
        prev (FibonacciHeapNode): The previous sibling
            in the circular doubly-linked list.
    """

    def __init__(self, key, value=None):
        """
        Initializes a new Fibonacci Heap Node.

        Args:
            key (any): The key of the node.
            value (any, optional): The value associated with the key. Defaults to None.
        """
        self.key = key
        self.value = value
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        self.next = self
        self.prev = self

    def add_child(self, node):
        """
        Adds a child node to this node.

        Args:
            node (FibonacciHeapNode): The child node to be added.
        """
        if not self.child:
            self.child = node
        else:
            node.prev = self.child
            node.next = self.child.next
            self.child.next.prev = node
            self.child.next = node
        node.parent = self
        self.degree += 1

    def remove_child(self, node):
        """
        Removes a child node from this node.

        Args:
            node (FibonacciHeapNode): The child node to be removed.
        """
        if node.next == node:  # Single child
            self.child = None
        elif self.child == node:
            self.child = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        node.parent = None
        self.degree -= 1


class FibonacciHeap:
    """
    Represents a Fibonacci Heap.

    Attributes:
        min_node (FibonacciHeapNode): The node with the minimum key.
        total_nodes (int): The total number of nodes in the heap.
    """

    def __init__(self):
        """
        Initializes an empty Fibonacci Heap.
        """
        self.min_node = None
        self.total_nodes = 0

    def is_empty(self):
        """
        Checks if the heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.

        Examples:
            >>> fh = FibonacciHeap()
            >>> fh.is_empty()
            True
            >>> n1 = fh.insert(5)
            >>> fh.is_empty()
            False
        """
        return self.min_node is None

    def insert(self, key, value=None):
        """
        Inserts a new node into the heap.

        Args:
            key (any): The key of the new node.
            value (any, optional): The value associated with the key. Defaults to None.

        Returns:
            FibonacciHeapNode: The newly inserted node.

        Examples:
            >>> fh = FibonacciHeap()
            >>> node = fh.insert(5, "value")
            >>> node.key
            5
        """
        node = FibonacciHeapNode(key, value)
        self._merge_with_root_list(node)
        if not self.min_node or node.key < self.min_node.key:
            self.min_node = node
        self.total_nodes += 1
        return node

    def find_min(self):
        """
        Finds the node with the minimum key.

        Returns:
            FibonacciHeapNode: The node with the minimum key.

        Examples:
            >>> fh = FibonacciHeap()
            >>> n1 = fh.insert(10)
            >>> n2 = fh.insert(2)
            >>> fh.find_min().key
            2
        """
        return self.min_node

    def extract_min(self):
        """
        Removes and returns the node with the minimum key.

        Returns:
            FibonacciHeapNode: The node with the minimum key.

        Examples:
            >>> fh = FibonacciHeap()
            >>> n1 = fh.insert(10)
            >>> n2 = fh.insert(2)
            >>> fh.extract_min().key
            2
        """
        temp_min_node = self.min_node
        if temp_min_node:
            if temp_min_node.child:
                children = list(self._iterate(temp_min_node.child))
                for child in children:
                    self._merge_with_root_list(child)
                    child.parent = None
            self._remove_from_root_list(temp_min_node)
            if temp_min_node == temp_min_node.next:
                self.min_node = None
            else:
                self.min_node = temp_min_node.next
                self._consolidate()
            self.total_nodes -= 1
        return temp_min_node

    def decrease_key(self, node, new_key):
        """
        Decreases the key of a given node.

        Args:
            node (FibonacciHeapNode): The node to decrease the key for.
            new_key (any): The new key value.

        Raises:
            ValueError: If the new key is greater than the current key.

        Examples:
            >>> fh = FibonacciHeap()
            >>> node = fh.insert(10)
            >>> fh.decrease_key(node, 5)
            >>> fh.find_min().key
            5
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        temp_parent = node.parent
        if temp_parent and node.key < temp_parent.key:
            self._cut(node, temp_parent)
            self._cascading_cut(temp_parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def delete(self, x):
        """
        Deletes a given node from the heap.

        Args:
            x (FibonacciHeapNode): The node to be deleted.

        Examples:
            >>> fh = FibonacciHeap()
            >>> node = fh.insert(10)
            >>> fh.delete(node)
            >>> fh.is_empty()
            True
        """
        self.decrease_key(x, -math.inf)
        self.extract_min()

    def union(self, other_heap):
        """
        Merges another Fibonacci Heap into this heap.

        Args:
            other_heap (FibonacciHeap): The other Fibonacci Heap to be merged.

        Examples:
            >>> fh1 = FibonacciHeap()
            >>> fh2 = FibonacciHeap()
            >>> n1 = fh1.insert(10)
            >>> n2 = fh2.insert(5)
            >>> fh1.union(fh2)
            >>> fh1.find_min().key
            5
        """
        if not other_heap.min_node:
            return
        if not self.min_node:
            self.min_node = other_heap.min_node
        else:
            self._merge_with_root_list(other_heap.min_node)
            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node
        self.total_nodes += other_heap.total_nodes

    def _merge_with_root_list(self, node):
        """
        Merges a node into the root list.

        Args:
            node (FibonacciHeapNode): The node to be merged.
        """
        if not self.min_node:
            self.min_node = node
        else:
            node.prev = self.min_node
            node.next = self.min_node.next
            self.min_node.next.prev = node
            self.min_node.next = node

    def _remove_from_root_list(self, node):
        """
        Removes a node from the root list.

        Args:
            node (FibonacciHeapNode): The node to be removed.
        """
        if node.next == node:
            self.min_node = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def _consolidate(self):
        """
        Consolidates the heap by combining trees of the same degree.
        """
        array_size = int(math.log(self.total_nodes) * 2) + 1
        array = [None] * array_size
        nodes = list(self._iterate(self.min_node))
        for node in nodes:
            temp_node = node
            degree = temp_node.degree
            while array[degree]:
                array_node = array[degree]
                if temp_node.key > array_node.key:
                    temp_node, array_node = array_node, temp_node
                self._link(array_node, temp_node)
                array[degree] = None
                degree += 1
            array[degree] = temp_node
        self.min_node = None
        for i in range(array_size):
            if array[i]:
                if not self.min_node:
                    self.min_node = array[i]
                else:
                    self._merge_with_root_list(array[i])
                    if array[i].key < self.min_node.key:
                        self.min_node = array[i]

    def _link(self, node_to_link, node_to_parent):
        """
        Links two nodes by making one a child of the other.

        Args:
            node_to_link (FibonacciHeapNode): The node to be linked as a child.
            node_to_parent (FibonacciHeapNode): The node to be the parent.
        """
        self._remove_from_root_list(node_to_link)
        node_to_parent.add_child(node_to_link)
        node_to_link.mark = False

    def _cut(self, node_to_cut, parent_node):
        """
        Cuts a node from its parent and adds it to the root list.

        Args:
            node_to_cut (FibonacciHeapNode): The node to be cut.
            parent_node (FibonacciHeapNode): The parent node.
        """
        parent_node.remove_child(node_to_cut)
        self._merge_with_root_list(node_to_cut)
        node_to_cut.mark = False

    def _cascading_cut(self, node_to_cut):
        """
        Performs a cascading cut operation.

        Args:
            node_to_cut (FibonacciHeapNode): The node to be cut recursively.
        """
        if temp_parent := node_to_cut.parent:
            if not node_to_cut.mark:
                node_to_cut.mark = True
            else:
                self._cut(node_to_cut, temp_parent)
                self._cascading_cut(temp_parent)

    def _iterate(self, start):
        """
        Iterates through a circular doubly linked list starting at a given node.

        Args:
            start (FibonacciHeapNode): The starting node.

        Yields:
            FibonacciHeapNode: The next node in the list.
        """
        node = start
        while True:
            yield node
            node = node.next
            if node == start:
                break
