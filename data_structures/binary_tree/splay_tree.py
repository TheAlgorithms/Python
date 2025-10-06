"""
Splay Tree implementation

A splay tree is a self-adjusting binary search tree where recently accessed
elements are quick to access again. It performs basic operations such as
insertion, look-up and removal in O(log n) amortized time.

Reference: https://en.wikipedia.org/wiki/Splay_tree
"""

from __future__ import annotations
from typing import Any, Iterator


class SplayNode:
    """Node class for Splay Tree"""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: SplayNode | None = None
        self.right: SplayNode | None = None


class SplayTree:
    """
    Splay Tree implementation with basic operations

    >>> tree = SplayTree()
    >>> tree.insert(10)
    >>> tree.insert(5)
    >>> tree.insert(15)
    >>> tree.search(5)
    True
    >>> tree.search(20)
    False
    >>> tree.delete(5)
    >>> tree.search(5)
    False
    >>> list(tree.inorder())
    [10, 15]
    """

    def __init__(self) -> None:
        self.root: SplayNode | None = None

    def _right_rotate(self, node: SplayNode) -> SplayNode:
        """Right rotation for splay operation"""
        left_child = node.left
        if left_child is None:
            return node
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _left_rotate(self, node: SplayNode) -> SplayNode:
        """Left rotation for splay operation"""
        right_child = node.right
        if right_child is None:
            return node
        node.right = right_child.left
        right_child.left = node
        return right_child

    def _splay(self, root: SplayNode | None, key: Any) -> SplayNode | None:
        """
        Splay operation to move accessed node to root
        """
        if root is None or root.data == key:
            return root

        # Key is in left subtree
        if key < root.data:
            if root.left is None:
                return root

            # Zig-Zig (Left Left)
            if key < root.left.data:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)

            # Zig-Zag (Left Right)
            elif key > root.left.data:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)

            return self._right_rotate(root) if root.left else root

        # Key is in right subtree
        else:
            if root.right is None:
                return root

            # Zag-Zag (Right Right)
            if key > root.right.data:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)

            # Zag-Zig (Right Left)
            elif key < root.right.data:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)

            return self._left_rotate(root) if root.right else root

    def insert(self, key: Any) -> None:
        """
        Insert a key into the splay tree

        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.root.data
        10
        """
        if self.root is None:
            self.root = SplayNode(key)
            return

        self.root = self._splay(self.root, key)

        if self.root.data == key:
            return  # Key already exists

        new_node = SplayNode(key)

        if key < self.root.data:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def search(self, key: Any) -> bool:
        """
        Search for a key in the splay tree

        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.search(10)
        True
        >>> tree.search(5)
        False
        """
        if self.root is None:
            return False

        self.root = self._splay(self.root, key)
        return self.root.data == key

    def delete(self, key: Any) -> None:
        """
        Delete a key from the splay tree

        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.delete(5)
        >>> tree.search(5)
        False
        """
        if self.root is None:
            return

        self.root = self._splay(self.root, key)

        if self.root.data != key:
            return  # Key not found

        if self.root.left is None:
            self.root = self.root.right
        elif self.root.right is None:
            self.root = self.root.left
        else:
            temp = self.root
            self.root = self._splay(self.root.left, key)
            self.root.right = temp.right

    def inorder(self) -> Iterator[Any]:
        """
        Inorder traversal of the splay tree

        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> list(tree.inorder())
        [5, 10, 15]
        """
        yield from self._inorder_helper(self.root)

    def _inorder_helper(self, node: SplayNode | None) -> Iterator[Any]:
        """Helper method for inorder traversal"""
        if node:
            yield from self._inorder_helper(node.left)
            yield node.data
            yield from self._inorder_helper(node.right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    tree = SplayTree()
    elements = [10, 5, 15, 3, 7, 12, 18]

    print("Inserting elements:", elements)
    for elem in elements:
        tree.insert(elem)

    print("Inorder traversal:", list(tree.inorder()))

    print("Searching for 7:", tree.search(7))
    print("Searching for 20:", tree.search(20))

    tree.delete(5)
    print("After deleting 5:", list(tree.inorder()))
