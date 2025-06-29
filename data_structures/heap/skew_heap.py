#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...


T = TypeVar("T", bound=Comparable)


class SkewNode(Generic[T]):
    """
    One node of the skew heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: SkewNode[T] | None = None
        self.right: SkewNode[T] | None = None

    @property
    def value(self) -> T:
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
        root1: SkewNode[T] | None, root2: SkewNode[T] | None
    ) -> SkewNode[T] | None:
        """
        Merge two nodes together.
        >>> SkewNode.merge(SkewNode(10), SkewNode(-10.5)).value
        -10.5
        >>> SkewNode.merge(SkewNode(10), SkewNode(10.5)).value
        10
        >>> SkewNode.merge(SkewNode(10), SkewNode(10)).value
        10
        >>> SkewNode.merge(SkewNode(-100), SkewNode(-10.5)).value
        -100
        """
        # Handle empty nodes
        if not root1:
            return root2
        if not root2:
            return root1

        # Compare values using explicit comparison function
        if SkewNode._is_less_than(root1.value, root2.value):
            # root1 is smaller, make it the new root
            result = root1
            temp = root1.right
            result.right = root1.left
            result.left = SkewNode.merge(temp, root2)
            return result
        else:
            # root2 is smaller or equal, use it as new root
            result = root2
            temp = root2.right
            result.right = root2.left
            result.left = SkewNode.merge(root1, temp)
            return result

    @staticmethod
    def _is_less_than(a: T, b: T) -> bool:
        """Safe comparison function that avoids type checker issues"""
        try:
            return a < b
        except TypeError:
            # Fallback comparison for non-comparable types
            # Uses string representation as last resort
            return str(a) < str(b)


class SkewHeap(Generic[T]):
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

    def __init__(self, data: Iterable[T] | None = ()) -> None:
        """
        Initialize the skew heap with optional data

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> list(sh)
        [1, 3, 3, 7]
        """
        self._root: SkewNode[T] | None = None
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

    def __iter__(self) -> Iterator[T]:
        """
        Iterate through all values in sorted order

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> list(sh)
        [1, 3, 3, 7]
        """
        # Create a temporary heap for iteration
        temp_heap: SkewHeap[T] = SkewHeap()
        result: list[T] = []

        # Pop all elements from the heap
        while self:
            item = self.pop()
            result.append(item)
            temp_heap.insert(item)

        # Restore the heap state
        self._root = temp_heap._root
        return iter(result)

    def insert(self, value: T) -> None:
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
        self._root = SkewNode.merge(self._root, SkewNode(value))

    def pop(self) -> T:
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
            self._root = SkewNode.merge(self._root.left, self._root.right)
        return result

    def top(self) -> T:
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
