"""
Build a binary tree from preorder + inorder or postorder + inorder traversals.

This module provides two main functions:
- build_tree_from_preorder_and_inorder()
- build_tree_from_postorder_and_inorder()

Each builds a binary tree represented by Node objects.

References:
    - https://en.wikipedia.org/wiki/Binary_tree
    - https://en.wikipedia.org/wiki/Tree_traversal
"""

from typing import Dict, List, Optional


class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
        data (int): The value of the node.
        left (Optional[Node]): Pointer to the left child.
        right (Optional[Node]): Pointer to the right child.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder_traversal(root: Optional[Node]) -> List[int]:
    """
    Return the inorder traversal of a binary tree as a list.

    >>> root = Node(3)
    >>> root.left = Node(2)
    >>> root.right = Node(4)
    >>> inorder_traversal(root)
    [2, 3, 4]
    """
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)


def _build_tree_from_preorder(
    preorder: List[int],
    pre_start: int,
    pre_end: int,
    inorder_seq: List[int],
    in_start: int,
    in_end: int,
    inorder_map: Dict[int, int],
) -> Optional[Node]:
    """Helper function for building a tree recursively from preorder + inorder."""
    if pre_start > pre_end or in_start > in_end:
        return None

    root_value = preorder[pre_start]
    root = Node(root_value)
    in_root_index = inorder_map[root_value]
    left_subtree_size = in_root_index - in_start

    root.left = _build_tree_from_preorder(
        preorder,
        pre_start + 1,
        pre_start + left_subtree_size,
        inorder_seq,
        in_start,
        in_root_index - 1,
        inorder_map,
    )
    root.right = _build_tree_from_preorder(
        preorder,
        pre_start + left_subtree_size + 1,
        pre_end,
        inorder_seq,
        in_root_index + 1,
        in_end,
        inorder_map,
    )
    return root


def build_tree_from_preorder_and_inorder(
    inorder_seq: List[int], preorder_seq: List[int]
) -> Optional[Node]:
    """
    Build a binary tree from preorder and inorder traversals.

    Args:
        inorder_seq: The inorder traversal sequence.
        preorder_seq: The preorder traversal sequence.

    Returns:
        Root node of the reconstructed binary tree.

    >>> inorder_seq = [1, 2, 3, 4, 5]
    >>> preorder_seq = [3, 2, 1, 4, 5]
    >>> root = build_tree_from_preorder_and_inorder(inorder_seq, preorder_seq)
    >>> inorder_traversal(root)
    [1, 2, 3, 4, 5]
    """
    inorder_map = {value: i for i, value in enumerate(inorder_seq)}
    return _build_tree_from_preorder(
        preorder_seq,
        0,
        len(preorder_seq) - 1,
        inorder_seq,
        0,
        len(inorder_seq) - 1,
        inorder_map,
    )


def _build_tree_from_postorder(
    postorder: List[int],
    post_start: int,
    post_end: int,
    inorder_seq: List[int],
    in_start: int,
    in_end: int,
    inorder_map: Dict[int, int],
) -> Optional[Node]:
    """Helper function for building a tree recursively from postorder + inorder."""
    if post_start > post_end or in_start > in_end:
        return None

    root_value = postorder[post_end]
    root = Node(root_value)
    in_root_index = inorder_map[root_value]
    left_subtree_size = in_root_index - in_start

    root.left = _build_tree_from_postorder(
        postorder,
        post_start,
        post_start + left_subtree_size - 1,
        inorder_seq,
        in_start,
        in_root_index - 1,
        inorder_map,
    )
    root.right = _build_tree_from_postorder(
        postorder,
        post_start + left_subtree_size,
        post_end - 1,
        inorder_seq,
        in_root_index + 1,
        in_end,
        inorder_map,
    )
    return root


def build_tree_from_postorder_and_inorder(
    inorder_seq: List[int], postorder_seq: List[int]
) -> Optional[Node]:
    """
    Build a binary tree from postorder and inorder traversals.

    Args:
        inorder_seq: The inorder traversal sequence.
        postorder_seq: The postorder traversal sequence.

    Returns:
        Root node of the reconstructed binary tree.

    >>> inorder_seq = [1, 2, 3, 4, 5]
    >>> postorder_seq = [1, 2, 5, 4, 3]
    >>> root = build_tree_from_postorder_and_inorder(inorder_seq, postorder_seq)
    >>> inorder_traversal(root)
    [1, 2, 3, 4, 5]
    """
    inorder_map = {value: i for i, value in enumerate(inorder_seq)}
    return _build_tree_from_postorder(
        postorder_seq,
        0,
        len(postorder_seq) - 1,
        inorder_seq,
        0,
        len(inorder_seq) - 1,
        inorder_map,
    )


if __name__ == "__main__":
    # Example usage for manual verification (not part of algorithmic test)
    inorder_seq = [1, 2, 3, 4, 5]
    preorder_seq = [3, 2, 1, 4, 5]
    postorder_seq = [1, 2, 5, 4, 3]

    root_pre = build_tree_from_preorder_and_inorder(inorder_seq, preorder_seq)
    print("Inorder (from Preorder+Inorder):", inorder_traversal(root_pre))

    root_post = build_tree_from_postorder_and_inorder(inorder_seq, postorder_seq)
    print("Inorder (from Postorder+Inorder):", inorder_traversal(root_post))
