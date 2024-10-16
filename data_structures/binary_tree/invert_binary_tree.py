"""
Given the root of a binary tree, invert the tree and return its root.

Leetcode: https://leetcode.com/problems/invert-binary-tree/description/

If n is the number of nodes in the tree, then:
Time complexity: O(n) as every subtree needs to be mirrored, we visit each node once.

Space complexity: O(h) where h is the height of the tree. This recursive algorithm 
uses the space of the stack which can grow to the height of the binary tree.
The space complexity will be O(n log n) for a binary tree and O(n) for a skewed tree.
"""

from __future__ import annotations 
from dataclasses import dataclass 

@dataclass
class TreeNode:
    """
    A TreeNode has a data variable and pointers to TreeNode objects for its left and right children.
    """
    
    def __init__(self, data: int) -> None:
        self.data = data 
        self.left: TreeNode | None = None 
        self.right: TreeNode | None = None 
    

class MirrorBinaryTree:
    def mirror_binary_tree(self, root : TreeNode):
        """
        Invert a binary tree and return the new root.

        Returns the root of the mirrored binary tree.

        >>> tree = TreeNode(0)
        >>> tree.left = TreeNode(10)
        >>> tree.right = TreeNode(20)
        >>> result_tree = MirrorBinaryTree().mirror_binary_tree(tree)
        >>> print_preorder(result_tree)
        0
        20
        10
        >>> tree2 = TreeNode(9)
        >>> result_tree2 = MirrorBinaryTree().mirror_binary_tree(tree2)
        >>> print_preorder(result_tree2)
        9
        """ 
        
        if not root:
            return None 

        if root.left:
            self.mirror_binary_tree(root.left)
        
        if root.right:
            self.mirror_binary_tree(root.right)
        
        root.left, root.right = root.right, root.left 

        return root

def print_preorder(root: TreeNode | None) -> None:
    """
    Print pre-order traversal of the tree .

    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> print_preorder(root)
    1
    2
    3
    >>> print_preorder(root.right)
    3
    """
    if not root:
        return None 
    if root:
        print(root.data)
        print_preorder(root.left)
        print_preorder(root.right)
        

if __name__ == "__main__":
    import doctest 
    doctest.testmod()
    
