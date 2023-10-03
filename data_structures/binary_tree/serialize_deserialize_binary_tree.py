from __future__ import annotations

class TreeNode:
    """
    A binary tree node has a value, left child, and right child.

    Props:
        val(int): The value of the node.
        left: The left child of the node.
        right: The right child of the node.
    """

    def __init__(self, val: int = 0, left:TreeNode = None, right:TreeNode = None) -> None:
        if not isinstance(val, int):
            raise TypeError("Value must be an integer.")
        self.val = val
        self.left = left
        self.right = right


# Helper functions
def are_trees_identical(root1: TreeNode, root2: TreeNode) -> bool:
    """
    Check if two binary trees are identical.

    Args:
        root1 (TreeNode): Tree 1
        root2 (TreeNode): Tree 2

    Returns:
        bool: True if the trees are identical, False otherwise.

    >>> root1 = TreeNode(1)
    >>> root1.left = TreeNode(2)
    >>> root1.right = TreeNode(3)
    >>> root2 = TreeNode(1)
    >>> root2.left = TreeNode(2)
    >>> root2.right = TreeNode(3)
    >>> are_trees_identical(root1, root2)
    True
    >>> root1 = TreeNode(1)
    >>> root1.left = TreeNode(2)
    >>> root1.right = TreeNode(3)
    >>> root2 = TreeNode(1)
    >>> root2.left = TreeNode(2)
    >>> root2.right = TreeNode(4)
    >>> are_trees_identical(root1, root2)
    False
    """

    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    return (
        root1.val == root2.val
        and are_trees_identical(root1.left, root2.left)
        and are_trees_identical(root1.right, root2.right)
    )


# Main functions
def serialize(root: TreeNode) -> str:
    """
    Serialize a binary tree to a string using preorder traversal.

    Args:
        root(TreeNode): The root of the binary tree.

    Returns:
        A string representation of the binary tree.

    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> root.right.left = TreeNode(4)
    >>> root.right.right = TreeNode(5)
    >>> serialize(root)
    '1,2,null,null,3,4,null,null,5,null,null'
    >>> root = TreeNode(1)
    >>> serialize(root)
    '1,null,null'
    """

    # Use "null" to represent empty nodes in the serialization
    if not root:
        return "null"

    return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)


def deserialize(data: str) -> TreeNode:
    """
    Deserialize a string to a binary tree.

    Args:
        data(str): The serialized string.

    Returns:
        The root of the binary tree.

    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> root.right.left = TreeNode(4)
    >>> root.right.right = TreeNode(5)
    >>> serialzed_data = serialize(root)
    >>> deserialized = deserialize(serialzed_data)
    >>> are_trees_identical(root, deserialized)
    True
    >>> root = TreeNode(1)
    >>> serialzed_data = serialize(root)
    >>> dummy_data = "1,2,null,null,3,4,null,null,5,null,null"
    >>> deserialized = deserialize(dummy_data)
    >>> are_trees_identical(root, deserialized)
    False
    """

    # Split the serialized string by comma to get node values
    nodes = data.split(",")

    def build_tree() -> TreeNode:
        # Get the next value from the list
        val = nodes.pop(0)

        if val == "null":
            return None

        node = TreeNode(int(val))
        node.left = build_tree()  # Recursively build left subtree
        node.right = build_tree()  # Recursively build right subtree

        return node

    return build_tree()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
