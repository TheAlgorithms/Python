# Morris Traversal for binary trees in O(n) time and O(1) auxiliary space.
"""
Morris Traversal is an algorithm that allows traversing a binary tree
(both In-Order and Pre-Order) in O(n) time complexity and O(1) auxiliary space,
without using recursion or an auxiliary call stack.

It works by temporarily linking the rightmost child of the current node's left
subtree (its in-order predecessor) to the current node (creating a threaded tree),
and then removing the link once the subtree has been processed.

References:
- https://en.wikipedia.org/wiki/Tree_traversal#Morris_in-order_traversal_using_threading
- J. H. Morris, "Traversing binary trees simply and cheaply",
  Information Processing Letters, vol. 9, no. 5, pp. 197-200, 1979.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    """
    A binary tree node containing an integer value and optional left/right children.
    """

    data: int
    left: Node | None = None
    right: Node | None = None


def morris_inorder_traversal(root: Node | None) -> list[int]:
    """
    Perform in-order traversal (Left, Root, Right) using Morris Traversal.

    Time Complexity: O(n) where n is the number of nodes.
    Auxiliary Space Complexity: O(1) as no recursion or call stack is used.

    >>> morris_inorder_traversal(None)
    []
    >>> morris_inorder_traversal(Node(10))
    [10]
    >>> tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    >>> morris_inorder_traversal(tree)
    [4, 2, 5, 1, 3]
    >>> skewed = Node(1, Node(2, Node(3)))
    >>> morris_inorder_traversal(skewed)
    [3, 2, 1]
    >>> right_skewed = Node(1, None, Node(2, None, Node(3)))
    >>> morris_inorder_traversal(right_skewed)
    [1, 2, 3]
    """
    traversal_result: list[int] = []
    current: Node | None = root

    while current is not None:
        if current.left is None:
            traversal_result.append(current.data)
            current = current.right
        else:
            # Find the in-order predecessor of current node
            predecessor: Node = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # Establish temporary thread link back to current
                predecessor.right = current
                current = current.left
            else:
                # Thread already exists; restore tree structure and visit current
                predecessor.right = None
                traversal_result.append(current.data)
                current = current.right

    return traversal_result


def morris_preorder_traversal(root: Node | None) -> list[int]:
    """
    Perform pre-order traversal (Root, Left, Right) using Morris Traversal.

    Time Complexity: O(n) where n is the number of nodes.
    Auxiliary Space Complexity: O(1) as no recursion or call stack is used.

    >>> morris_preorder_traversal(None)
    []
    >>> morris_preorder_traversal(Node(10))
    [10]
    >>> tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    >>> morris_preorder_traversal(tree)
    [1, 2, 4, 5, 3]
    >>> skewed = Node(1, Node(2, Node(3)))
    >>> morris_preorder_traversal(skewed)
    [1, 2, 3]
    >>> right_skewed = Node(1, None, Node(2, None, Node(3)))
    >>> morris_preorder_traversal(right_skewed)
    [1, 2, 3]
    """
    traversal_result: list[int] = []
    current: Node | None = root

    while current is not None:
        if current.left is None:
            traversal_result.append(current.data)
            current = current.right
        else:
            # Find the in-order predecessor of current node
            predecessor: Node = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # Visit current node before descending into the left subtree
                traversal_result.append(current.data)
                predecessor.right = current
                current = current.left
            else:
                # Thread already exists; restore tree structure
                predecessor.right = None
                current = current.right

    return traversal_result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
