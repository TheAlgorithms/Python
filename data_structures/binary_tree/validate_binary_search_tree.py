from __future__ import annotations

# Storing inorder traversal values into this list
traversed_node_values = []  # type: list[int]


class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def display(tree: Node | None) -> None:  # In Order traversal of the tree
    """
    >>> root = Node(1)
    >>> root.left = Node(0)
    >>> root.right = Node(2)
    >>> display(root)
    0
    1
    2
    >>> display(root.right)
    2
    """
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)


def inorder_traversal(tree: Node | None) -> None:
    """
    Inserts value of nodes into list `traversed_node_values` inorder fashion

    >>> root = Node(10)
    >>> root.left = Node(0)
    >>> root.right = Node(20)
    >>> inorder_traversal(root)
    """
    if tree is None:
        return
    inorder_traversal(tree.left)
    traversed_node_values.append(tree.data)
    inorder_traversal(tree.right)


def is_valid_bst(tree: Node) -> bool:
    """
    Returns True if this is a valid binary tree

    >>> tree = Node(20)
    >>> tree.left = Node(10)
    >>> tree.right = Node(30)
    >>> traversed_node_values.clear()
    >>> is_valid_bst(tree)
    True
    >>> tree = Node(20)
    >>> tree.left = Node(11)
    >>> tree.right = Node(5)
    >>> is_valid_bst(tree)
    False
    >>> tree = Node(20)
    >>> tree.left = Node(11)
    >>> tree.right = Node(55)
    >>> is_valid_bst(tree)
    True
    """
    traversed_node_values.clear()
    if tree is None:
        return True
    inorder_traversal(tree)

    """
    Now, if `traversed_node_values` is sorted and doesn't contain any duplicate values
    it means the given tree is valid binary search tree
    """
    for i in range(len(traversed_node_values) - 1):
        if traversed_node_values[i] >= traversed_node_values[i + 1]:
            return False
    return True


def main() -> None:
    """
    Main function for testing.

    >>> tree = Node(20)
    >>> tree.left = Node(10)
    >>> tree.right = Node(30)
    >>> display(tree)
    10
    20
    30
    >>> is_valid_bst(tree)
    True

    >>> tree = Node(10)
    >>> tree.left = Node(30)
    >>> tree.right = Node(20)
    >>> display(tree)
    30
    10
    20
    >>> is_valid_bst(tree)
    False
    """
    tree = Node(2)
    tree.left = Node(1)
    tree.right = Node(3)

    print("Tree is: ")
    display(tree)
    print("Tree is valid binary search tree: ", is_valid_bst(tree))


if __name__ == "__main__":
    main()
