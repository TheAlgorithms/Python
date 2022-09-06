class Node:
    """
    A Node has data variable and pointers to Nodes to its left and right.
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def display(tree: Node | None) -> str:
    """
    In Order traversal of the tree

    >>> root = Node(1)
    >>> root.left = Node(0)
    >>> root.right = Node(2)
    >>> print(display(root))
    012
    >>> print(display(root.right))
    2
    """
    inorder_string: str = ""

    def inner_display(tree: Node | None) -> str:
        nonlocal inorder_string
        if tree:
            inner_display(tree.left)
            inorder_string += str(tree.data)
            inner_display(tree.right)
        return inorder_string

    inner_display(tree)
    return inorder_string


def inorder_traversal(tree: Node | None) -> list:
    """
    Iterate recursively and insert value of nodes into
    list `traversed_node_values` inorder fashion
    >>> root = Node(10)
    >>> root.left = Node(0)
    >>> root.right = Node(20)
    >>> print(inorder_traversal(root))
    [0, 10, 20]
    """
    # Storing inorder traversal values into this list
    traversed_node_values: list[int] = []

    def inner_inorder_traversal(tree: Node | None) -> None:
        if tree is None:
            return
        nonlocal traversed_node_values
        inner_inorder_traversal(tree.left)
        traversed_node_values.append(tree.data)
        inner_inorder_traversal(tree.right)

    inner_inorder_traversal(tree)
    return traversed_node_values


def is_valid_bst(tree: Node) -> bool:
    """
    Returns True if this is a valid binary tree

    >>> tree = Node(20)
    >>> tree.left = Node(10)
    >>> tree.right = Node(30)
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
    if tree is None:
        return True
    traversed_node_values = inorder_traversal(tree)

    """
    Now, if `traversed_node_values` is sorted and
    doesn't contain any duplicate values,
    it means the given tree is valid binary search tree
    """
    return not any(
        (value >= traversed_node_values[index + 1])
        for index, value in enumerate(traversed_node_values[:-1])
    )


def main() -> None:
    """
    Main function for testing.
    >>> tree = Node(20)
    >>> tree.left = Node(10)
    >>> tree.right = Node(30)
    >>> print(display(tree))
    102030
    >>> is_valid_bst(tree)
    True

    >>> tree = Node(10)
    >>> tree.left = Node(30)
    >>> tree.right = Node(20)
    >>> print(display(tree))
    301020

    >>> is_valid_bst(tree)
    False
    """
    tree = Node(2)
    tree.left = Node(1)
    tree.right = Node(3)

    print("Tree is: ")
    print(display(tree))
    print("Tree is valid binary search tree: ", is_valid_bst(tree))


if __name__ == "__main__":
    main()
