# https://en.wikipedia.org/wiki/Tree_traversal
from __future__ import annotations

from collections import deque
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None


def make_tree() -> Node | None:
    r"""
    The below tree
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


def preorder(root: Node | None) -> Sequence[int]:
    """
    Lazy preorder traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Yields:
        The values of nodes in the tree using lazy traversal.
    """
    if not root:
        return
    yield root.data
    yield from preorder(root.left)
    yield from preorder(root.right)


def postorder(root: Node | None) -> Sequence[int]:
    """
    Lazy post-order traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Yields:
        The values of nodes in the tree using lazy traversal.
    """
    if not root:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root.data


def inorder(root: Node | None) -> Sequence[int]:
    """
    Lazy in-order traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Yields:
        The values of nodes in the tree using lazy traversal.
    """
    if not root:
        return
    yield from inorder(root.left)
    yield root.data
    yield from inorder(root.right)


def reverse_inorder(root: Node | None) -> Sequence[int]:
    """
    Lazy reverse in-order traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Yields:
        The values of nodes in the tree using lazy traversal.
    """
    if not root:
        return
    yield from reverse_inorder(root.right)
    yield root.data
    yield from reverse_inorder(root.left)


def height(root: Node | None) -> int:
    """
    Recursive function for calculating the height of the binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The height of the binary tree.
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order(root: Node | None) -> Sequence[int]:
    """
    Lazy level order traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Yields:
        The values of nodes in the tree using lazy traversal.
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


def get_nodes_from_left_to_right(
    root: Node | None, level: int
) -> Sequence[int]:
    """
    Lazy traversal to get nodes from left to right at a particular level of a binary tree.

    Args:
        root: The root node of the binary tree.
        level: The level at which nodes are retrieved.

    Yields:
        The values of nodes at the specified level using lazy traversal.
    """
    if not root:
        return

    def populate_output(root: Node | None, level: int) -> None:
        if not root:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.left, level - 1)
            yield from populate_output(root.right, level - 1)

    yield from populate_output(root, level)


def get_nodes_from_right_to_left(
    root: Node | None, level: int
) -> Sequence[int]:
    """
    Lazy traversal to get nodes from right to left at a particular level of a binary tree.

    Args:
        root: The root node of the binary tree.
        level: The level at which nodes are retrieved.

    Yields:
        The values of nodes at the specified level using lazy traversal.
    """
    if not root:
        return

    def populate_output(root: Node | None, level: int) -> None:
        if not root:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.right, level - 1)
            yield from populate_output(root.left, level - 1)

    yield from populate_output(root, level)


def zigzag(root: Node | None) -> Sequence[Node | None] | list[Any]:
    """
    ZigZag traverse:
    Returns a list of nodes value from left to right and right to left, alternatively.

    Args:
        root: The root node of the binary tree.

    Yields:
        The values of nodes in a zigzag order using lazy traversal.
    """
    if root is None:
        return

    flag = 0
    height_tree = height(root)

    for h in range(1, height_tree + 1):
        if not flag:
            yield from get_nodes_from_left_to_right(root, h)
            flag = 1
        else:
            yield from get_nodes_from_right_to_left(root, h)
            flag = 0


def main() -> None:  # Main function for testing.
    # Create binary tree.
    root = make_tree()

    # All Traversals of the binary are as follows:
    print(f"In-order Traversal: {list(inorder(root))}")
    print(f"Reverse In-order Traversal: {list(reverse_inorder(root))}")
    print(f"Pre-order Traversal: {list(preorder(root))}")
    print(f"Post-order Traversal: {list(postorder(root))}", "\n")

    print(f"Height of Tree: {height(root)}", "\n")

    print("Complete Level Order Traversal: ")
    print(list(level_order(root)), "\n")

    print("Level-wise order Traversal: ")

    for level in range(1, height(root) + 1):
        print(f"Level {level}:", list(get_nodes_from_left_to_right(root, level=level)))

    print("\nZigZag order Traversal: ")
    print(list(zigzag(root)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
