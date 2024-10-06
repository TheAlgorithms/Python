class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode' | None=None, right: 'TreeNode' | None =None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_sum_bst(root: TreeNode) -> int:
    """
    The solution traverses a binary tree to find the maximum sum of
    keys in any subtree that is a Binary Search Tree (BST). It uses
    recursion to validate BST properties and calculates sums, returning
    the highest sum found among all valid BST subtrees.

    >>> t1 = TreeNode(4)
    >>> t1.left = TreeNode(3)
    >>> t1.left.left = TreeNode(1)
    >>> t1.left.right = TreeNode(2)
    >>> print(max_sum_bst(t1))
    2
    >>> t2 = TreeNode(-4)
    >>> t2.left = TreeNode(-2)
    >>> t2.right = TreeNode(-5)
    >>> print(max_sum_bst(t2))
    0
    >>> t3 = TreeNode(1)
    >>> t3.left = TreeNode(4)
    >>> t3.left.left = TreeNode(2)
    >>> t3.left.right = TreeNode(4)
    >>> t3.right = TreeNode(3)
    >>> t3.right.left = TreeNode(2)
    >>> t3.right.right = TreeNode(5)
    >>> t3.right.right.left = TreeNode(4)
    >>> t3.right.right.right = TreeNode(6)
    >>> print(max_sum_bst(t3))
    20
    """
    ans = 0

    def solver(node) -> int:
        """
        Returns the maximum sum by making recursive calls
        """
        nonlocal ans

        if not node:
            return True, float("inf"), float("-inf"), 0  # Valid BST, min, max, sum

        is_left_valid, min_left, max_left, sum_left = solver(node.left)
        is_right_valid, min_right, max_right, sum_right = solver(node.right)

        if is_left_valid and is_right_valid and max_left < node.val < min_right:
            total_sum = sum_left + sum_right + node.val
            ans = max(ans, total_sum)
            return True, min(min_left, node.val), max(max_right, node.val), total_sum

        return False, -1, -1, -1  # Not a valid BST

    solver(root)
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
