"""
This is a python3 implementation of binary search tree using iteration
To run tests:
python -m unittest binary_search_tree_recursive.py
To run an example:
python binary_search_tree_iterative.py
"""
from __future__ import annotations
from dataclasses import dataclass


# Node of Tree
@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None


def make_tree() -> Node:
    return Node(1, Node(2, Node(4), Node(5)), Node(3))


# Inorder tree traversal
def print_inorder(root: Node):
    """
    In-order traversal visits left subtree, root node, right subtree.
    >>> print_inorder(make_tree())
    4->2->5->1->3->
    """
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            key = stack.pop()
            print(key.data, end="->")
            current = key.right
        else:
            break


# Preorder tree traversal
def print_preorder(root: Node):
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> print_preorder(make_tree())
    1->2->4->5->3->
    """
    current = root
    stack = [current]
    while stack:
        key = stack.pop()
        print(key.data, end="->")
        if key.right:
            stack.append(key.right)
        if key.left:
            stack.append(key.left)
    return


# Postorder tree traversal
def print_postorder(root: Node):
    """
    Post-order traversal visits left subtree, right subtree, root node.
    >>> print_postorder(make_tree())
    4->5->2->3->1->
    """
    current = root
    stack1 = []
    stack2 = []
    stack1.append(current)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        print(node.data, end="->")
    return


def main():  # Main function for testing.
    """
    Create binary tree.
    """
    root = make_tree()
    """
    All Traversals of the binary are as follows:
    """
    print("In-order Traversal is: ")
    print_inorder(root)
    print("\n")
    print(" Pre-order Traversal is: ")
    print_preorder(root)
    print("\n")
    print("Post-order Traversal is: ")
    print_postorder(root)
    print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
