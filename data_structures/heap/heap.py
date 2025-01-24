from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable
from typing import Generic, Protocol, TypeVar


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        pass

    @abstractmethod
    def __gt__(self: T, other: T) -> bool:
        pass

    @abstractmethod
    def __eq__(self: T, other: object) -> bool:
        pass


T = TypeVar("T", bound=Comparable)


class Heap(Generic[T]):
    """A Max Heap Implementation

    >>> unsorted = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
    >>> h = Heap()
    >>> h.build_max_heap(unsorted)
    >>> h
    [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]
    >>>
    >>> h.extract_max()
    209
    >>> h
    [201, 107, 25, 103, 11, 15, 1, 9, 7, 5]
    >>>
    >>> h.insert(100)
    >>> h
    [201, 107, 25, 103, 100, 15, 1, 9, 7, 5, 11]
    >>>
    >>> h.heap_sort()
    >>> h
    [1, 5, 7, 9, 11, 15, 25, 100, 103, 107, 201]
    """

    def __init__(self) -> None:
        self.h: list[T] = []
        self.heap_size: int = 0

    def __repr__(self) -> str:
        return str(self.h)

    def parent_index(self, child_idx: int) -> int | None:
        """
        returns the parent index based on the given child index

        >>> h = Heap()
        >>> h.build_max_heap([103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5])
        >>> h
        [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]

        >>> h.parent_index(-1)  # returns none if index is <=0

        >>> h.parent_index(0)   # returns none if index is <=0

        >>> h.parent_index(1)
        0
        >>> h.parent_index(2)
        0
        >>> h.parent_index(3)
        1
        >>> h.parent_index(4)
        1
        >>> h.parent_index(5)
        2
        >>> h.parent_index(10.5)
        4.0
        >>> h.parent_index(209.0)
        104.0
        >>> h.parent_index("Test")
        Traceback (most recent call last):
        ...
        TypeError: '>' not supported between instances of 'str' and 'int'
        """
        if child_idx > 0:
            return (child_idx - 1) // 2
        return None

    def left_child_idx(self, parent_idx: int) -> int | None:
        """
        return the left child index if the left child exists.
        if not, return None.
        """
        left_child_index = 2 * parent_idx + 1
        if left_child_index < self.heap_size:
            return left_child_index
        return None

    def right_child_idx(self, parent_idx: int) -> int | None:
        """
        return the right child index if the right child exists.
        if not, return None.
        """
        right_child_index = 2 * parent_idx + 2
        if right_child_index < self.heap_size:
            return right_child_index
        return None

    def max_heapify(self, index: int) -> None:
        """
        correct a single violation of the heap property in a subtree's root.

        It is the function that is responsible for restoring the property
        of Max heap i.e the maximum element is always at top.
        """
        if index < self.heap_size:
            violation: int = index
            left_child = self.left_child_idx(index)
            right_child = self.right_child_idx(index)
            # check which child is larger than its parent
            if left_child is not None and self.h[left_child] > self.h[violation]:
                violation = left_child
            if right_child is not None and self.h[right_child] > self.h[violation]:
                violation = right_child
            # if violation indeed exists
            if violation != index:
                # swap to fix the violation
                self.h[violation], self.h[index] = self.h[index], self.h[violation]
                # fix the subsequent violation recursively if any
                self.max_heapify(violation)

    def build_max_heap(self, collection: Iterable[T]) -> None:
        """
        build max heap from an unsorted array

        >>> h = Heap()
        >>> h.build_max_heap([20,40,50,20,10])
        >>> h
        [50, 40, 20, 20, 10]

        >>> h = Heap()
        >>> h.build_max_heap([1,2,3,4,5,6,7,8,9,0])
        >>> h
        [9, 8, 7, 4, 5, 6, 3, 2, 1, 0]

        >>> h = Heap()
        >>> h.build_max_heap([514,5,61,57,8,99,105])
        >>> h
        [514, 57, 105, 5, 8, 99, 61]

        >>> h = Heap()
        >>> h.build_max_heap([514,5,61.6,57,8,9.9,105])
        >>> h
        [514, 57, 105, 5, 8, 9.9, 61.6]
        """
        self.h = list(collection)
        self.heap_size = len(self.h)
        if self.heap_size > 1:
            # max_heapify from right to left but exclude leaves (last level)
            for i in range(self.heap_size // 2 - 1, -1, -1):
                self.max_heapify(i)

    def extract_max(self) -> T:
        """
        get and remove max from heap

        >>> h = Heap()
        >>> h.build_max_heap([20,40,50,20,10])
        >>> h.extract_max()
        50

        >>> h = Heap()
        >>> h.build_max_heap([514,5,61,57,8,99,105])
        >>> h.extract_max()
        514

        >>> h = Heap()
        >>> h.build_max_heap([1,2,3,4,5,6,7,8,9,0])
        >>> h.extract_max()
        9
        """
        if self.heap_size >= 2:
            me = self.h[0]
            self.h[0] = self.h.pop(-1)
            self.heap_size -= 1
            self.max_heapify(0)
            return me
        elif self.heap_size == 1:
            self.heap_size -= 1
            return self.h.pop(-1)
        else:
            raise Exception("Empty heap")

    def insert(self, value: T) -> None:
        """
        insert a new value into the max heap

        >>> h = Heap()
        >>> h.insert(10)
        >>> h
        [10]

        >>> h = Heap()
        >>> h.insert(10)
        >>> h.insert(10)
        >>> h
        [10, 10]

        >>> h = Heap()
        >>> h.insert(10)
        >>> h.insert(10.1)
        >>> h
        [10.1, 10]

        >>> h = Heap()
        >>> h.insert(0.1)
        >>> h.insert(0)
        >>> h.insert(9)
        >>> h.insert(5)
        >>> h
        [9, 5, 0.1, 0]
        """
        self.h.append(value)
        idx = (self.heap_size - 1) // 2
        self.heap_size += 1
        while idx >= 0:
            self.max_heapify(idx)
            idx = (idx - 1) // 2

    def heap_sort(self) -> None:
        size = self.heap_size
        for j in range(size - 1, 0, -1):
            self.h[0], self.h[j] = self.h[j], self.h[0]
            self.heap_size -= 1
            self.max_heapify(0)
        self.heap_size = size


if __name__ == "__main__":
    import doctest

    # run doc test
    doctest.testmod()

    # demo
    for unsorted in [
        [0],
        [2],
        [3, 5],
        [5, 3],
        [5, 5],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 3, 5],
        [0, 2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [-45, -2, -5],
    ]:
        print(f"unsorted array: {unsorted}")

        heap: Heap[int] = Heap()
        heap.build_max_heap(unsorted)
        print(f"after build heap: {heap}")

        print(f"max value: {heap.extract_max()}")
        print(f"after max value removed: {heap}")

        heap.insert(100)
        print(f"after new value 100 inserted: {heap}")

        heap.heap_sort()
        print(f"heap-sorted array: {heap}\n")
