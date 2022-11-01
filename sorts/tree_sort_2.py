"""

tree_sort_2

- makes use of the data structure Binary Tree to sort the list in O(nlogn) time.
- Binary Search Tree [BST]
  - For each node with value v
    - All values in the left subtree are < v
    - All values in the right subtree are > v
  - No Duplicate values.
- Logic:
  - Build a Binary Search Tree
  - Traverse the tree in increasing order.

"""
from typing import Any


class TreeSort:
    """
    Binary Search Tree Data Structure
        - An empty left and right branches will be created for every value inserted,
        to perform better in recursive methods
    """

    # Constructor
    def __init__(self, initval: Any = None) -> None:
        self.value: Any
        self.left: Any
        self.right: Any

        self.value = initval
        if self.value:
            self.left = TreeSort()
            self.right = TreeSort()
        else:
            self.left = None
            self.right = None

    def isempty(self) -> bool:
        """
        Empty nodes are None valued.
        Returns true if tree is empty else False
        >>> tree = TreeSort()
        >>> tree.isempty()
        True
        >>> tree.insert(1)
        >>> tree.isempty()
        False
        """
        if self.value is None:
            return True
        return False

    # Inorder Traversal
    def inorder(self) -> list:
        """
        Returns a list sorted in increasing order from the Binary Search Tree.
        >>> tree = TreeSort()
        >>> list_data = [23235,82107,35775,91961,4323,40556,76603,64302,27316,74372]
        >>> for data in list_data:
        ...     tree.insert(data)
        >>> tree.inorder()
        [4323, 23235, 27316, 35775, 40556, 64302, 74372, 76603, 82107, 91961]
        """
        # Corner Case
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    # Display Tree
    def __str__(self) -> str:
        """
        >>> tree = TreeSort()
        >>> list_data = [23235,82107,35775,91961,4323,40556,76603,64302,27316,74372]
        >>> for data in list_data:
        ...     tree.insert(data)
        >>> print(tree)
        [4323, 23235, 27316, 35775, 40556, 64302, 74372, 76603, 82107, 91961]
        """
        return str(self.inorder())

    # Insert new element
    def insert(self, data: Any) -> None:
        """
        Inserts the value data to the Binary Search Tree
        Let
        >>> tree = TreeSort()
        >>> tree.insert(1)
        >>> print(tree)
        [1]
        >>> tree.insert(2)
        >>> print(tree)
        [1, 2]
        >>> tree.insert(3)
        >>> print(tree)
        [1, 2, 3]
        """
        # Create new tree
        if self.isempty():
            self.value = data
            self.left = TreeSort()
            self.right = TreeSort()

        # Value already exists
        if self.value == data:
            return

        if data < self.value:
            self.left.insert(data)
            return
        if data > self.value:
            self.right.insert(data)
            return


def tree_sort(list_data: list) -> list:
    """
    Returns a list array sorted in increasing order from the Binary Search Tree.
    >>> tree_sort([23235,82107,35775,91961,4323,40556,76603,64302,27316,74372])
    [4323, 23235, 27316, 35775, 40556, 64302, 74372, 76603, 82107, 91961]
    >>> tree_sort([50,52,54,74,93,100,114,124,130,143])
    [50, 52, 54, 74, 93, 100, 114, 124, 130, 143]
    """
    if len(list_data) == 0 or len(list_data) == 1:
        return list_data
    tree = TreeSort()
    for i in list_data:
        tree.insert(i)
    return tree.inorder()


if __name__ == "__main__":
    print(
        tree_sort([23235, 82107, 35775, 91961, 4323, 40556, 76603, 64302, 27316, 74372])
    )
