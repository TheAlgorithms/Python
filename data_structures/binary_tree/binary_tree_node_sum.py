"""
Sum of all nodes in a binary tree.

Python implementation: 
    O(n) time complexity - Recurses through :meth:`depth_first_search`
                            with each element.
    O(n) space complexity - At any point in time maximum number of stack 
                            frames that could be in memory is `n`
"""


from __future__ import annotations


class Node:
    """
    A Node has value variable and pointers
    to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTreeNodeSum:
    r"""
    The below tree looks like this
        10
       /  \
      5   -3
     /    / \
    12   8  0

    >>> tree = Node(10)
    >>> BinaryTreeNodeSum(tree).node_sum()
    10

    >>> tree.left = Node(5)
    >>> BinaryTreeNodeSum(tree).node_sum()
    15

    >>> tree.right = Node(-3)
    >>> BinaryTreeNodeSum(tree).node_sum()
    12

    >>> tree.left.left = Node(12)
    >>> BinaryTreeNodeSum(tree).node_sum()
    24

    >>> tree.right.left = Node(8)
    >>> tree.right.right = Node(0)
    >>> BinaryTreeNodeSum(tree).node_sum()
    32
    """

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        if node is None:
            return 0
        return node.value + (
            self.depth_first_search(node.left) +
            self.depth_first_search(node.right)
        )

    def node_sum(self) -> int:
        return self.depth_first_search(self.tree)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

