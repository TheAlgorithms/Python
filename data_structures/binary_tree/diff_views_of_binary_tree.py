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
    """
    def dfs(root: TreeNode | None, depth: int, right_view: list[int]) -> None:
        if not root:
            return
        
        if depth == len(right_view):
            right_view.append(root.val)
        
        dfs(root.right, depth + 1, right_view)
        dfs(root.left, depth + 1, right_view)

    right_view = []
    if not root:
        return right_view
    dfs(root, 0, right_view)
    return right_view

def binary_tree_left_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the left side view of binary tree.
    
    >>> binary_tree_left_side_view(None)
    []
    """
    def dfs(root: TreeNode | None, depth: int, left_view: list[int]) -> None:
        if not root:
            return
        
        if depth == len(left_view):
            left_view.append(root.val)
        
        dfs(root.left, depth + 1, left_view)
        dfs(root.right, depth + 1, left_view)

    left_view = []
    if not root:
        return left_view
    dfs(root, 0, left_view)
    return left_view

def binary_tree_top_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the top side view of binary tree.

    >>> binary_tree_top_side_view(None)
    []
    """
    from collections import defaultdict

    def bfs(root: TreeNode | None, top_view: list[int]) -> None:
        queue = [(root, 0)]
        lookup = defaultdict(list)

        while queue:
            first = queue.pop(0)
            node,hd = first
            lookup[hd].append(node.val)
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        for key, val in sorted(lookup.items(), key = lambda x:x[0]):
            top_view.append(val[0])
    
    top_view = []
    if not root:
        return top_view
    bfs(root, top_view)
    return top_view

def binary_tree_bottom_side_view(root: TreeNode | None) -> list[int]:
    """
    Function returns the bottom side view of binary tree

    >>> binary_tree_bottom_side_view(None)
    []
    """
    from collections import defaultdict

    def bfs(root: TreeNode | None, bottom_view: list[int]) -> None:
        queue = [(root, 0)]
        lookup = defaultdict(list)

        while queue:
            first = queue.pop(0)
            node,hd = first
            lookup[hd].append(node.val)
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        for key, val in sorted(lookup.items(), key = lambda x:x[0]):
            bottom_view.append(val[-1])
    
    bottom_view = []
    if not root:
        return bottom_view
    bfs(root, bottom_view)
    return bottom_view


tree_1 = TreeNode(3)
tree_1.left = TreeNode(9)
tree_1.right = TreeNode(20)
tree_1.right.left = TreeNode(15)
tree_1.right.right = TreeNode(7)

print(binary_tree_right_side_view(tree_1))  # Output: [3, 20, 7]
print(binary_tree_left_side_view(tree_1))   # Output: [3, 9, 15]
print(binary_tree_top_side_view(tree_1))    # Output: [9, 3, 20, 7]
print(binary_tree_bottom_side_view(tree_1)) # Output: [9, 15, 20, 7]

if __name__ == "__main__":
    import doctest

    doctest.testmod()