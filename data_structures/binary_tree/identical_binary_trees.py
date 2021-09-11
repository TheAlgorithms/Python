#!/usr/local/bin/python3
from __future__ import annotations

"""
Problem Description: Given two binary trees, check if the two trees are identical or not.
Two trees are considered to be identical if the both have same identical and value of corresponding nodes are equal
"""

"""

Example 1: 
Tree 1 = 1, 2, 3
Tree 2 = 1, 2, 3
Output = True

Example 2:
Tree 1 = 1,2,3,4,5 
Tree 2 = 1,2,3,null,null,4,null,5
Output = False

"""


class TreeNode:
    """
    A binary tree node has a value variable and pointers to its left and right TreeNodes
    """

    def __init__(self, val=0) -> None:
        self.value = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def identical_binary_trees(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    """
    identical_binary_tree function takes root of the two trees and return True or False depending on if the trees are
    identical or not.
    """

    # if both the roots does not exist then in that particular condition trees are identical considering both of
    # them are None
    if root1 is None and root2 is None:
        return True

    # if either one of the root does not exist then trees can not be identical.
    if root1 is None or root2 is None:
        return False

    # Recursively find out if the remaining tree is identical and also add the condition if current TreeNode value
    # are equal.

    return identical_binary_trees(root1.left, root2.left) and identical_binary_trees(root1.right, root2.right) and \
        (root1.value == root2.value)


def print_preorder(root: TreeNode | None) -> None:
    """
    print_preorder takes root of a tree as a parameter and prints the preorder traversal of the binary tree.
    """

    if root:
        print(root.value, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)


if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(3)
    tree3.left.left = TreeNode(4)
    tree3.left.right = TreeNode(5)

    tree4 = TreeNode(1)
    tree4.left = TreeNode(2)
    tree4.right = TreeNode(3)
    tree4.right.left = TreeNode(4)
    tree4.right.left.left = TreeNode(5)

    print("Example 1: ")
    print("Tree 1  -->  ", end="")
    print_preorder(tree1)
    print()
    print("Tree 2  -->  ", end="")
    print_preorder(tree2)
    print()
    print(f'Trees are identical: {identical_binary_trees(tree1, tree2)}')

    print("Example 2: ")
    print("Tree 1  -->  ", end="")
    print_preorder(tree3)
    print()
    print("Tree 2  -->  ", end="")
    print_preorder(tree4)
    print()
    print(f'Trees are identical: {identical_binary_trees(tree3, tree4)}')
