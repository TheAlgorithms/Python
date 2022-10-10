# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest
# path from the root node down to the farthest leaf node.

from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def height_of_tree(root: TreeNode | None, depth=0) -> int:
    """
    Function returns the height of tree

    >>> height_of_tree(None)
    0
    """
    # Base condition of recurrsion, if the root is not present return the current depth
    if not root:
        return depth
    # Same like dfs, go as much as you can in depth and return the maximum possible depth
    return max(
        height_of_tree(root.left, depth + 1),
        height_of_tree(root.right, depth + 1)
    )


# Example 1

"""
    3       ->  1
   / \
  9   20    ->  2
     /  \
    15   7  ->  3
"""
tree_1 = TreeNode(3)
tree_1.left = TreeNode(9)
tree_1.right = TreeNode(20)
tree_1.right.left = TreeNode(15)
tree_1.right.right = TreeNode(7)

print(height_of_tree(tree_1))  # Output: 3


if __name__ == "__main__":
    import doctest

    doctest.testmod()
