#!/usr/bin/env python3

from __future__ import annotations

import random
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class RandomizedHeapNode(Generic[T]):
    """
    One node of the randomized heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: RandomizedHeapNode[T] | None = None
        self.right: RandomizedHeapNode[T] | None = None

    @property
    def value(self) -> T:
        """Return the value of the node."""
        return self._value

    @staticmethod
    def merge(
        root1: RandomizedHeapNode[T] | None, root2: RandomizedHeapNode[T] | None
    ) -> RandomizedHeapNode[T] | None:
        """Merge 2 nodes together."""
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        if random.choice([True, False]):
            root1.left, root1.right = root1.right, root1.left

        root1.left = RandomizedHeapNode.merge(root1.left, root2)

        return root1


class RandomizedHeap(Generic[T]):
    """
    A data structure that allows inserting a new value and to pop the smallest
    values. Both operations take O(logN) time where N is the size of the
    structure.
    Wiki: https://en.wikipedia.org/wiki/Randomized_meldable_heap

    >>> RandomizedHeap([2, 3, 1, 5, 1, 7]).to_sorted_list()
    [1, 1, 2, 3, 5, 7]

    >>> rh = RandomizedHeap()
    >>> rh.pop()
    Traceback (most recent call last):
        ...
    IndexError: Can't get top element for the empty heap.

    >>> rh.insert(1)
    >>> rh.insert(-1)
    >>> rh.insert(0)
    >>> rh.to_sorted_list()
    [-1, 0, 1]
    """

    def __init__(self, data: Iterable[T] | None = ()) -> None:
        """
        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.to_sorted_list()
        [1, 3, 3, 7]
        """
        self._root: RandomizedHeapNode[T] | None = None
        for item in data:
            self.insert(item)

    def insert(self, value: T) -> None:
        """
        Insert the value into the heap.

        >>> rh = RandomizedHeap()
        >>> rh.insert(3)
        >>> rh.insert(1)
        >>> rh.insert(3)
        >>> rh.insert(7)
        >>> rh.to_sorted_list()
        [1, 3, 3, 7]
        """
        self._root = RandomizedHeapNode.merge(self._root, RandomizedHeapNode(value))

    def pop(self) -> T:
        """
        Pop the smallest value from the heap and return it.

        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.pop()
        1
        >>> rh.pop()
        3
        >>> rh.pop()
        3
        >>> rh.pop()
        7
        >>> rh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        result = self.top()
        self._root = RandomizedHeapNode.merge(self._root.left, self._root.right)

        return result

    def top(self) -> T:
        """
        Return the smallest value from the heap.

        >>> rh = RandomizedHeap()
        >>> rh.insert(3)
        >>> rh.top()
        3
        >>> rh.insert(1)
        >>> rh.top()
        1
        >>> rh.insert(3)
        >>> rh.top()
        1
        >>> rh.insert(7)
        >>> rh.top()
        1
        """
        if not self._root:
            raise IndexError("Can't get top element for the empty heap.")
        return self._root.value

    def clear(self):
        """
        Clear the heap.

        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.clear()
        >>> rh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        self._root = None

    def to_sorted_list(self) -> list[T]:
        """
        Returns sorted list containing all the values in the heap.

        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.to_sorted_list()
        [1, 3, 3, 7]
        """
        result = []
        while self:
            result.append(self.pop())

        return result

    def __bool__(self) -> bool:
        """
        Check if the heap is not empty.

        >>> rh = RandomizedHeap()
        >>> bool(rh)
        False
        >>> rh.insert(1)
        >>> bool(rh)
        True
        >>> rh.clear()
        >>> bool(rh)
        False
        """
        return self._root is not None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
