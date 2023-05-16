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


def preorder(root: Node | None) -> list[int]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> preorder(make_tree())
    [1, 2, 4, 5, 3]
    """
    return [root.data, *preorder(root.left), *preorder(root.right)] if root else []


def postorder(root: Node | None) -> list[int]:
    """
    Post-order traversal visits left subtree, right subtree, root node.
    >>> postorder(make_tree())
    [4, 5, 2, 3, 1]
    """
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []


def inorder(root: Node | None) -> list[int]:
    """
    In-order traversal visits left subtree, root node, right subtree.
    >>> inorder(make_tree())
    [4, 2, 5, 1, 3]
    """
    return [*inorder(root.left), root.data, *inorder(root.right)] if root else []


def reverse_inorder(root: Node | None) -> list[int]:
    """
    Reverse in-order traversal visits right subtree, root node, left subtree.
    >>> reverse_inorder(make_tree())
    [3, 1, 5, 2, 4]
    """
    return (
        [*reverse_inorder(root.right), root.data, *reverse_inorder(root.left)]
        if root
        else []
    )


def height(root: Node | None) -> int:
    """
    Recursive function for calculating the height of the binary tree.
    >>> height(None)
    0
    >>> height(make_tree())
    3
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order(root: Node | None) -> Sequence[Node | None]:
    """
    Returns a list of nodes value from a whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    """
    output: list[Any] = []

    if root is None:
        return output

    process_queue = deque([root])

    while process_queue:
        node = process_queue.popleft()
        output.append(node.data)

        if node.left:
            process_queue.append(node.left)
        if node.right:
            process_queue.append(node.right)
    return output


def get_nodes_from_left_to_right(
    root: Node | None, level: int
) -> Sequence[Node | None]:
    """
    Returns a list of nodes value from a particular level:
    Left to right direction of the binary tree.
    """
    output: list[Any] = []

    def populate_output(root: Node | None, level: int) -> None:
        if not root:
            return
        if level == 1:
            output.append(root.data)
        elif level > 1:
            populate_output(root.left, level - 1)
            populate_output(root.right, level - 1)

    populate_output(root, level)
    return output


def get_nodes_from_right_to_left(
    root: Node | None, level: int
) -> Sequence[Node | None]:
    """
    Returns a list of nodes value from a particular level:
    Right to left direction of the binary tree.
    """
    output: list[Any] = []

    def populate_output(root: Node | None, level: int) -> None:
        if root is None:
            return
        if level == 1:
            output.append(root.data)
        elif level > 1:
            populate_output(root.right, level - 1)
            populate_output(root.left, level - 1)

    populate_output(root, level)
    return output


def zigzag(root: Node | None) -> Sequence[Node | None] | list[Any]:
    """
    ZigZag traverse:
    Returns a list of nodes value from left to right and right to left, alternatively.
    """
    if root is None:
        return []

    output: list[Sequence[Node | None]] = []

    flag = 0
    height_tree = height(root)

    for h in range(1, height_tree + 1):
        if not flag:
            output.append(get_nodes_from_left_to_right(root, h))
            flag = 1
        else:
            output.append(get_nodes_from_right_to_left(root, h))
            flag = 0

    return output


def main() -> None:  # Main function for testing.
    # Create binary tree.
    root = make_tree()

    # All Traversals of the binary are as follows:
    print(f"In-order Traversal: {inorder(root)}")
    print(f"Reverse In-order Traversal: {reverse_inorder(root)}")
    print(f"Pre-order Traversal: {preorder(root)}")
    print(f"Post-order Traversal: {postorder(root)}", "\n")

    print(f"Height of Tree: {height(root)}", "\n")

    print("Complete Level Order Traversal: ")
    print(level_order(root), "\n")

    print("Level-wise order Traversal: ")

    for level in range(1, height(root) + 1):
        print(f"Level {level}:", get_nodes_from_left_to_right(root, level=level))

    print("\nZigZag order Traversal: ")
    print(zigzag(root))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
