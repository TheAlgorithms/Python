from __future__ import annotations

from collections import deque
from collections.abc import Generator
from dataclasses import dataclass


# https://en.wikipedia.org/wiki/Tree_traversal
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


def preorder(root: Node | None) -> Generator[int, None, None]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> list(preorder(make_tree()))
    [1, 2, 4, 5, 3]
    """
    if not root:
        return
    yield root.data
    yield from preorder(root.left)
    yield from preorder(root.right)


def postorder(root: Node | None) -> Generator[int, None, None]:
    """
    Post-order traversal visits left subtree, right subtree, root node.
    >>> list(postorder(make_tree()))
    [4, 5, 2, 3, 1]
    """
    if not root:
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root.data


def inorder(root: Node | None) -> Generator[int, None, None]:
    """
    In-order traversal visits left subtree, root node, right subtree.
    >>> list(inorder(make_tree()))
    [4, 2, 5, 1, 3]
    """
    if not root:
        return
    yield from inorder(root.left)
    yield root.data
    yield from inorder(root.right)


def reverse_inorder(root: Node | None) -> Generator[int, None, None]:
    """
    Reverse in-order traversal visits right subtree, root node, left subtree.
    >>> list(reverse_inorder(make_tree()))
    [3, 1, 5, 2, 4]
    """
    if not root:
        return
    yield from reverse_inorder(root.right)
    yield root.data
    yield from reverse_inorder(root.left)


def height(root: Node | None) -> int:
    """
    Recursive function for calculating the height of the binary tree.
    >>> height(None)
    0
    >>> height(make_tree())
    3
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order(root: Node | None) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
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
) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a particular level:
    Left to right direction of the binary tree.
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


def get_nodes_from_right_to_left(
    root: Node | None, level: int
) -> Generator[int, None, None]:
    """
    Returns a list of nodes value from a particular level:
    Right to left direction of the binary tree.
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


def zigzag(root: Node | None) -> Generator[int, None, None]:
    """
    ZigZag traverse:
    Returns a list of nodes value from left to right and right to left, alternatively.
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
    print(f"{list(level_order(root))} \n")

    print("Level-wise order Traversal: ")

    for level in range(1, height(root) + 1):
        print(f"Level {level}:", list(get_nodes_from_left_to_right(root, level=level)))

    print("\nZigZag order Traversal: ")
    print(f"{list(zigzag(root))}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
