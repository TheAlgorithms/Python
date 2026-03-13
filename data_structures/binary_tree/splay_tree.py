"""
Splay Tree Implementation

A splay tree is a self-adjusting binary search tree with the additional property
that recently accessed elements are quick to access again. It performs basic
operations such as insertion, look-up and removal in O(log n) amortized time.

The key operation in a splay tree is splaying, which moves a node to the root
through a series of tree rotations. After every access (search, insert, delete),
the accessed node is splayed to the root.

Key Features:
    - Self-balancing through splaying operations
    - Simple implementation (no balance factors or colors)
    - Good cache performance due to locality of reference
    - Amortized O(log n) time complexity for operations
    - No additional storage overhead per node

Splaying Operations:
    - Zig: Single rotation (when node's parent is root)
    - Zig-Zig: Double rotation in same direction
    - Zig-Zag: Double rotation in different directions (like AVL rotation)

For more information:
https://en.wikipedia.org/wiki/Splay_tree

Author: [Priyams contribution to TheAlgorithms/Python]
"""

from __future__ import annotations

from typing import Any


class Node:
    """
    A node in the Splay Tree.

    Attributes:
        key: The value stored in the node
        left: Reference to the left child
        right: Reference to the right child
        parent: Reference to the parent node
    """

    def __init__(self, key: Any) -> None:
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None

    def __repr__(self) -> str:
        """
        Return string representation of the node.

        Examples:
        >>> node = Node(10)
        >>> repr(node)
        'Node(10)'
        >>> str(node)
        'Node(10)'
        >>> node = Node("hello")
        >>> repr(node)
        'Node(hello)'
        >>> node = Node(-5)
        >>> repr(node)
        'Node(-5)'
        >>> node = Node(3.14)
        >>> repr(node)
        'Node(3.14)'
        >>> node = Node(None)
        >>> repr(node)
        'Node(None)'
        """
        return f"Node({self.key})"


class SplayTree:
    """
    Splay Tree implementation with standard BST operations.

    The tree automatically splays (moves to root) any accessed node,
    providing excellent amortized performance for sequences of operations.

    Examples:
    >>> tree = SplayTree()
    >>> tree.insert(10)
    >>> tree.insert(5)
    >>> tree.insert(15)
    >>> tree.insert(3)
    >>> tree.insert(7)
    >>> tree.search(7)
    True
    >>> tree.search(100)
    False
    >>> tree.inorder()
    [3, 5, 7, 10, 15]
    >>> _ = tree.delete(5)
    >>> tree.inorder()
    [3, 7, 10, 15]
    >>> tree.get_root_key()  # Root changes after delete
    3
    """

    def __init__(self) -> None:
        self.root: Node | None = None

    def _right_rotate(self, node: Node) -> None:
        """
        Perform a right rotation on the given node.

        Before rotation:
              node
              /  \\
            left  C
            /  \\
           A    B

        After rotation:
            left
            /  \\
           A   node
               /  \\
              B    C

        Args:
            node: The node to rotate

        Time Complexity: O(1)
        """
        left_child = node.left
        if left_child is None:
            return

        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def _left_rotate(self, node: Node) -> None:
        """
        Perform a left rotation on the given node.

        Before rotation:
            node
            /  \\
           A   right
               /  \\
              B    C

        After rotation:
              right
              /  \\
            node  C
            /  \\
           A    B

        Args:
            node: The node to rotate

        Time Complexity: O(1)
        """
        right_child = node.right
        if right_child is None:
            return

        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _splay(self, node: Node) -> None:
        """
        Splay the given node to the root of the tree.

        This is the core operation of a splay tree. It moves the node
        to the root through a series of rotations:
        - Zig: node's parent is root (single rotation)
        - Zig-Zig: node and parent are both left or both right children
        - Zig-Zag: node is left child and parent is right, or vice versa

        Args:
            node: The node to splay to root

        Time Complexity: O(log n) amortized
        """
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                # Zig case: parent is root, single rotation
                if node == parent.left:
                    self._right_rotate(parent)
                else:
                    self._left_rotate(parent)
            elif node == parent.left and parent == grandparent.left:
                # Zig-Zig case: both are left children
                self._right_rotate(grandparent)
                self._right_rotate(parent)
            elif node == parent.right and parent == grandparent.right:
                # Zig-Zig case: both are right children
                self._left_rotate(grandparent)
                self._left_rotate(parent)
            elif node == parent.right and parent == grandparent.left:
                # Zig-Zag case: node is right child, parent is left child
                self._left_rotate(parent)
                self._right_rotate(grandparent)
            else:
                # Zig-Zag case: node is left child, parent is right child
                self._right_rotate(parent)
                self._left_rotate(grandparent)

    def insert(self, key: Any) -> None:
        """
        Insert a key into the splay tree.

        After insertion, the new node is splayed to the root.
        If the key already exists, it is splayed to root but not duplicated.

        Args:
            key: The key to insert

        Time Complexity: O(log n) amortized

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.get_root_key()
        15
        """
        node = Node(key)

        if self.root is None:
            self.root = node
            return

        current: Node | None = self.root
        parent: Node | None = None

        # Standard BST insertion
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Key already exists, splay it to root
                self._splay(current)
                return

        node.parent = parent
        if parent is not None:
            if key < parent.key:
                parent.left = node
            else:
                parent.right = node

        # Splay the newly inserted node to root
        self._splay(node)

    def search(self, key: Any) -> bool:
        """
        Search for a key in the splay tree.

        If found, the node containing the key is splayed to the root.
        If not found, the last accessed node is splayed to the root.

        Args:
            key: The key to search for

        Returns:
            bool: True if key exists, False otherwise

        Time Complexity: O(log n) amortized

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.search(5)
        True
        >>> tree.get_root_key()
        5
        >>> tree.search(100)
        False
        """
        if self.root is None:
            return False

        current: Node | None = self.root
        parent: Node | None = None

        while current is not None:
            if key == current.key:
                self._splay(current)
                return True
            parent = current
            current = current.left if key < current.key else current.right

        # Key not found, splay the last accessed node
        if parent is not None:
            self._splay(parent)
        return False

    def delete(self, key: Any) -> bool:
        """
        Delete a key from the splay tree.

        The node to be deleted is first splayed to the root, then removed.
        The tree is reconstructed by joining the left and right subtrees.

        Args:
            key: The key to delete

        Returns:
            bool: True if key was deleted, False if key not found

        Time Complexity: O(log n) amortized

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.delete(5)
        True
        >>> tree.search(5)
        False
        >>> tree.delete(100)
        False
        """
        if not self.search(key):  # This also splays the node if found
            return False

        # After search, the node with key is at root
        if self.root is None:
            return False

        left_subtree = self.root.left
        right_subtree = self.root.right

        if left_subtree is None:
            self.root = right_subtree
            if self.root is not None:
                self.root.parent = None
        else:
            # Find maximum in left subtree and splay it
            left_subtree.parent = None
            self.root = left_subtree

            # Find the maximum node in left subtree
            max_node = left_subtree
            while max_node.right is not None:
                max_node = max_node.right

            # Splay the maximum node to root of left subtree
            self._splay(max_node)

            # Attach right subtree
            self.root.right = right_subtree
            if right_subtree is not None:
                right_subtree.parent = self.root

        return True

    def find_min(self) -> Any | None:
        """
        Find the minimum key in the tree.

        The minimum node is splayed to the root after being found.

        Returns:
            The minimum key, or None if tree is empty

        Time Complexity: O(log n) amortized

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.find_min()
        5
        >>> tree.get_root_key()
        5
        """
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        self._splay(current)
        return current.key

    def find_max(self) -> Any | None:
        """
        Find the maximum key in the tree.

        The maximum node is splayed to the root after being found.

        Returns:
            The maximum key, or None if tree is empty

        Time Complexity: O(log n) amortized

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.find_max()
        15
        >>> tree.get_root_key()
        15
        """
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right

        self._splay(current)
        return current.key

    def inorder(self) -> list[Any]:
        """
        Return an inorder traversal of the tree.

        Returns:
            List of keys in sorted order

        Time Complexity: O(n)

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.insert(3)
        >>> tree.insert(7)
        >>> tree.inorder()
        [3, 5, 7, 10, 15]
        """
        result: list[Any] = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: Node | None, result: list[Any]) -> None:
        """Helper method for inorder traversal."""
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)

    def preorder(self) -> list[Any]:
        """
        Return a preorder traversal of the tree.

        Returns:
            List of keys in preorder

        Time Complexity: O(n)

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> sorted(tree.preorder())  # Tree structure varies after inserts
        [5, 10, 15]
        """
        result: list[Any] = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node: Node | None, result: list[Any]) -> None:
        """Helper method for preorder traversal."""
        if node is not None:
            result.append(node.key)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def get_root_key(self) -> Any | None:
        """
        Get the key of the root node.

        Returns:
            The root's key, or None if tree is empty

        Examples:
        >>> tree = SplayTree()
        >>> tree.get_root_key() is None
        True
        >>> tree.insert(10)
        >>> tree.get_root_key()
        10
        """
        return self.root.key if self.root else None

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
        Get the number of nodes in the tree.

        Returns:
            The number of nodes

        Time Complexity: O(n)

        Examples:
        >>> tree = SplayTree()
        >>> tree.size()
        0
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.size()
        3
        """
        return self._size_helper(self.root)

    def _size_helper(self, node: Node | None) -> int:
        """Helper method to calculate tree size."""
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)

    def height(self) -> int:
        """
        Get the height of the tree.

        Returns:
            The height of the tree (empty tree has height -1)

        Time Complexity: O(n)

        Examples:
        >>> tree = SplayTree()
        >>> tree.height()
        -1
        >>> tree.insert(10)
        >>> tree.height()
        0
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.height() <= 2
        True
        """
        return self._height_helper(self.root)

    def _height_helper(self, node: Node | None) -> int:
        """Helper method to calculate tree height."""
        if node is None:
            return -1
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))

    def display(self) -> None:
        """
        Display the tree structure in a readable format.

        Examples:
        >>> tree = SplayTree()
        >>> tree.insert(10)
        >>> tree.insert(5)
        >>> tree.insert(15)
        >>> tree.display()  # doctest: +SKIP
        15
        ├── 5
        │   ├── None
        │   └── 10
        │       ├── None
        │       └── None
        └── None
        """
        if self.root is None:
            print("Empty tree")
        else:
            self._display_helper(self.root, "", True)

    def _display_helper(self, node: Node | None, prefix: str, is_tail: bool) -> None:
        """Helper method to display tree structure."""
        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.key))
            children = [node.left, node.right]
            for i, child in enumerate(children):
                if child is not None or i == 0:  # Show at least left child position
                    extension = "    " if is_tail else "│   "
                    if child is not None:
                        self._display_helper(child, prefix + extension, i == 1)
                    else:
                        print(
                            prefix + extension + ("└── " if i == 1 else "├── ") + "None"
                        )


def performance_comparison() -> None:
    """
    Demonstrate the performance characteristics of Splay Trees.

    This shows how splay trees excel at repeated access to the same elements.

    Examples:
    >>> tree = SplayTree()
    >>> for i in range(1, 11):
    ...     tree.insert(i)
    >>> tree.size()
    10
    >>> tree.get_root_key()  # Last inserted element
    10
    >>> # Demonstrate locality of reference - repeated access
    >>> for _ in range(5):
    ...     _ = tree.search(5)
    >>> tree.get_root_key()  # Element 5 is now at root
    5
    >>> # Verify tree still maintains BST property
    >>> tree.inorder()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> # Test that min/max operations work and splay to root
    >>> min_val = tree.find_min()
    >>> min_val
    1
    >>> tree.get_root_key()  # Min is now at root
    1
    >>> max_val = tree.find_max()
    >>> max_val
    10
    >>> tree.get_root_key()  # Max is now at root
    10
    >>> # Verify height is reasonable (not degenerate)
    >>> tree.height() < 10
    True
    """
    import random
    import time

    print("=== Splay Tree Performance Demonstration ===\n")

    tree = SplayTree()

    # Insert elements
    print("Inserting elements 1-100...")
    for i in range(1, 101):
        tree.insert(i)

    print(f"Tree size: {tree.size()}")
    print(f"Tree height: {tree.height()}")
    print(f"Root after insertions: {tree.get_root_key()}\n")

    # Demonstrate locality of reference
    print("Accessing element 50 repeatedly (demonstrating cache-friendly behavior)...")
    start = time.time()
    for _ in range(1000):
        tree.search(50)
    end = time.time()
    print(f"Time for 1000 accesses to same element: {(end - start) * 1000:.4f} ms")
    print(f"Root after repeated access to 50: {tree.get_root_key()}\n")

    # Random access pattern
    print("Random access pattern...")
    random.seed(42)
    keys = [random.randint(1, 100) for _ in range(100)]
    start = time.time()
    for key in keys:
        tree.search(key)
    end = time.time()
    print(f"Time for 100 random accesses: {(end - start) * 1000:.4f} ms\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Run performance demonstration
    print("\n" + "=" * 50 + "\n")
    performance_comparison()

    # Interactive demonstration
    print("\n" + "=" * 50)
    print("=== Interactive Demonstration ===\n")

    tree = SplayTree()
    elements = [50, 25, 75, 10, 30, 60, 90, 5, 15, 27, 55, 65, 85, 95]

    print(f"Inserting elements: {elements}")
    for elem in elements:
        tree.insert(elem)

    print(f"\nInorder traversal: {tree.inorder()}")
    print(f"Tree size: {tree.size()}")
    print(f"Tree height: {tree.height()}")
    print(f"Root: {tree.get_root_key()}")

    print("\nSearching for 27 (will become new root)...")
    tree.search(27)
    print(f"Root after searching 27: {tree.get_root_key()}")

    print("\nFinding minimum...")
    min_key = tree.find_min()
    print(f"Minimum: {min_key}")
    print(f"Root after finding min: {tree.get_root_key()}")

    print("\nFinding maximum...")
    max_key = tree.find_max()
    print(f"Maximum: {max_key}")
    print(f"Root after finding max: {tree.get_root_key()}")

    print("\nDeleting 75...")
    tree.delete(75)
    print(f"Inorder after deletion: {tree.inorder()}")
    print(f"Root after deletion: {tree.get_root_key()}")

    print("\nTree structure:")
    tree.display()
