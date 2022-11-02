"""
Author  : Alexander Pantyukhin
Date    : November 2, 2022

Task:
Given the root of a binary tree, determine if it is a valid binary search
tree (BST).

A valid BST is defined as follows:

 - The left subtree of a node contains only nodes with keys less than the node's key.
 - The right subtree of a node contains only nodes with keys greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.

Implementation notes:
Depth-first search approach.

leetcode: https://leetcode.com/problems/validate-binary-search-tree/

Let n is the number of nodes in tree
Runtime: O(n)
Space: O(1)
"""



class TreeNode:
    def __init__(
        self,
        data: float = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right


def is_bst(root: TreeNode | None) -> bool:
    """
    >>> is_bst(TreeNode(2, TreeNode(1), TreeNode(3)))
    True

    >>> is_bst(TreeNode(0, TreeNode(-11), TreeNode(3)))
    True

    >>> is_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3))))
    False

    >>> is_bst(TreeNode('a', TreeNode(1), TreeNode(4, TreeNode(3))))
    Traceback (most recent call last):
     ...
    ValueError: Each node should be type of TreeNode and data should be float.

    >>> is_bst(TreeNode(2, TreeNode([]), TreeNode(4, TreeNode(3))))
    Traceback (most recent call last):
     ...
    ValueError: Each node should be type of TreeNode and data should be float.
    """

    # Validation
    def is_valid_tree(node: TreeNode | None) -> bool:
        """
        >>> is_valid_tree(None)
        True

        >>> is_valid_tree('abc')
        False

        >>> is_valid_tree(TreeNode('not a float'))
        False

        >>> is_valid_tree(TreeNode(1, TreeNode('123')))
        False
        """
        if node is None:
            return True

        if not isinstance(node, TreeNode):
            return False

        try:
            float(node.data)
        except:
            return False

        return is_valid_tree(node.left) and is_valid_tree(node.right)

    if not is_valid_tree(root):
        raise ValueError(
            "Each node should be type of TreeNode and data should be float."
        )

    def is_bst_internal(
        node: TreeNode | None, left_bound: float, right_bound: float
    ) -> bool:
        """
        >>> is_bst_internal(None)
        True
        """

        if node is None:
            return True

        return (
            (node.data > left_bound)
            and (node.data < right_bound)
            and is_bst_internal(node.left, left_bound, node.data)
            and is_bst_internal(node.right, node.data, right_bound)
        )

    return is_bst_internal(root, -float("inf"), float("inf"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
