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


class Tree:
    # Binary Search Tree Data Structure
    # Constructor
    def __init__(self, initval=None) -> None:
        """
        An empty left and right branches will be created for every value inserted,
        to perform better in recursive methods
        """
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    # Empty nodes are None valued
    def isempty(self) -> bool:
        """Returns true if tree is empty else False"""
        return self.value == None

    def isleaf(self) -> bool:
        """Returns true if leaf is a node"""
        return self.value != None and self.left.isempty() and self.right.isempty()

    # Inorder Traversal
    def inorder(self) -> list:
        """Returns a list sorted in increasing order from the Binary Search Tree."""
        # Corner Case
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    # Display Tree
    def __str__(self) -> str:
        """Prints the sorted tree"""
        return str(self.inorder())

    # Insert new element
    def insert(self, v) -> None:
        """Inserts the value v to the Binary Search Tree"""
        # Create new tree
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()

        # Value already exists
        if self.value == v:
            return

        if v < self.value:
            self.left.insert(v)
            return
        if v > self.value:
            self.right.insert(v)
            return


def tree_sort(L) -> list:
    """
    Returns a list L sorted in increasing order from the Binary Search Tree.
    >>> tree_sort([23235,82107,35775,91961,4323,40556,76603,64302,27316,74372])
    [4323, 23235, 27316, 35775, 40556, 64302, 74372, 76603, 82107, 91961]
    >>> tree_sort([50,52,54,74,93,100,114,124,130,143])
    [50, 52, 54, 74, 93, 100, 114, 124, 130, 143]
    """
    if L == [] or len(L) == 1:
        return L
    T = Tree()
    for i in L:
        T.insert(i)
    return T.inorder()


if __name__ == "__main__":
    print(
        tree_sort([23235, 82107, 35775, 91961, 4323, 40556, 76603, 64302, 27316, 74372])
    )
