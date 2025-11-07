"""
Splay Tree implementation in Python.

A Splay Tree is a self-adjusting binary search tree where recently accessed
elements are moved closer to the root using rotations (splaying).
This improves access times for frequently used elements.

Reference: https://en.wikipedia.org/wiki/Splay_tree
Author: yeshuawm999
"""

from __future__ import annotations
from typing import Optional


class Node:
    """A node in the Splay Tree."""

    def __init__(
        self,
        key: int,
        parent: Optional["Node"] = None,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
    ) -> None:
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class SplayTree:
    """A self-adjusting Binary Search Tree (Splay Tree)."""

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    # --- Basic Rotation Operations ---

    def _rotate_left(self, x: Node) -> None:
        """Perform a left rotation around node x."""
        y = x.right
        if not y:
            return
        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, x: Node) -> None:
        """Perform a right rotation around node x."""
        y = x.left
        if not y:
            return
        x.left = y.right
        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # --- Core Splay Operation ---

    def _splay(self, x: Node) -> None:
        """Moves node x to the root of the tree using a sequence of rotations."""
        while x.parent:
            parent = x.parent
            grandparent = parent.parent

            if not grandparent:
                # Zig Case (x is a child of the root)
                # One single rotation:
                # Right if x is a left child, Left if x is a right child
                if x == parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)

            # Two rotations are performed: Zig-Zig or Zig-Zag
            elif x == parent.left and parent == grandparent.left:
                # Case 1: Zig-Zig (x, parent, and grandparent all on left)
                self._rotate_right(grandparent)
                self._rotate_right(parent)
            elif x == parent.right and parent == grandparent.right:
                # Case 1: Zig-Zig (x, parent, and grandparent all on right)
                self._rotate_left(grandparent)
                self._rotate_left(parent)
            elif x == parent.left and parent == grandparent.right:
                # Case 2: Zig-Zag (x is left child, parent is right child)
                self._rotate_right(parent)
                self._rotate_left(grandparent)
            elif x == parent.right and parent == grandparent.left:
                # Case 2: Zig-Zag (x is right child, parent is left child)
                self._rotate_left(parent)
                self._rotate_right(grandparent)

    # --- Search Method (Uses splay) ---

    def search(self, key: int) -> bool:
        """Search for a key. If found, splay it to the root."""
        current = self.root
        found_node = None
        while current:
            if key == current.key:
                found_node = current
                break
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if found_node:
            self._splay(found_node)
            return True
        return False


# --- Example Usage ---
if __name__ == "__main__":
    """
    Example run:
    >>> tree = SplayTree()
    >>> tree.root = Node(10)
    >>> tree.root.left = Node(5, parent=tree.root)
    >>> tree.root.right = Node(15, parent=tree.root)
    >>> print("Before search:", tree.root.key)
    >>> found = tree.search(5)
    >>> print("Found:", found)
    >>> print("After splay, new root:", tree.root.key)
    """

    tree = SplayTree()
    tree.root = Node(10)
    tree.root.left = Node(5, parent=tree.root)
    tree.root.right = Node(15, parent=tree.root)

    print("Before search:", tree.root.key)
    found = tree.search(5)
    print("Found:", found)
    print("After splay, new root:", tree.root.key)
