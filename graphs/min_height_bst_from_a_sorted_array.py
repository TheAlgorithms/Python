"""
Given a sorted array, create a binary search tree with minimal height.

Example 1:
Input:
[1, 2, 3, 4, 5, 6, 7]

Output:
[4, 2, 6, 1, 3, 5, 7]

Explanation:
         4
       /   \
      2     6
     / \   / \
    1   3  5  7

Example 2:
Input:
[-3, 1, 2, 3, 5, 6, 8, 11]

Output:
[5, 2, 8, 1, 3, 6, 11, -3]

Explanation:
        5
      /   \
     2     8
    / \   / \
   1   3 6  11
  /
-3


Example 3:
Input:
[1, 2, 3, 4]

Output:
[3, 2, 4, 1]

Explanation:
     3
    / \
   2   4
  /
 1
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None # Points to another TreeNode object
        self.right = None # Points to another TreeNode object

class Solution:
    def _build_min_height_bst(self, nums, left, right):
        if left >= right:
            return None
        mid_idx = left + (right-left) // 2
        new_node = TreeNode(nums[mid_idx])
        new_node.left = self._build_min_height_bst(nums, left, mid_idx)
        new_node.right = self._build_min_height_bst(nums, mid_idx+1, right)

        return new_node

    def sortedArrayToBST(self, nums):
        final_ans = self._build_min_height_bst(nums, 0, len(nums))
        return final_ans

sol = Solution()
print(sol.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7]))
