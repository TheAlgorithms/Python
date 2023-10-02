"""
Given the root of a binary tree, invert the tree, and return its root.

Leetcode problem reference: https://leetcode.com/problems/invert-binary-tree/
"""

from __future__ import annotations


class Node:
    """
    A Node has value variable and pointers to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


def display(tree: Node | None) -> None:  
    """
    Prints the inorder traversal of a tree
    """
    if tree:
        display(tree.left)
        print(tree.value, end=" ")
        display(tree.right)

def invert_binary_tree(root: Node| None) -> None:
    """
    Inverts a binary tree and returns the root node of the binary tree
    """
    if root != None: #If root is not None
            temp : Node = root.left  #Save left Node in a temp variable
            # Swap the Nodes
            root.left = root.right 
            root.right = temp
            # Now, invoke the function recursively for both the children
            invert_binary_tree(root.left) 
            invert_binary_tree(root.right)
    # Return the Node
    return root

if __name__ == "__main__":
    # Create a binary tree with 7 Nodes
    t1 : Node = Node(1)
    t1.left = Node(2)
    t1.right = Node(3)
    t1.left.left = Node(4)
    t1.left.right = Node(5)
    t1.right.left = Node(6)
    t1.right.right = Node(7)

    """
     The tree is like
              1
        2         3
      4   5     6    7
    """

    print("Tree: ",end=" ")
    display(t1)  

    #Invert the binary tree (t1) and store the returned Node in t2
    t2 : Node = invert_binary_tree(t1)  
    """
     The inverted tree is like
             1
        3         2
      7    6    5   4     
    """

    print("\nInverted Tree: ", end=" ")
    display(t2)  
    print()