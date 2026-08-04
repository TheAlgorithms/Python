"""
Binary Tree Construction from Preorder/Inorder or Postorder/Inorder sequences.

This module allows building a binary tree when given:

- Preorder and inorder sequences
- Postorder and inorder sequences

Doctest examples are included for verification.
"""

from __future__ import annotations  # for forward references


class Node:
    """Class representing a node in a binary tree."""

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


def inorder_traversal(root: Node | None, out: list[int]) -> None:
    """Perform normal inorder traversal and store values in 'out' list."""
    if root is None:
        return
    inorder_traversal(root.left, out)
    out.append(root.data)
    inorder_traversal(root.right, out)


def _build_tree_from_preorder(
    preorder: list[int],
    pre_start: int,
    pre_end: int,
    inorder: list[int],
    in_start: int,
    in_end: int,
    in_map: dict[int, int],
) -> Node | None:
    """Internal recursive function to build tree from preorder & inorder."""
    if pre_start > pre_end or in_start > in_end:
        return None

    root = Node(preorder[pre_start])
    in_root_index = in_map[root.data]
    nums_left = in_root_index - in_start

    root.left = _build_tree_from_preorder(
        preorder,
        pre_start + 1,
        pre_start + nums_left,
        inorder,
        in_start,
        in_root_index - 1,
        in_map,
    )
    root.right = _build_tree_from_preorder(
        preorder,
        pre_start + nums_left + 1,
        pre_end,
        inorder,
        in_root_index + 1,
        in_end,
        in_map,
    )

    return root


def build_tree_from_preorder(inorder: list[int], preorder: list[int]) -> Node | None:
    """Build binary tree from preorder and inorder sequences."""
    in_map = {val: idx for idx, val in enumerate(inorder)}
    return _build_tree_from_preorder(
        preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, in_map
    )


def _build_tree_from_postorder(
    postorder: list[int],
    post_start: int,
    post_end: int,
    inorder: list[int],
    in_start: int,
    in_end: int,
    in_map: dict[int, int],
) -> Node | None:
    """
    Internal recursive function to build tree from postorder & inorder.

    Example:
    >>> inorder_seq = [1, 2, 3]
    >>> postorder_seq = [1, 3, 2]
    >>> inmp = {v:i for i,v in enumerate(inorder_seq)}
    >>> root = _build_tree_from_postorder(
    ...     postorder_seq, 0, 2, inorder_seq, 0, 2, inmp
    ... )
    >>> root.data
    2
    >>> root.left.data
    1
    >>> root.right.data
    3
    """
    if post_start > post_end or in_start > in_end:
        return None

    root = Node(postorder[post_end])
    in_root_index = in_map[root.data]
    nums_left = in_root_index - in_start

    root.left = _build_tree_from_postorder(
        postorder,
        post_start,
        post_start + nums_left - 1,
        inorder,
        in_start,
        in_root_index - 1,
        in_map,
    )
    root.right = _build_tree_from_postorder(
        postorder,
        post_start + nums_left,
        post_end - 1,
        inorder,
        in_root_index + 1,
        in_end,
        in_map,
    )

    return root


def build_tree_from_postorder(inorder: list[int], postorder: list[int]) -> Node | None:
    """Build binary tree from postorder and inorder sequences."""
    in_map = {val: idx for idx, val in enumerate(inorder)}
    return _build_tree_from_postorder(
        postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1, in_map
    )


if __name__ == "__main__":
    inorder_seq = [1, 2, 3, 4, 5]
    preorder_seq = [3, 2, 1, 4, 5]
    postorder_seq = [1, 2, 5, 4, 3]

    tree_pre = build_tree_from_preorder(inorder_seq, preorder_seq)
    tree_post = build_tree_from_postorder(inorder_seq, postorder_seq)

    out: list[int] = []
    inorder_traversal(tree_pre, out)
    print("Inorder from Preorder Tree:", out)
    out.clear()
    inorder_traversal(tree_post, out)
    print("Inorder from Postorder Tree:", out)
