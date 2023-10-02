from __future__ import annotations  # Use annotations for forward references

from collections import deque
from collections.abc import Generator
from dataclasses import dataclass

# Define a Node class to represent binary tree nodes
@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

# Function to create a sample binary tree
def make_tree() -> Node | None:
    """
    Create a sample binary tree:
        1
       / \
      2   3
     / \
    4   5
    """
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    return tree

# Pre-order traversal of a binary tree
def preorder(root: Node | None) -> Generator[int, None, None]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    """
    if not root:
        return
    yield root.data
    yield from preorder(root.left)
    yield from preorder(root.right)

# Post-order traversal of a binary tree
def postorder(root: Node | None) -> Generator[int, None, None]:
    """
    Post-order traversal visits left subtree, right subtree, root node.
    """
    if not root:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root.data

# In-order traversal of a binary tree
def inorder(root: Node | None) -> Generator[int, None, None]:
    """
    In-order traversal visits left subtree, root node, right subtree.
    """
    if not root:
        return
    yield from inorder(root.left)
    yield root.data
    yield from inorder(root.right)

# Reverse in-order traversal of a binary tree
def reverse_inorder(root: Node | None) -> Generator[int, None, None]:
    """
    Reverse in-order traversal visits right subtree, root node, left subtree.
    """
    if not root:
        return
    yield from reverse_inorder(root.right)
    yield root.data
    yield from reverse_inorder(root.left)

# Calculate the height of a binary tree
def height(root: Node | None) -> int:
    """
    Recursive function for calculating the height of the binary tree.
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0

# Level-order traversal of a binary tree
def level_order(root: Node | None) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a whole binary tree in Level Order Traverse.
    """
    if root is None:
        return

    process_queue = deque([root])

    while process_queue:
        node = process_queue.popleft()
        yield node.data

        if node.left:
            process_queue.append(node.left)
        if node.right:
            process_queue.append(node.right)

# Get nodes from left to right at a specific level of the binary tree
def get_nodes_from_left_to_right(
    root: Node | None, level: int
) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a particular level: Left to right direction of the binary tree.
    """

    def populate_output(root: Node | None, level: int) -> Generator[int, None, None]:
        if not root:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.left, level - 1)
            yield from populate_output(root.right, level - 1)

    yield from populate_output(root, level)

# Get nodes from right to left at a specific level of the binary tree
def get_nodes_from_right_to_left(
    root: Node | None, level: int
) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a particular level: Right to left direction of the binary tree.
    """

    def populate_output(root: Node | None, level: int) -> Generator[int, None, None]:
        if root is None:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.right, level - 1)
            yield from populate_output(root.left, level - 1)

    yield from populate_output(root, level)

# Zigzag traversal of a binary tree
def zigzag(root: Node | None) -> Generator[int, None, None]:
    """
    ZigZag traverse: Returns a list
