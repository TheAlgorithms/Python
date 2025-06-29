#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from typing import Any


class SkewNode:
    """
    One node of the skew heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: Any) -> None:
        self._value: Any = value
        self.left: SkewNode | None = None
        self.right: SkewNode | None = None

    @property
    def value(self) -> Any:
        """
        Return the value of the node.

        >>> SkewNode(0).value
        0
        >>> SkewNode(3.14159).value
        3.14159
        >>> SkewNode("hello").value
        'hello'
        >>> SkewNode(True).value
        True
        >>> SkewNode(10).value
        10
        """
        return self._value

    @staticmethod
    def merge(
        root1: SkewNode | None, root2: SkewNode | None, comp: Callable[[Any, Any], bool]
    ) -> SkewNode | None:
        """
        Merge two nodes together.
        >>> def comp(a, b): return a < b
        >>> SkewNode.merge(SkewNode(10), SkewNode(-10.5), comp).value
        -10.5
        >>> SkewNode.merge(SkewNode(10), SkewNode(10.5), comp).value
        10
        >>> SkewNode.merge(SkewNode(10), SkewNode(10), comp).value
        10
        >>> SkewNode.merge(SkewNode(-100), SkewNode(-10.5), comp).value
        -100
        """
        # Handle empty nodes
        if not root1:
            return root2
        if not root2:
            return root1

        # Compare values using provided comparison function
        if comp(root1.value, root2.value):
            # root1 is smaller, make it the new root
            result = root1
            temp = root1.right
            result.right = root1.left
            result.left = SkewNode.merge(temp, root2, comp)
            return result
        else:
            # root2 is smaller or equal, use it as new root
            result = root2
            temp = root2.right
            result.right = root2.left
            result.left = SkewNode.merge(root1, temp, comp)
            return result


class SkewHeap:
    """
    A data structure that allows inserting a new value and popping the smallest
    values. Both operations take O(logN) time where N is the size of the heap.
    Wiki: https://en.wikipedia.org/wiki/Skew_heap
    Visualization: https://www.cs.usfca.edu/~galles/visualization/SkewHeap.html

    >>> list(SkewHeap([2, 3, 1, 5, 1, 7]))
    [1, 1, 2, 3, 5, 7]

    >>> sh = SkewHeap()
    >>> sh.pop()
    Traceback (most recent call last):
        ...
    IndexError: Can't get top element for the empty heap.

    >>> sh.insert(1)
    >>> sh.insert(-1)
    >>> sh.insert(0)
    >>> list(sh)
    [-1, 0, 1]
    """

    def __init__(
        self,
        data: Iterable[Any] | None = None,
        comp: Callable[[Any, Any], bool] = lambda a, b: a < b,
    ) -> None:
        """
        Initialize the skew heap with optional data and comparison function

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> list(sh)
        [1, 3, 3, 7]

        # Max-heap example
        >>> max_heap = SkewHeap([3, 1, 3, 7], comp=lambda a, b: a > b)
        >>> list(max_heap)
        [7, 3, 3, 1]
        """
        self._root: SkewNode | None = None
        self._comp = comp
        if data:
            for item in data:
                self.insert(item)

    def __bool__(self) -> bool:
        """
        Check if the heap is not empty

        >>> sh = SkewHeap()
        >>> bool(sh)
        False
        >>> sh.insert(1)
        >>> bool(sh)
        True
        >>> sh.clear()
        >>> bool(sh)
        False
        """
        return self._root is not None

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate through all values in sorted order

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> list(sh)
        [1, 3, 3, 7]
        """
        # Create a temporary heap for iteration
        temp_heap = SkewHeap(comp=self._comp)
        result: list[Any] = []

        # Pop all elements from the heap
        while self:
            item = self.pop()
            result.append(item)
            temp_heap.insert(item)

        # Restore the heap state
        self._root = temp_heap._root
        return iter(result)

    def insert(self, value: Any) -> None:
        """
        Insert a new value into the heap

        >>> sh = SkewHeap()
        >>> sh.insert(3)
        >>> sh.insert(1)
        >>> sh.insert(3)
        >>> sh.insert(7)
        >>> list(sh)
        [1, 3, 3, 7]
        """
        self._root = SkewNode.merge(self._root, SkewNode(value), self._comp)

    def pop(self) -> Any:
        """
        Remove and return the smallest value from the heap

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> sh.pop()
        1
        >>> sh.pop()
        3
        >>> sh.pop()
        3
        >>> sh.pop()
        7
        >>> sh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        result = self.top()
        if self._root:
            self._root = SkewNode.merge(self._root.left, self._root.right, self._comp)
        return result

    def top(self) -> Any:
        """
        Return the smallest value without removing it

        >>> sh = SkewHeap()
        >>> sh.insert(3)
        >>> sh.top()
        3
        >>> sh.insert(1)
        >>> sh.top()
        1
        >>> sh.insert(3)
        >>> sh.top()
        1
        >>> sh.insert(7)
        >>> sh.top()
        1
        """
        if not self._root:
            raise IndexError("Can't get top element for the empty heap.")
        return self._root.value

    def clear(self) -> None:
        """
        Clear all elements from the heap

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> sh.clear()
        >>> sh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        self._root = None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
