# https://en.wikipedia.org/wiki/Tree_traversal
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass
class Node:
    data: int
    left: NodeType = None
    right: NodeType = None


NodeType = Optional[Node]


def make_tree() -> Node:
    return Node(1, Node(2, Node(4), Node(5)), Node(3))


def preorder(root: NodeType) -> list[int]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> preorder(make_tree())
    [1, 2, 4, 5, 3]
    """
    return [root.data] + preorder(root.left) + preorder(root.right) if root else []


def postorder(root: NodeType) -> list[int]:
    """
    Post-order traversal visits left subtree, right subtree, root node.
    >>> postorder(make_tree())
    [4, 5, 2, 3, 1]
    """
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []


def inorder(root: NodeType) -> list[int]:
    """
    In-order traversal visits left subtree, root node, right subtree.
    >>> inorder(make_tree())
    [4, 2, 5, 1, 3]
    """
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []


def height(root: NodeType) -> int:
    """
    Recursive function for calculating the height of the binary tree.
    >>> height(None)
    0
    >>> height(make_tree())
    3
    """
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order_1(root: NodeType) -> Sequence[NodeType]:
    """
    Print whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    """
    if not root:
        return []

    temp = root
    process_queue = deque([temp])

    while process_queue:
        print(process_queue[0].data, end=" ")
        temp = process_queue.popleft()

        if temp.left:
            process_queue.append(temp.left)
        if temp.right:
            process_queue.append(temp.right)
    return process_queue


def print_left_to_right(root: NodeType, level: int) -> None:
    """
    Print elements on particular level from left to right direction of the binary tree.
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_left_to_right(root.left, level - 1)
        print_left_to_right(root.right, level - 1)


def print_right_to_left(root: NodeType, level: int) -> None:
    """
    Print elements on particular level from right to left direction of the binary tree.
    """
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_right_to_left(root.right, level - 1)
        print_right_to_left(root.left, level - 1)


def zigzag(root: NodeType) -> None:
    """
    ZigZag traverse: Print node left to right and right to left, alternatively.
    """
    flag = 0
    height_tree = height(root)
    for h in range(1, height_tree + 1):
        if flag == 0:
            print_left_to_right(root, h)
            flag = 1
        else:
            print_right_to_left(root, h)
            flag = 0


def main() -> None:  # Main function for testing.
    """
    Create binary tree.
    """
    root = make_tree()
    """
    All Traversals of the binary are as follows:
    """
    print(f"  In-order Traversal is {inorder(root)}")
    print(f" Pre-order Traversal is {preorder(root)}")
    print(f"Post-order Traversal is {postorder(root)}")
    print(f"Height of Tree is {height(root)}")
    print("Complete Level Order Traversal is : ")
    level_order_1(root)
    print("\nLevel-wise order Traversal is : ")
    for h in range(1, height(root) + 1):
        print_left_to_right(root, h)
    print("\nZigZag order Traversal is : ")
    zigzag(root)
    print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
