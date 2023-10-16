"""
Tree_sort algorithm.

Build a Binary Search Tree and then iterate thru it to get a sorted list.
"""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.val
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def insert(self, val: int) -> None:
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)


def tree_sort(arr: list[int]) -> tuple[int, ...]:
    """
    >>> tree_sort([])
    ()
    >>> tree_sort((1,))
    (1,)
    >>> tree_sort((1, 2))
    (1, 2)
    >>> tree_sort([5, 2, 7])
    (2, 5, 7)
    >>> tree_sort((5, -4, 9, 2, 7))
    (-4, 2, 5, 7, 9)
    >>> tree_sort([5, 6, 1, -1, 4, 37, 2, 7])
    (-1, 1, 2, 4, 5, 6, 7, 37)

    # >>> tree_sort(range(10, -10, -1)) == tuple(sorted(range(10, -10, -1)))
    # True
    """
    if len(arr) == 0:
        return tuple(arr)
    root = Node(arr[0])
    for item in arr[1:]:
        root.insert(item)
    return tuple(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{tree_sort([5, 6, 1, -1, 4, 37, -3, 7]) = }")
