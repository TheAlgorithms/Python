"""
all_traversals_one_pass.py

This module demonstrates how to perform Preorder, Inorder, and Postorder traversals
of a binary tree in a single traversal using an iterative approach with a stack.
"""

from typing import Optional, List, Tuple


class Node:
    """
    A class to represent a node in a binary tree.

    Attributes
    ----------
    data : int
        The value stored in the node.
    left : Node, optional
        The left child of the node.
    right : Node, optional
        The right child of the node.

    Reference: https://en.wikipedia.org/wiki/Binary_tree
    """

    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def all_traversals(root: Optional[Node]) -> Tuple[List[int], List[int], List[int]]:
    """
    Perform Preorder, Inorder, and Postorder traversals in a single pass.

    Parameters
    ----------
    root : Node
        The root of the binary tree.

    Returns
    -------
    Tuple[List[int], List[int], List[int]]
        A tuple containing three lists:
            - preorder  : List of nodes in Preorder (Root -> Left -> Right)
            - inorder   : List of nodes in Inorder  (Left -> Root -> Right)
            - postorder : List of nodes in Postorder(Left -> Right -> Root)

    Explanation
    -----------
    Each node is paired with a state value:
        state = 1  → Preorder processing (Root node is first time seen)
        state = 2  → Inorder processing (Left subtree done, process root)
        state = 3  → Postorder processing (Both subtrees done)

    Algorithm Steps:
    ---------------
    1. Initialize a stack with (root, 1).
    2. Pop the top element:
        - If state == 1:
            → Add node to Preorder
            → Push (node, 2)
            → If left child exists, push (left, 1)
        - If state == 2:
            → Add node to Inorder
            → Push (node, 3)
            → If right child exists, push (right, 1)
        - If state == 3:
            → Add node to Postorder
    3. Continue until stack is empty.

    Reference: Tree Traversals- https://en.wikipedia.org/wiki/Tree_traversal
               Stack Data Structure- https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

    """

    if root is None:
        return [], [], []

    stack: List[Tuple[Node, int]] = [(root, 1)]  # (node, state)
    preorder, inorder, postorder = [], [], []

    while stack:
        node, state = stack.pop()

        if state == 1:
            # Preorder position
            preorder.append(node.data)
            # Increment state to process inorder next time
            stack.append((node, 2))
            # Left child goes before inorder
            if node.left:
                stack.append((node.left, 1))

        elif state == 2:
            # Inorder position
            inorder.append(node.data)
            # Increment state to process postorder next time
            stack.append((node, 3))
            # Right child goes before postorder
            if node.right:
                stack.append((node.right, 1))

        else:
            # Postorder position
            postorder.append(node.data)

    return preorder, inorder, postorder


def build_sample_tree() -> Node:
    """
    Build and return a sample binary tree for demonstration.

                1
               / \\
              2   3
             / \\   \\
            4   5   6

    Returns
    -------
    Node
        The root node of the binary tree.

    Reference: https://en.wikipedia.org/wiki/Binary_tree
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root


if __name__ == "__main__":
    # Example
    root = build_sample_tree()
    preorder, inorder, postorder = all_traversals(root)

    print("Preorder  :", preorder)
    print("Inorder   :", inorder)
    print("Postorder :", postorder)
