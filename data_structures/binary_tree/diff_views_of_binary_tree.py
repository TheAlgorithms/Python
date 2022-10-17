"""
Problem:
Given root of binary Tree, print the

1. binary-tree-right-side-view
2. binary-tree-left-side-view
3. binary-tree-top-side-view
4. binary-tree-bottom-side-view


1. binary-tree-right-side-view

    3       <-  3
   / \
  9   20    <-  20
     /  \
    15   7  <-  7

Output: [3, 20, 7]


2. binary-tree-left-side-view

3  ->    3
        / \
9  ->  9   20
          /  \
15 ->    15   7

Output: [3, 9, 15]


3. binary-tree-top-side-view

  9 3 20 7
  ⬇ ⬇ ⬇  ⬇

    3
   / \
  9   20
     /  \
    15   7

Output: [9, 3, 20, 7]

4. binary-tree-bottom-side-view

    3
   / \
  9   20
     /  \
    15   7
  ↑  ↑ ↑  ↑
  9 15 20 7

Output: [9, 15, 20, 7]

"""

from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the right side view of binary tree.

    >>> binary_tree_right_side_view(None)
    []

    >>> tree_1 = TreeNode(3)
    >>> tree_1.left = TreeNode(9)
    >>> tree_1.right = TreeNode(20)
    >>> tree_1.right.left = TreeNode(15)
    >>> tree_1.right.right = TreeNode(7)
    >>> binary_tree_right_side_view(tree_1)
    [3, 20, 7]
    """

    def dfs(root: TreeNode | None, depth: int, right_view: list[int]) -> None:
        """
        A depth first search preorder traversal to append the values at
        right side of tree.

        >>> dfs([], 0, [])
        None
        """
        if not root:
            return

        if depth == len(right_view):
            right_view.append(root.val)

        dfs(root.right, depth + 1, right_view)
        dfs(root.left, depth + 1, right_view)

    right_view: list = []
    if not root:
        return right_view
    dfs(root, 0, right_view)
    return right_view


def binary_tree_left_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the left side view of binary tree.

    >>> binary_tree_left_side_view(None)
    []


    >>> tree_1 = TreeNode(3)
    >>> tree_1.left = TreeNode(9)
    >>> tree_1.right = TreeNode(20)
    >>> tree_1.right.left = TreeNode(15)
    >>> tree_1.right.right = TreeNode(7)
    >>> binary_tree_left_side_view(tree_1)
    [3, 9, 15]
    """

    def dfs(root: TreeNode | None, depth: int, left_view: list[int]) -> None:
        """
        A depth first search preorder traversal to append the values
        at left side of tree.

        >>> dfs([], 0, [])
        None
        """
        if not root:
            return

        if depth == len(left_view):
            left_view.append(root.val)

        dfs(root.left, depth + 1, left_view)
        dfs(root.right, depth + 1, left_view)

    left_view: list = []
    if not root:
        return left_view
    dfs(root, 0, left_view)
    return left_view


def binary_tree_top_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the top side view of binary tree.

    >>> binary_tree_top_side_view(None)
    []


    >>> tree_1 = TreeNode(3)
    >>> tree_1.left = TreeNode(9)
    >>> tree_1.right = TreeNode(20)
    >>> tree_1.right.left = TreeNode(15)
    >>> tree_1.right.right = TreeNode(7)
    >>> binary_tree_top_side_view(tree_1)
    [9, 3, 20, 7]
    """
    from collections import defaultdict

    def breadth_first_search(root: TreeNode, top_view: list[int]) -> None:
        """
        A breadth first search traversal with defaultdict ds to append
        the values of tree from top view

        >>> bfs(TreeNode(5), [])
        None
        """
        queue = [(root, 0)]
        lookup = defaultdict(list)

        while queue:
            first = queue.pop(0)
            node, hd = first
            lookup[hd].append(node.val)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        for key, val in sorted(lookup.items(), key=lambda each: each[0]):
            top_view.append(val[0])

    top_view: list = []
    if not root:
        return top_view
    bfs(root, top_view)
    return top_view


def binary_tree_bottom_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the bottom side view of binary tree

    >>> binary_tree_bottom_side_view(None)
    []

    >>> tree_1 = TreeNode(3)
    >>> tree_1.left = TreeNode(9)
    >>> tree_1.right = TreeNode(20)
    >>> tree_1.right.left = TreeNode(15)
    >>> tree_1.right.right = TreeNode(7)
    >>> binary_tree_bottom_side_view(tree_1)
    [9, 15, 20, 7]
    """
    from collections import defaultdict

    def bfs(root: TreeNode, bottom_view: list[int]) -> None:
        """
        A breadth first search traversal with defaultdict ds to append
        the values of tree from bottom view

        >>> bfs(TreeNode(5), [])
        None
        """
        queue = [(root, 0)]
        lookup = defaultdict(list)

        while queue:
            first = queue.pop(0)
            node, hd = first
            lookup[hd].append(node.val)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        for key, val in sorted(lookup.items(), key=lambda each: each[0]):
            bottom_view.append(val[-1])

    bottom_view: list = []
    if not root:
        return bottom_view
    bfs(root, bottom_view)
    return bottom_view


if __name__ == "__main__":
    import doctest

    doctest.testmod()
