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
    

    @property 
    def mirror_binary_tree(self, root):
        pass 