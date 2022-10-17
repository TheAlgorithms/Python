"""
Illustrate how to implement inorder traversal in binary search tree.
Author: Gurneet Singh
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""


class BinaryTreeNode:
    """Defining the structure of BinaryTreeNode"""

    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None


def insert(node: BinaryTreeNode | None, new_value: int) -> BinaryTreeNode | None:
    """
    If the binary search tree is empty, make a new node and declare it as root.
    >>> node_a = BinaryTreeNode(12345)
    >>> node_b = insert(node_a, 67890)
    >>> node_a.left_child == node_b.left_child
    True
    >>> node_a.right_child == node_b.right_child
    True
    >>> node_a.data == node_b.data
    True
    """
    if node is None:
        node = BinaryTreeNode(new_value)
        return node

    # binary search tree is not empty,
    # so we will insert it into the tree
    # if new_value is less than value of data in node,
    #  add it to left subtree and proceed recursively
    if new_value < node.data:
        node.left_child = insert(node.left_child, new_value)
    else:
        # if new_value is greater than value of data in node,
        #  add it to right subtree and proceed recursively
        node.right_child = insert(node.right_child, new_value)
    return node


def inorder(node: None | BinaryTreeNode) -> list[int]:  # if node is None,return
    """
    >>> inorder(make_tree())
    [6, 10, 14, 15, 20, 25, 60]
    """
    if node:
        inorder_array = inorder(node.left_child)
        inorder_array = inorder_array + [node.data]
        inorder_array = inorder_array + inorder(node.right_child)
    else:
        inorder_array = []
    return inorder_array


def make_tree() -> BinaryTreeNode | None:

    root = insert(None, 15)
    insert(root, 10)
    insert(root, 25)
    insert(root, 6)
    insert(root, 14)
    insert(root, 20)
    insert(root, 60)
    return root


def main() -> None:
    # main function
    root = make_tree()
    print("Printing values of binary search tree in Inorder Traversal.")
    inorder(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
