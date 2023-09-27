"""
Author  : Alexander Pantyukhin
Date    : November 7, 2022

Task:
You are given a tree root of a binary tree with n nodes, where each node has
node.data coins. There are exactly n coins in whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node
to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Example 1:

   3
  / \
 0   0

Result: 2

Example 2:

   0
  / \
 3   0

Result 3

leetcode: https://leetcode.com/problems/distribute-coins-in-binary-tree/

Implementation notes:
User depth-first search approach.

Let n is the number of nodes in tree
Runtime: O(n)
Space: O(1)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class TreeNode:
    data: int
    left: TreeNode | None = None
    right: TreeNode | None = None


class CoinsDistribResult(NamedTuple):
    moves: int
    excess: int


def distribute_coins(root: TreeNode | None) -> int:
    """
    >>> distribute_coins(TreeNode(3, TreeNode(0), TreeNode(0)))
    2
    >>> distribute_coins(TreeNode(0, TreeNode(3), TreeNode(0)))
    3
    >>> distribute_coins(TreeNode(0, TreeNode(0), TreeNode(3)))
    3
    >>> distribute_coins(None)
    0
    >>> distribute_coins(TreeNode(0, TreeNode(0), TreeNode(0)))
    Traceback (most recent call last):
     ...
    ValueError: The nodes number should be same as the number of coins
    >>> distribute_coins(TreeNode(0, TreeNode(1), TreeNode(1)))
    Traceback (most recent call last):
     ...
    ValueError: The nodes number should be same as the number of coins
    """

    if root is None:
        return 0

    # Validation
    def count_nodes(node: TreeNode | None) -> int:
        """
        >>> count_nodes(None)
        0
        """
        if node is None:
            return 0

        return count_nodes(node.left) + count_nodes(node.right) + 1

    def count_coins(node: TreeNode | None) -> int:
        """
        >>> count_coins(None)
        0
        """
        if node is None:
            return 0

        return count_coins(node.left) + count_coins(node.right) + node.data

    if count_nodes(root) != count_coins(root):
        raise ValueError("The nodes number should be same as the number of coins")

    # Main calculation
    def get_distrib(node: TreeNode | None) -> CoinsDistribResult:
        """
        >>> get_distrib(None)
        namedtuple("CoinsDistribResult", "0 2")
        """

        if node is None:
            return CoinsDistribResult(0, 1)

        left_distrib_moves, left_distrib_excess = get_distrib(node.left)
        right_distrib_moves, right_distrib_excess = get_distrib(node.right)

        coins_to_left = 1 - left_distrib_excess
        coins_to_right = 1 - right_distrib_excess

        result_moves = (
            left_distrib_moves
            + right_distrib_moves
            + abs(coins_to_left)
            + abs(coins_to_right)
        )
        result_excess = node.data - coins_to_left - coins_to_right

        return CoinsDistribResult(result_moves, result_excess)

    return get_distrib(root)[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
