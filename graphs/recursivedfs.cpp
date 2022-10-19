"""
https://simple.wikipedia.org/wiki/Depth-first_search
"""
      
from __future__ import annotations

import time
from math import sqrt

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode

class Solution:
    prev_node = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
          return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev_node
        root.left = None

        self.prev_node = root

    def findFullNode(self, root: Optional[TreeNode]) -> None:
      if root.left:
        self.findFullNode(root.left)
      print(root.val),
      if root.right:
        self.findFullNode(root.right)
if __name__ == "__main__":
    lst = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = creatBTree(lst, 0)
    s = Solution()
    print("List before reversing:")
    s.findFullNode(root)
    print("\n")

    dfs_start_time = time.time()
    s.flatten(root)
    dfs_end_time = time.time() - dfs_start_time
    print(f"BidirectionalAStar execution time = {dfs_end_time:f} seconds")
