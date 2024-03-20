"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid binary search tree is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

In effect, a binary tree is a valid BST if its nodes are sorted in ascending order.
leetcode: https://leetcode.com/problems/validate-binary-search-tree/

If n is the number of nodes in the tree then:
Runtime: O(n)
Space: O(1)
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: float
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[float]:
        """
        >>> root = Node(data=2.1)
        >>> list(root)
        [2.1]
        >>> root.left=Node(data=2.0)
        >>> list(root)
        [2.0, 2.1]
        >>> root.right=Node(data=2.2)
        >>> list(root)
        [2.0, 2.1, 2.2]
        """
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    @property
    def is_sorted(self) -> bool:
        """
        >>> Node(data='abc').is_sorted
        True
        >>> Node(data=2,
        ...      left=Node(data=1.999),
        ...      right=Node(data=3)).is_sorted
        True
        >>> Node(data=0,
        ...      left=Node(data=0),
        ...      right=Node(data=0)).is_sorted
        True
        >>> Node(data=0,
        ...      left=Node(data=-11),
        ...      right=Node(data=3)).is_sorted
        True
        >>> Node(data=5,
        ...      left=Node(data=1),
        ...      right=Node(data=4, left=Node(data=3))).is_sorted
        False
        >>> Node(data='a',
        ...      left=Node(data=1),
        ...      right=Node(data=4, left=Node(data=3))).is_sorted
        Traceback (most recent call last):
            ...
        TypeError: '<' not supported between instances of 'str' and 'int'
        >>> Node(data=2,
        ...      left=Node([]),
        ...      right=Node(data=4, left=Node(data=3))).is_sorted
        Traceback (most recent call last):
            ...
        TypeError: '<' not supported between instances of 'int' and 'list'
        """
        if self.left and (self.data < self.left.data or not self.left.is_sorted):
            return False
        if self.right and (self.data > self.right.data or not self.right.is_sorted):
            return False
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    tree = Node(data=2.1, left=Node(data=2.0), right=Node(data=2.2))
    print(f"Tree {list(tree)} is sorted: {tree.is_sorted = }.")
    assert tree.right
    tree.right.data = 2.0
    print(f"Tree {list(tree)} is sorted: {tree.is_sorted = }.")
    tree.right.data = 2.1
    print(f"Tree {list(tree)} is sorted: {tree.is_sorted = }.")
