"""
In a binary search tree (BST):
* The floor of key 'k' is the maximum value that is smaller than or equal to 'k'.
* The ceiling of key 'k' is the minimum value that is greater than or equal to 'k'.

Reference:
https://bit.ly/46uB0a2

Author : Arunkumar
Date : 14th October 2023
"""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.key
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)


def floor_ceiling(root: Node | None, key: int) -> tuple[int | None, int | None]:
    """
    Find the floor and ceiling values for a given key in a Binary Search Tree (BST).

    Args:
        root: The root of the binary search tree.
        key: The key for which to find the floor and ceiling.

    Returns:
        A tuple containing the floor and ceiling values, respectively.

    Examples:
        >>> root = Node(10)
        >>> root.left = Node(5)
        >>> root.right = Node(20)
        >>> root.left.left = Node(3)
        >>> root.left.right = Node(7)
        >>> root.right.left = Node(15)
        >>> root.right.right = Node(25)
        >>> tuple(root)
        (3, 5, 7, 10, 15, 20, 25)
        >>> floor_ceiling(root, 8)
        (7, 10)
        >>> floor_ceiling(root, 14)
        (10, 15)
        >>> floor_ceiling(root, -1)
        (None, 3)
        >>> floor_ceiling(root, 30)
        (25, None)
    """
    floor_val = None
    ceiling_val = None

    while root:
        if root.key == key:
            floor_val = root.key
            ceiling_val = root.key
            break

        if key < root.key:
            ceiling_val = root.key
            root = root.left
        else:
            floor_val = root.key
            root = root.right

    return floor_val, ceiling_val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
