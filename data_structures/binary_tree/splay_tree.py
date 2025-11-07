"""
Splay Tree implementation in Python.

A Splay Tree is a self-adjusting binary search tree where recently accessed
elements are moved closer to the root using rotations (splaying).
This improves access times for frequently used elements.

Reference: https://en.wikipedia.org/wiki/Splay_tree
Author: yeshuawm999
"""

<<<<<<< HEAD

# class node
class Node:
    """A node in the Splay Tree."""

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key  # The value stored in the node
        self.parent = parent  # Pointer to the parent node
        self.left = left  # Pointer to the left child
        self.right = right  # Pointer to the right child


# Spary Tree class
class SplayTree:
    """A self-adjusting Binary Search Tree."""

    def __init__(self):
        self.root = None  # The root of the tree

    # --- Basic Rotation Operations ---

    def _rotate_left(self, x):
=======
from __future__ import annotations
from typing import Optional


class Node:
    """A node in the Splay Tree."""

    def __init__(
        self,
        key: int,
        parent: Optional[Node] = None,
        left: Optional[Node] = None,
        right: Optional[Node] = None,
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
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
        """Perform a left rotation around node x (moving x down and right)."""
        y = x.right
        if not y:
            return
        x.right = y.left
        if y.left:
            y.left.parent = x

<<<<<<< HEAD
        # 2. Update y's parent to be x's parent
        y.parent = x.parent
        if not x.parent:
            self.root = y  # y becomes the new root
=======
        y.parent = x.parent
        if not x.parent:
            self.root = y
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

<<<<<<< HEAD
        # 3. Update y's left child to be x
=======
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
        y.left = x
        x.parent = y

    def _rotate_right(self, x: Node) -> None:
        """Perform a right rotation around node x (moving x down and left)."""
        y = x.left
        if not y:
            return
        x.left = y.right
        if y.right:
            y.right.parent = x

<<<<<<< HEAD
        # 2. Update y's parent to be x's parent
        y.parent = x.parent
        if not x.parent:
            self.root = y  # y becomes the new new root
=======
        y.parent = x.parent
        if not x.parent:
            self.root = y
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

<<<<<<< HEAD
        # 3. Update y's right child to be x
=======
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
        y.right = x
        x.parent = y

    # --- Core Splay Operation ---

<<<<<<< HEAD
    def _splay(self, x):
=======
    def _splay(self, x: Node) -> None:
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
        """Moves node x to the root of the tree using a sequence of rotations."""
        while x.parent:
            parent = x.parent
            grandparent = parent.parent

            if not grandparent:
                # Zig Case (x is a child of the root)
                # One single rotation (Right if left child, Left if right child)
                if x == parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)
<<<<<<< HEAD

            else:
                # Two rotations are performed: Zig-Zig or Zig-Zag

                # Case 1: Zig-Zig (x, parent, and grandparent are all on one side)
                if x == parent.left and parent == grandparent.left:
                    # x and parent are both left children (Left-Left)
                    self._rotate_right(grandparent)  # Rotate grandparent down
                    self._rotate_right(parent)  # Rotate parent down
                elif x == parent.right and parent == grandparent.right:
                    # x and parent are both right children (Right-Right)
                    self._rotate_left(grandparent)  # Rotate grandparent down
                    self._rotate_left(parent)  # Rotate parent down

                # Case 2: Zig-Zag (x is on one side, parent is on the other)
                elif x == parent.left and parent == grandparent.right:
                    # x is left child, parent is right child
                    self._rotate_right(parent)  # Rotate parent first
                    self._rotate_left(grandparent)  # Rotate grandparent next
                else:  # x == parent.right and parent == grandparent.left
                    # x is right child, parent is left child
                    self._rotate_left(parent)  # Rotate parent first
                    self._rotate_right(grandparent)  # Rotate grandparent next

    # --- Example Search Method (Uses splay) ---

    def search(self, key):
        """Searches for a key. If found, splays it to the root."""
=======

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
            else:
                # Case 2: Zig-Zag (x is right child, parent is left child)
                self._rotate_left(parent)
                self._rotate_right(grandparent)

    # --- Search Method (Uses splay) ---

    def search(self, key: int) -> bool:
        """Search for a key. If found, splay it to the root."""
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
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
<<<<<<< HEAD
            self._splay(found_node)  # Node is brought to the root
=======
            self._splay(found_node)
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
            return True
        return False


<<<<<<< HEAD
=======
# --- Example Usage (for TheAlgorithms CI testing) ---
>>>>>>> 5d5b0f04 (Fixed lint issues, added type hints, and cleaned Splay Tree implementation)
if __name__ == "__main__":
    """
    Example:
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
