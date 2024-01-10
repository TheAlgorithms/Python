"""
The floor of a key 'k' in a BST is the maximum
value that is smaller than or equal to 'k'.

The ceiling of a key 'k' in a BST is the minimum
value that is greater than or equal to 'k'.

Reference:
https://bit.ly/46uB0a2

Author : Arunkumar
Date : 14th October 2023
"""


class TreeNode:
    def __init__(self, key: int) -> None:
        """
        Initialize a TreeNode with the given key.

        Args:
            key (int): The key value for the node.
        """
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def floor_ceiling(root: TreeNode | None, key: int) -> tuple[int | None, int | None]:
    """
    Find the floor and ceiling values for a given key in a Binary Search Tree (BST).

    Args:
        root (TreeNode): The root of the BST.
        key (int): The key for which to find the floor and ceiling.

    Returns:
        tuple[int | None, int | None]:
        A tuple containing the floor and ceiling values, respectively.

    Examples:
        >>> root = TreeNode(10)
        >>> root.left = TreeNode(5)
        >>> root.right = TreeNode(20)
        >>> root.left.left = TreeNode(3)
        >>> root.left.right = TreeNode(7)
        >>> root.right.left = TreeNode(15)
        >>> root.right.right = TreeNode(25)
        >>> floor, ceiling = floor_ceiling(root, 8)
        >>> floor
        7
        >>> ceiling
        10
        >>> floor, ceiling = floor_ceiling(root, 14)
        >>> floor
        10
        >>> ceiling
        15
    """
    floor_val = None
    ceiling_val = None

    while root is not None:
        if root.key == key:
            floor_val = root.key
            ceiling_val = root.key
            break

        if key < root.key:
            ceiling_val = root.key
            root = root.left
        else:
            floor_val = root.key
            root = root.right

    return floor_val, ceiling_val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
