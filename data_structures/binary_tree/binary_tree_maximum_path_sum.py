"""
A path in a binary tree is a sequence of nodes where each pair
of adjacent nodes in the sequence has an edge connecting
them. A node can only appear in the sequence at most once. Note
that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Leetcode Reference : https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


class TreeNode:

    """
    TreeNode has tree variables, val -> Stores value of the node
    left, right -> Stores the pointer to left or right node.
    """

    def __init__(self, val: int, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class GetMaxPathSum:

    r"""

    GetMaxPathSum takes root node of a tree as initial argument.
    Upon calling max_path_sum(), it returns maximum path
    sum from the tree.

    # Test

    The below tree looks like this
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1

    Result will be calculated like : 3 -> 3 -> 5 -> 10 -> -3 -> 11
    As it is the maximum path possible.


    >>> root = TreeNode(10)
    >>> root.left = TreeNode(5)
    >>> root.right = TreeNode(-3)
    >>> root.left.left = TreeNode(3)
    >>> root.left.right = TreeNode(2)
    >>> root.right.right = TreeNode(11)
    >>> root.left.left.left = TreeNode(3)
    >>> root.left.left.right = TreeNode(-2)
    >>> root.left.right.right = TreeNode(1)

    >>> GetMaxPathSum(root).max_path_sum()
    29
    """

    def __init__(self, root):
        self.sum = -9999999999
        self.root = root

    def traverse(self, root: TreeNode | None) -> int:

        """
        Returns maximum path sum by recursively taking max_path_sum from left
        and max_path_sum from right if current Node has a left or right Node.

        :param root -> tree root:
        :return int:
        """

        if root is None:
            return 0

        right_sum = max(self.traverse(root.right), 0)
        left_sum = max(self.traverse(root.left), 0)

        val = root.val + right_sum + left_sum
        self.sum = max(val, self.sum)

        return root.val + max(right_sum, left_sum)

    def max_path_sum(self) -> int:

        """
        Driver method to get max_path_sum by calling traverse method.
        :return max_path_sum:
        """
        self.traverse(self.root)
        return self.sum


def construct_tree() -> TreeNode:
    """
    The below tree
       -10
       / \
      9   20
         /  \
       15    7
    """

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


if __name__ == '__main__':
    import doctest

    tree = GetMaxPathSum(construct_tree())
    max_sum = tree.max_path_sum()

    print("Given example output: ", max_sum)

    doctest.testmod()
