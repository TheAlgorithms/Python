"""
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Leetcode reference: https://leetcode.com/problems/symmetric-tree/
"""


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


class SymmetricTree:
    def is_symmetric_tree(self, tree: Node) -> bool:
        r"""
        Test cases for is_symmetric_tree function.

        The below tree looks like this
               1
             /   \
            2      2
           / \    / \
          3   4   4  3

        >>> tree = Node(1)
        >>> tree.left = Node(2)
        >>> tree.right = Node(2)
        >>> tree.left.left = Node(3)
        >>> tree.left.right = Node(4)
        >>> tree.right.left = Node(4)
        >>> tree.right.right = Node(3)

        >>> SymmetricTree().is_symmetric_tree(tree)
        True

        The below tree looks like this
              1
            /   \
          2      2
         / \    / \
        3   4   3  4

        >>> tree2 = Node(1)
        >>> tree2.left = Node(2)
        >>> tree2.right = Node(2)
        >>> tree2.left.left = Node(3)
        >>> tree2.left.right = Node(4)
        >>> tree2.right.left = Node(3)
        >>> tree2.right.right = Node(4)

        >>> SymmetricTree().is_symmetric_tree(tree2)
        False
        """
        if tree is None:
            # An empty tree is considered symmetric.
            return True
        return self.is_mirror(tree.left, tree.right)

    def is_mirror(self, left: Node | None, right: Node | Node) -> bool:
        """
        >>> tree1 = Node(1)
        >>> tree1.left = Node(2)
        >>> tree1.right = Node(2)
        >>> tree1.left.left = Node(3)
        >>> tree1.left.right = Node(4)
        >>> tree1.right.left = Node(4)
        >>> tree1.right.right = Node(3)
        >>> SymmetricTree().is_mirror(tree1.left, tree1.right)
        True
        """
        if left is None and right is None:
            # Both sides are empty, which is symmetric.
            return True
        if left is None or right is None:
            # One side is empty while the other is not, which is not symmetric.
            return False
        if left.data == right.data:
            # The values match, so check the subtree
            return self.is_mirror(left.left, right.right) and self.is_mirror(
                left.right, right.left
            )
        return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
