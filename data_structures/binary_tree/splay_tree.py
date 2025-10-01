"""
Splay Tree implementation - A self-adjusting binary search tree.

A Splay tree is a self-adjusting binary search tree where recently accessed
elements are moved to the root through rotations. This provides amortized
O(log n) time complexity for search, insert, and delete operations.

The splaying operation moves a node to the root by performing a series of
rotations, making frequently accessed elements faster to access in the future.

For more information, see: https://en.wikipedia.org/wiki/Splay_tree

Time Complexity (amortized):
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

Space Complexity: O(n)

Operations:
- Zig: Single rotation (when parent is root)
- Zig-zig: Double rotation in same direction
- Zig-zag: Double rotation in opposite directions

Example:
>>> tree = SplayTree()
>>> _ = tree.insert(10)
>>> _ = tree.insert(20)
>>> _ = tree.insert(30)
>>> _ = tree.insert(5)
>>> _ = tree.insert(15)
>>> list(tree.inorder())
[5, 10, 15, 20, 30]
>>> tree.search(15)
True
>>> tree.search(25)
False
>>> _ = tree.delete(20)
>>> list(tree.inorder())
[5, 10, 15, 30]
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Self


@dataclass
class SplayNode:
    """A node in the Splay Tree."""

    value: Any
    left: SplayNode | None = None
    right: SplayNode | None = None
    parent: SplayNode | None = None

    def __iter__(self) -> Iterator[Any]:
        """Inorder traversal iterator."""
        yield from self.left or []
        yield self.value
        yield from self.right or []

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    @property
    def is_right(self) -> bool:
        """Check if this node is the right child of its parent."""
        return bool(self.parent and self is self.parent.right)


@dataclass
class SplayTree:
    """
    Splay Tree implementation - A self-adjusting BST.

    This tree automatically moves recently accessed elements to the root
    through rotations, providing amortized O(log n) performance for all operations.
    """

    root: SplayNode | None = None

    def __bool__(self) -> bool:
        """Return True if the tree is not empty."""
        return self.root is not None

    def __iter__(self) -> Iterator[Any]:
        """Iterate over the tree in inorder traversal."""
        yield from self.root or []

    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        return sum(1 for _ in self)

    def __str__(self) -> str:
        """Return a string representation of the tree."""
        return str(self.root)

    def _rotate_right(self, node: SplayNode) -> None:
        """Perform a right rotation on the given node."""
        if not node.left:
            return

        left_child = node.left
        node.left = left_child.right

        if left_child.right:
            left_child.right.parent = node

        left_child.parent = node.parent

        if not node.parent:
            self.root = left_child
        elif node is node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def _rotate_left(self, node: SplayNode) -> None:
        """Perform a left rotation on the given node."""
        if not node.right:
            return

        right_child = node.right
        node.right = right_child.left

        if right_child.left:
            right_child.left.parent = node

        right_child.parent = node.parent

        if not node.parent:
            self.root = right_child
        elif node is node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _splay(self, node: SplayNode) -> None:
        """
        Splay the given node to the root through a series of rotations.

        The splaying operation uses three types of rotations:
        - Zig: Single rotation when parent is root
        - Zig-zig: Double rotation in same direction
        - Zig-zag: Double rotation in opposite directions
        """
        while node.parent:
            parent = node.parent
            grandparent = parent.parent

            if not grandparent:
                # Zig case: parent is root
                if node is parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)
            elif (node is parent.left and parent is grandparent.left) or (
                node is parent.right and parent is grandparent.right
            ):
                # Zig-zig case: same direction
                if parent is grandparent.left:
                    self._rotate_right(grandparent)
                    self._rotate_right(parent)
                else:
                    self._rotate_left(grandparent)
                    self._rotate_left(parent)
            elif node is parent.left:
                # Zig-zag case: opposite directions (left child)
                self._rotate_right(parent)
                self._rotate_left(grandparent)
            else:
                # Zig-zag case: opposite directions (right child)
                self._rotate_left(parent)
                self._rotate_right(grandparent)

    def _find_node(self, value: Any) -> SplayNode | None:
        """Find a node with the given value, splaying it to root if found."""
        current = self.root
        while current:
            if value == current.value:
                self._splay(current)
                return current
            elif value < current.value:
                if not current.left:
                    break
                current = current.left
            else:
                if not current.right:
                    break
                current = current.right

        # If we found a node (even if not exact match), splay it
        if current:
            self._splay(current)
        return None

    def search(self, value: Any) -> bool:
        """Search for a value in the tree. Returns True if found."""
        return self._find_node(value) is not None

    def insert(self, value: Any) -> Self:
        """Insert a value into the splay tree."""
        if not self.root:
            self.root = SplayNode(value)
            return self

        # Find the insertion point
        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = SplayNode(value, parent=current)
                    self._splay(current.left)
                    break
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = SplayNode(value, parent=current)
                    self._splay(current.right)
                    break
            else:
                # Value already exists, splay the existing node
                self._splay(current)
                break

        return self

    def delete(self, value: Any) -> Self:
        """Delete a value from the splay tree."""
        node = self._find_node(value)
        if not node:
            return self

        # Node to delete is now at root
        left_tree = node.left
        right_tree = node.right

        # Remove the root
        if left_tree:
            left_tree.parent = None
        if right_tree:
            right_tree.parent = None

        # If no left subtree, right becomes root
        if not left_tree:
            self.root = right_tree
            return self

        # Find the maximum in left subtree
        max_left = left_tree
        while max_left.right:
            max_left = max_left.right

        # Splay the maximum to root of left subtree
        self._splay(max_left)

        # Attach right subtree to the new root
        max_left.right = right_tree
        if right_tree:
            right_tree.parent = max_left

        self.root = max_left
        return self

    def inorder(self) -> Iterator[Any]:
        """Return an inorder iterator."""
        yield from self

    def preorder(self) -> Iterator[Any]:
        """Return a preorder iterator."""

        def _preorder(node: SplayNode | None) -> Iterator[Any]:
            if node:
                yield node.value
                yield from _preorder(node.left)
                yield from _preorder(node.right)

        yield from _preorder(self.root)

    def postorder(self) -> Iterator[Any]:
        """Return a postorder iterator."""

        def _postorder(node: SplayNode | None) -> Iterator[Any]:
            if node:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.value

        yield from _postorder(self.root)

    def get_min(self) -> Any:
        """Get the minimum value in the tree."""
        if not self.root:
            raise ValueError("Tree is empty")
        current = self.root
        while current.left:
            current = current.left
        self._splay(current)
        return current.value

    def get_max(self) -> Any:
        """Get the maximum value in the tree."""
        if not self.root:
            raise ValueError("Tree is empty")
        current = self.root
        while current.right:
            current = current.right
        self._splay(current)
        return current.value

    def is_empty(self) -> bool:
        """Check if the tree is empty."""
        return self.root is None

    def clear(self) -> Self:
        """Clear the tree."""
        self.root = None
        return self
