from __future__ import annotations


class Node:
    """
    prints the inorder Traversal of transformed tree
    >>> sum = 0
    >>> root = Node(11)
    >>> root.left = Node(2)
    >>> root.right = Node(29)
    >>> root.left.left = Node(1)
    >>> root.left.right = Node(7)
    >>> root.right.left = Node(15)
    >>> root.right.right = Node(40)
    >>> root.right.right.left = Node(35)
    >>> printInorder(root)
    1 2 7 11 15 29 35 40

    >>> transformTree(root)

    >>> printInorder(root)
    139 137 130 119 104 75 40 0
    """

    def __init__(self, x) -> None:
        self.data = x
        self.left = None
        self.right = None


# Recursive function to transform a BST to sum tree.
# This function traverses the tree in reverse inorder so
# that we have visited all greater key nodes of the currently
# visited node
def transformTreeUtil(root) -> None:
    """
    Transform a binary tree into a sum tree.

    Example:
    >>> root = Node(11)
    >>> root.left = Node(2)
    >>> root.right = Node(29)
    >>> transformTree(root)
    >>> root.data
    60
    >>> root.left.data
    31
    >>> root.right.data
    29
    """

    # Base case
    if root == None:
        return

    # Recur for right subtree
    transformTreeUtil(root.right)

    # Update sum
    global sum
    sum = sum + root.data

    # Store old sum in the current node
    root.data = sum - root.data

    # Recur for left subtree
    transformTreeUtil(root.left)


# A wrapper over transformTreeUtil()
def transformTree(root) -> None:
    """
    Transform a binary tree into a sum tree.

    Example:
    >>> root = Node(11)
    >>> root.left = Node(2)
    >>> root.right = Node(29)
    >>> transformTree(root)
    >>> root.data
    60
    >>> root.left.data
    31
    >>> root.right.data
    29
    """

    # sum = 0 #Initialize sum
    transformTreeUtil(root)


# A utility function to prindorder traversal of a
# binary tree
def printInorder(root):
    """
    Perform an inorder traversal of a binary tree and print the nodes.

    Example:
    >>> root = Node(11)
    >>> root.left = Node(2)
    >>> root.right = Node(29)
    >>> printInorder(root)
    2 11 29
    """

    if root == None:
        return

    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


# Driver Program to test above functions
if __name__ == "__main__":
    sum = 0
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)

    print("Inorder Traversal of given tree")
    printInorder(root)

    transformTree(root)

    print("\nInorder Traversal of transformed tree")
    printInorder(root)
