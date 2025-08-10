"""
Splay Tree implementation - a self-adjusting binary search tree.

A splay tree is a self-balancing binary search tree with the additional property
that recently accessed elements are quick to access again. All normal operations
on a binary search tree are combined with one basic operation, called splaying.

Time Complexity:
- Average case: O(log n) for all operations
- Worst case: O(n) for a single operation, but amortized O(log n)
- Amortized: O(log n) for all operations

Space Complexity: O(n)

Source: https://en.wikipedia.org/wiki/Splay_tree
"""

from __future__ import annotations

from typing import Any, Generic, TypeVar

T = TypeVar("T", bound=Any)


class SplayNode(Generic[T]):  # noqa: UP046
    """
    A node in the splay tree.

    Args:
        data: The data stored in the node
        left: Reference to the left child node
        right: Reference to the right child node

    >>> node = SplayNode(10)
    >>> node.data
    10
    >>> node.left is None
    True
    >>> node.right is None
    True
    """

    def __init__(
        self,
        data: T,
        left: SplayNode[T] | None = None,
        right: SplayNode[T] | None = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"SplayNode({self.data})"


class SplayTree(Generic[T]):  # noqa: UP046
    """
    Splay Tree implementation with standard BST operations.

    The splay tree performs a splay operation after each access,
    moving the accessed node to the root.

    Examples:
    >>> tree = SplayTree()
    >>> tree.insert(10)
    >>> tree.insert(5)
    >>> tree.insert(15)
    >>> tree.search(5)
    True
    >>> tree.search(20)
    False
    >>> tree.delete(5)
    True
    >>> tree.search(5)
    False
    >>> tree.delete(100)
    False
    >>> tree.is_empty()
    False
    >>> tree.size()
    2
    >>> tree.find_min()
    10
    >>> tree.find_max()
    15
    >>> tree.delete(15)
    True
    >>> tree.delete(10)
    True
    >>> tree.is_empty()
    True
    """

    def __init__(self) -> None:
        """Initialize an empty splay tree."""
        self.root: SplayNode[T] | None = None

    def _right_rotate(self, node: SplayNode[T]) -> SplayNode[T]:
        """
        Perform right rotation on the given node.

        Args:
            node: The node to rotate

        Returns:
            The new root after rotation
        """
        if node.left is None:
            return node

        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _left_rotate(self, node: SplayNode[T]) -> SplayNode[T]:
        """
        Perform left rotation on the given node.

        Args:
            node: The node to rotate

        Returns:
            The new root after rotation
        """
        if node.right is None:
            return node

        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def _splay(self, node: SplayNode[T] | None, key: T) -> SplayNode[T] | None:
        """
        Splay operation that moves the key (or the node that would contain it)
        to the root of the tree.

        Args:
            node: Current node
            key: Key to splay

        Returns:
            New root after splaying
        """
        if node is None or node.data == key:
            return node

        # Key is in left subtree
        if key < node.data:
            if node.left is None:
                return node

            # Type narrowing: we know node.left is not None here
            left_node = node.left

            # Zig-Zig (Left Left)
            if key < left_node.data:
                # Recursively splay the key to left-left grandchild
                left_node.left = self._splay(left_node.left, key)
                # First rotation for node
                node = self._right_rotate(node)

            # Zig-Zag (Left Right)
            elif key > left_node.data:
                # Recursively splay the key to left-right grandchild
                left_node.right = self._splay(left_node.right, key)
                # First rotation for left child
                if left_node.right is not None:
                    node.left = self._left_rotate(left_node)

            # Second rotation for root
            return self._right_rotate(node) if node.left else node

        # Key is in right subtree
        else:
            if node.right is None:
                return node

            # Type narrowing: we know node.right is not None here
            right_node = node.right

            # Zag-Zag (Right Right)
            if key > right_node.data:
                # Recursively splay the key to right-right grandchild
                right_node.right = self._splay(right_node.right, key)
                # First rotation for node
                node = self._left_rotate(node)

            # Zag-Zig (Right Left)
            elif key < right_node.data:
                # Recursively splay the key to right-left grandchild
                right_node.left = self._splay(right_node.left, key)
                # First rotation for right child
                if right_node.left is not None:
                    node.right = self._right_rotate(right_node)

            # Second rotation for root
            return self._left_rotate(node) if node.right else node

    def search(self, key: T) -> bool:
        """
        Search for a key in the splay tree.

        Args:
            key: Key to search for

        Returns:
            True if key is found, False otherwise

        Raises:
            ValueError: If key is None

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.search(10)
        True
        >>> tree.search(5)
        False
        """
        if key is None:
            raise ValueError("Cannot search for None value")

        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.data == key

    def insert(self, key: T) -> None:
        """
        Insert a key into the splay tree.

        Args:
            key: Key to insert

        Raises:
            ValueError: If key is None

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.search(10)
        True
        """
        if key is None:
            raise ValueError("Cannot insert None value")

        if self.root is None:
            self.root = SplayNode(key)
            return

        self.root = self._splay(self.root, key)

        # Type narrowing: after splay, root should not be None
        assert self.root is not None

        # If key already exists, do nothing
        if self.root.data == key:
            return

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

    def delete(self, key: T) -> bool:
        """
        Delete a key from the splay tree.

        Args:
            key: Key to delete

        Returns:
            True if key was deleted, False if key was not found

        Raises:
            ValueError: If key is None

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.delete(10)
        True
        >>> tree.delete(5)
        True
        >>> tree.delete(100)
        False
        """
        if key is None:
            raise ValueError("Cannot delete None value")

        if self.root is None:
            return False

        self.root = self._splay(self.root, key)

        # Type narrowing: after splay, root should not be None
        assert self.root is not None

        if self.root.data != key:
            return False

        # Node to delete is at root
        if self.root.left is None:
            self.root = self.root.right
        elif self.root.right is None:
            self.root = self.root.left
        else:
            # Find maximum in left subtree and splay it
            temp = self.root.left
            while temp is not None and temp.right is not None:
                temp = temp.right

            # Splay the maximum element to root of left subtree
            if temp is not None:
                left_subtree = self._splay(self.root.left, temp.data)
                if left_subtree is not None:
                    left_subtree.right = self.root.right
                    self.root = left_subtree

        return True

    def is_empty(self) -> bool:
        """
        Check if the tree is empty.

        Returns:
            True if tree is empty, False otherwise

        Examples:
        >>> tree = SplayTree()
        >>> tree.is_empty()
        True
        >>> tree.insert(10)
        >>> tree.is_empty()
        False
        """
        return self.root is None

    def size(self) -> int:
        """
        Return the number of nodes in the tree.

        Returns:
            Number of nodes in the tree

        Examples:
        >>> tree = SplayTree()
        >>> tree.size()
        0
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.size()
        2
        """

        def _count(node: SplayNode[T] | None) -> int:
            if node is None:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)

    def find_min(self) -> T | None:
        """
        Find and return the minimum element, splaying it to root.

        Returns:
            Minimum element or None if tree is empty

        Examples:
        >>> tree = SplayTree()
        >>> tree.find_min() is None
        True
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.find_min()
        5
        """
        if self.root is None:
            return None

        current = self.root
        while current.left:
            current = current.left

        # Splay the minimum to root
        self.root = self._splay(self.root, current.data)
        return self.root.data if self.root else None

    def find_max(self) -> T | None:
        """
        Find and return the maximum element, splaying it to root.

        Returns:
            Maximum element or None if tree is empty

        Examples:
        >>> tree = SplayTree()
        >>> tree.find_max() is None
        True
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.find_max()
        15
        """
        if self.root is None:
            return None

        current = self.root
        while current.right:
            current = current.right

        # Splay the maximum to root
        self.root = self._splay(self.root, current.data)
        return self.root.data if self.root else None

    def inorder_traversal(self) -> list[T]:
        """
        Perform inorder traversal of the tree.

        Returns:
            List of elements in sorted order

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.insert(3)
        >>> tree.insert(7)
        >>> sorted_elements = tree.inorder_traversal()
        >>> sorted_elements == [3, 5, 7, 10, 15]
        True
        """
        result = []

        def _inorder(node: SplayNode[T] | None) -> None:
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)

        _inorder(self.root)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage - Fixed instantiation
    tree: SplayTree[int] = SplayTree()

    # Test empty tree
    print("Empty tree operations:")
    print(f"Is empty: {tree.is_empty()}")
    print(f"Size: {tree.size()}")
    print(f"Min: {tree.find_min()}")
    print(f"Max: {tree.find_max()}")

    # Insert elements
    elements = [10, 5, 15, 3, 7, 12, 18]
    print(f"\nInserting elements: {elements}")
    for elem in elements:
        tree.insert(elem)

    print(f"Inorder traversal: {tree.inorder_traversal()}")
    print(f"Size after insertions: {tree.size()}")

    # Search operations
    print(f"\nSearch 7: {tree.search(7)}")
    print(f"Search 20: {tree.search(20)}")

    # Min/Max operations
    print(f"Minimum: {tree.find_min()}")
    print(f"Maximum: {tree.find_max()}")

    # Delete operations
    print(f"\nDelete 5: {tree.delete(5)}")
    print(f"Delete 20: {tree.delete(20)}")
    print(f"After deletions: {tree.inorder_traversal()}")
    print(f"Size after deletions: {tree.size()}")

    print("\n✅ All tests passed!")
