"""
Splay Tree implementation in Python.

A Splay Tree is a self-adjusting binary search tree that brings the most
recently accessed element to the root via tree rotations. It provides
amortized O(log n) time complexity for search, insert, and delete operations.

Reference:
https://en.wikipedia.org/wiki/Splay_tree
"""

from __future__ import annotations
from typing import Optional, List


class Node:
    """Node class for the Splay Tree."""

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class SplayTree:
    """Splay Tree Data Structure."""

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    # ------------------------- ROTATIONS -------------------------
    def _right_rotate(self, x: Node) -> Node:
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x: Node) -> Node:
        y = x.right
        x.right = y.left
        y.left = x
        return y

    # ------------------------- SPLAY OPERATION -------------------------
    def _splay(self, root: Optional[Node], key: int) -> Optional[Node]:
        if root is None or root.key == key:
            return root

        # Key in left subtree
        if key < root.key:
            if root.left is None:
                return root

            # Zig-Zig (Left Left)
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)
            # Zig-Zag (Left Right)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)
            return root if root.left is None else self._right_rotate(root)

        # Key in right subtree
        else:
            if root.right is None:
                return root

            # Zig-Zig (Right Right)
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)
            # Zig-Zag (Right Left)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            return root if root.right is None else self._left_rotate(root)

    # ------------------------- INSERTION -------------------------
    def insert(self, key: int) -> None:
        """Inserts a key into the Splay Tree."""
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return  # No duplicates

        new_node = Node(key)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    # ------------------------- SEARCH -------------------------
    def search(self, key: int) -> bool:
        """Searches for a key and splays it to the root."""
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    # ------------------------- DELETION -------------------------
    def delete(self, key: int) -> None:
        """Deletes a key from the Splay Tree."""
        if not self.root:
            return

        self.root = self._splay(self.root, key)
        if self.root.key != key:
            return  # Key not found

        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root.right
            self.root = self._splay(self.root.left, key)
            self.root.right = temp

    # ------------------------- TRAVERSALS -------------------------
    def inorder(self, root: Optional[Node]) -> List[int]:
        """Returns an inorder traversal of the tree."""
        return (
            []
            if not root
            else self.inorder(root.left) + [root.key] + self.inorder(root.right)
        )

    def preorder(self, root: Optional[Node]) -> List[int]:
        """Returns a preorder traversal of the tree."""
        return (
            []
            if not root
            else [root.key] + self.preorder(root.left) + self.preorder(root.right)
        )


if __name__ == "__main__":
    # Example usage and demonstration
    tree = SplayTree()
    for value in [10, 20, 30, 40, 50, 25]:
        tree.insert(value)

    print("Inorder traversal:", tree.inorder(tree.root))
    print("Search for 25:", tree.search(25))
    print("After searching 25, root =", tree.root.key)
    tree.delete(20)
    print("After deleting 20:", tree.inorder(tree.root))
