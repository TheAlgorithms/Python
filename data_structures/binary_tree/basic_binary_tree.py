from __future__ import annotations  # Allows using the class itself as a type hint within the class

from collections.abc import Iterator  # For type hinting iteration
from dataclasses import dataclass     # For concise class definitions


# -----------------------------
# Node class: represents one node in the binary tree
# -----------------------------
@dataclass
class Node:
    data: int  # Value stored in the node
    left: Node | None = None   # Left child node
    right: Node | None = None  # Right child node

    # -----------------------------
    # In-order traversal generator
    # Allows iterating over Node like: `for x in node: ...`
    # -----------------------------
    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left   # Yield all values from the left subtree
        yield self.data            # Yield the current node's data
        if self.right:
            yield from self.right  # Yield all values from the right subtree

    # -----------------------------
    # Returns number of nodes in the subtree rooted at this node
    # -----------------------------
    def __len__(self) -> int:
        return sum(1 for _ in self)  # Count all nodes using iteration

    # -----------------------------
    # Check if the subtree rooted at this node is a full binary tree
    # A full binary tree: every node has 0 or 2 children
    # -----------------------------
    def is_full(self) -> bool:
        if not self or (not self.left and not self.right):
            return True  # Leaf node is full
        if self.left and self.right:
            # Node has two children → recursively check both subtrees
            return self.left.is_full() and self.right.is_full()
        return False  # Node has only one child → not full


# -----------------------------
# BinaryTree class: represents the whole binary tree
# -----------------------------
@dataclass
class BinaryTree:
    root: Node  # Root node of the tree

    # -----------------------------
    # Iterate over tree using in-order traversal
    # -----------------------------
    def __iter__(self) -> Iterator[int]:
        return iter(self.root)

    # -----------------------------
    # Return total number of nodes in the tree
    # -----------------------------
    def __len__(self) -> int:
        return len(self.root)

    # -----------------------------
    # Factory method: small tree (3 nodes)
    # -----------------------------
    @classmethod
    def small_tree(cls) -> BinaryTree:
        """
        Return a small binary tree with 3 nodes.
        >>> binary_tree = BinaryTree.small_tree()
        >>> len(binary_tree)
        3
        >>> list(binary_tree)
        [1, 2, 3]
        """
        binary_tree = BinaryTree(Node(2))  # Root node = 2
        binary_tree.root.left = Node(1)    # Left child
        binary_tree.root.right = Node(3)   # Right child
        return binary_tree

    # -----------------------------
    # Factory method: medium tree (7 nodes)
    # -----------------------------
    @classmethod
    def medium_tree(cls) -> BinaryTree:
        """
        Return a medium binary tree with 7 nodes.
        >>> binary_tree = BinaryTree.medium_tree()
        >>> len(binary_tree)
        7
        >>> list(binary_tree)
        [1, 2, 3, 4, 5, 6, 7]
        """
        binary_tree = BinaryTree(Node(4))  # Root node = 4
        binary_tree.root.left = two = Node(2)
        two.left = Node(1)
        two.right = Node(3)
        binary_tree.root.right = five = Node(5)
        five.right = six = Node(6)
        six.right = Node(7)
        return binary_tree

    # -----------------------------
    # Public method: get depth of tree
    # -----------------------------
    def depth(self) -> int:
        """
        Returns the depth of the tree
        >>> BinaryTree(Node(1)).depth()
        1
        >>> BinaryTree.small_tree().depth()
        2
        >>> BinaryTree.medium_tree().depth()
        4
        """
        return self._depth(self.root)

    # -----------------------------
    # Helper recursive method to compute depth
    # Depth = 1 + max(depth of left, depth of right)
    # -----------------------------
    def _depth(self, node: Node | None) -> int:
        if not node:
            return 0  # Empty node contributes 0 to depth
        return 1 + max(self._depth(node.left), self._depth(node.right))

    # -----------------------------
    # Check if the tree is full
    # -----------------------------
    def is_full(self) -> bool:
        """
        Returns True if the tree is full
        >>> BinaryTree(Node(1)).is_full()
        True
        >>> BinaryTree.small_tree().is_full()
        True
        >>> BinaryTree.medium_tree().is_full()
        False
        """
        return self.root.is_full()


# -----------------------------
# Run doctests if executed as main
# -----------------------------
if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Automatically tests all docstring examples
