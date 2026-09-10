"""
Splay Tree - a self-adjusting binary search tree.

A splay tree is a binary search tree with the additional property that
recently accessed elements are quick to access again.  Every access (search,
insert or delete) moves the target node to the root through a sequence of
rotations called "splaying".  This gives an amortized time complexity of
O(log n) per operation and makes the tree very efficient when the access
pattern has locality of reference (a small subset of keys is touched often).

Reference: https://en.wikipedia.org/wiki/Splay_tree
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field


@dataclass
class Node:
    """
    A single node of a splay tree.

    The ``left`` and ``right`` children are excluded from ``repr`` so that a
    node prints compactly instead of recursively dumping the whole subtree.

    >>> Node(10)
    Node(key=10)
    """

    key: int
    left: Node | None = field(default=None, repr=False)
    right: Node | None = field(default=None, repr=False)


class SplayTree:
    """
    A self-adjusting binary search tree.

    >>> tree = SplayTree()
    >>> tree.insert(10)
    >>> tree.insert(20)
    >>> tree.insert(30)
    >>> tree.root.key  # last inserted key is splayed to the root
    30
    >>> tree.search(10)
    True
    >>> tree.root.key  # the searched key is now the root
    10
    >>> tree.search(99)
    False
    >>> list(tree)
    [10, 20, 30]
    """

    def __init__(self) -> None:
        self.root: Node | None = None

    def _rotate_right(self, node: Node) -> Node:
        """
        Perform a right rotation around ``node`` and return the new subtree root.

            node            left
           /    \\          /    \\
         left    c   -->   a     node
        /   \\                   /    \\
       a     b                 b      c
        """
        left = node.left
        assert left is not None
        node.left = left.right
        left.right = node
        return left

    def _rotate_left(self, node: Node) -> Node:
        """
        Perform a left rotation around ``node`` and return the new subtree root.

           node                 right
          /    \\               /     \\
         a     right   -->    node     c
              /     \\        /    \\
             b       c       a      b
        """
        right = node.right
        assert right is not None
        node.right = right.left
        right.left = node
        return right

    def _splay(self, root: Node | None, key: int) -> Node | None:
        """
        Splay the node with ``key`` (or the last node on the search path if
        ``key`` is absent) to the root of the subtree and return the new root.
        This uses the classic bottom-up recursive formulation.
        """
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                # Zig-Zig (left left)
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:
                # Zig-Zag (left right)
                root.left.right = self._splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self._rotate_left(root.left)
            return root if root.left is None else self._rotate_right(root)
        else:
            if root.right is None:
                return root
            if key > root.right.key:
                # Zig-Zig (right right)
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            elif key < root.right.key:
                # Zig-Zag (right left)
                root.right.left = self._splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self._rotate_right(root.right)
            return root if root.right is None else self._rotate_left(root)

    def insert(self, key: int) -> None:
        """
        Insert ``key`` into the tree and splay it to the root.

        >>> tree = SplayTree()
        >>> for key in (5, 3, 8, 3):  # duplicate keys are ignored
        ...     tree.insert(key)
        >>> list(tree)
        [3, 5, 8]
        >>> tree.root.key  # the duplicate access splays 3 back to the root
        3
        """
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self._splay(self.root, key)
        assert self.root is not None
        if self.root.key == key:
            return  # key already present, it is now at the root

        node = Node(key)
        if key < self.root.key:
            node.right = self.root
            node.left = self.root.left
            self.root.left = None
        else:
            node.left = self.root
            node.right = self.root.right
            self.root.right = None
        self.root = node

    def search(self, key: int) -> bool:
        """
        Return whether ``key`` is present and splay the last accessed node.

        >>> tree = SplayTree()
        >>> tree.search(1)
        False
        >>> for key in (40, 20, 60):
        ...     tree.insert(key)
        >>> tree.search(20)
        True
        >>> tree.root.key
        20
        """
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def delete(self, key: int) -> None:
        """
        Remove ``key`` from the tree if it is present.

        >>> tree = SplayTree()
        >>> for key in (10, 20, 30, 40):
        ...     tree.insert(key)
        >>> tree.delete(20)
        >>> list(tree)
        [10, 30, 40]
        >>> tree.delete(99)  # deleting an absent key is a no-op
        >>> list(tree)
        [10, 30, 40]
        >>> for key in (10, 30, 40):
        ...     tree.delete(key)
        >>> list(tree)
        []
        """
        if self.root is None:
            return

        self.root = self._splay(self.root, key)
        assert self.root is not None
        if self.root.key != key:
            return  # key not found

        left, right = self.root.left, self.root.right
        if left is None:
            self.root = right
        else:
            # Splay the maximum of the left subtree to its root; it has no
            # right child, so the right subtree can be attached there.
            left = self._splay(left, key)
            assert left is not None
            left.right = right
            self.root = left

    def __iter__(self) -> Iterator[int]:
        """
        Yield the keys of the tree in ascending (in-order) order.

        >>> tree = SplayTree()
        >>> for key in (7, 2, 9, 4, 1):
        ...     tree.insert(key)
        >>> list(tree)
        [1, 2, 4, 7, 9]
        """

        def in_order(node: Node | None) -> Iterator[int]:
            if node is not None:
                yield from in_order(node.left)
                yield node.key
                yield from in_order(node.right)

        yield from in_order(self.root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
