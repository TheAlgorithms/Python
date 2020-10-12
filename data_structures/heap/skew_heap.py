#!/usr/bin/env python3

from __future__ import annotations

from typing import Generic, Iterable, List, Optional, TypeVar

__all__ = ["SkewHeap"]

T = TypeVar("T")


class SkewNode(Generic[T]):
    """One node of the skew heap. Contains the value and references to two children."""

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: Optional[SkewNode[T]] = None
        self.right: Optional[SkewNode[T]] = None

    @property
    def value(self) -> T:
        """Return the value of the node."""
        return self._value

    @staticmethod
    def merge(
        root1: Optional[SkewNode[T]], root2: Optional[SkewNode[T]]
    ) -> Optional[SkewNode[T]]:
        """Merge 2 nodes together."""
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        result = root1
        temp = root1.right
        result.right = root1.left
        result.left = SkewNode.merge(temp, root2)

        return result


class SkewHeap(Generic[T]):
    """
    A data structure that allows inserting a new value and to pop the smallest
    values. Both operations take O(logN) time where N is the size of the structure.
    - Wiki: https://en.wikipedia.org/wiki/Skew_heap
    - Visualisation: https://www.cs.usfca.edu/~galles/visualization/SkewHeap.html

    >>> SkewHeap.from_list([2, 3, 1, 5, 1, 7]).to_sorted_list()
    [1, 1, 2, 3, 5, 7]

    >>> sh = SkewHeap()
    >>> sh.insert(1)
    >>> sh.top()
    1
    >>> sh.insert(0)
    >>> sh.pop()
    0
    >>> sh.pop()
    1
    >>> sh.top()
    Traceback (most recent call last):
        ...
    AttributeError: Can't get top element for the empty heap.
    """

    def __init__(self) -> None:
        self._root: Optional[SkewNode[T]] = None

    def insert(self, value: T) -> None:
        """Insert the value into the heap."""
        self._root = SkewNode.merge(self._root, SkewNode(value))

    def pop(self) -> T:
        """Pop the smallest value from the heap and return it."""
        result = self.top()
        self._root = SkewNode.merge(self._root.left, self._root.right)

        return result

    def top(self) -> T:
        """Return the smallest value from the heap."""
        if not self._root:
            raise AttributeError("Can't get top element for the empty heap.")
        return self._root.value

    def clear(self):
        self._root = None

    @staticmethod
    def from_list(data: Iterable[T]) -> SkewHeap[T]:
        """Get the sorted list from the heap. Heap will be cleared afterwards."""
        result = SkewHeap()
        for item in data:
            result.insert(item)

        return result

    def to_sorted_list(self) -> List[T]:
        """Returns sorted list containing all the values in the heap."""
        result = []
        while self:
            result.append(self.pop())

        return result

    def __bool__(self) -> bool:
        """Check if the heap is not empty."""
        return self._root is not None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
