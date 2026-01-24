"""
Problem Statement: Given a binary perform an inorder traversal using Morris Inorder
traversal algorithm. (Iterative version of Inorder traversal of tree)

https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
"""


class TreeNode:
    """
    Class representing a node in a binary tree.

    Attributes:
    -----------
    value : The value stored at the node.
    left : Pointer to the left child node (default is None).
    right : Pointer to the right child node (default is None).
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinaryTree:
    """
    Class representing a binary tree.

    >>> bt = BinaryTree()
    >>> bt.insert(9)
    >>> bt.insert(6)
    >>> bt.insert(10)
    >>> bt.insert(3)
    >>> bt.insert(7)
    >>> bt.insert(12)
    >>> bt.insert(2)
    >>> bt.insert(5)
    >>> bt.insert(4)
    >>> bt.morris_inorder_traversal()
    [2, 3, 4, 5, 6, 7, 9, 10, 12]

    """

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        """
        Insert a value into the binary tree.

        Parameters:
        -----------
        value : The value to be inserted into the binary tree.
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        """
        Helper function to insert a value recursively into the tree.

        Parameters:
        -----------
        node : The current node in the binary tree.
        value : The value to be inserted.
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif node.right is None:
            node.right = TreeNode(value)
        else:
            self._insert_recursive(node.right, value)

    def _predecessor(self, node: TreeNode) -> TreeNode:
        """
        Helper Function to return predecessor of the given node in a binary tree

        Parameters:
        -----------
        node : A node in the binary tree.

        Returns:
        --------
        The predecessor of the node passed in the parameter
        """
        temp_node = node.left
        while temp_node and temp_node.right and temp_node.right != node:
            temp_node = temp_node.right
        assert temp_node is not None, "Predecessor should not be None"
        return temp_node

    def morris_inorder_traversal(self) -> list[int]:
        """
        Function for inorder traversal using morris inorder traversal.

        Algorithm :
        ------------
        First set current node as root node.

        while current node is not empty
            If the current node has no left child.
                print the current node.
                point the current node to its right child

            else.
                find predecssor node of the current node.
                if predecessor has no right child,
                    make the current node as the right child of the predecessor node.
                    point current node to its left child.
                else,
                    remove the link of the right child of predecessor node.
                    print the current node
                    point the current node to its right child.

        Returns:
        --------
        A list of integers representing the inorder traversal.



        """
        inorder_traversal = []
        current_node = self.root

        while current_node:
            if current_node.left is None:
                inorder_traversal.append(current_node.value)
                current_node = current_node.right
            else:
                predecessor_node = self._predecessor(current_node)
                if predecessor_node.right is None:
                    predecessor_node.right = current_node
                    current_node = current_node.left
                else:
                    predecessor_node.right = None
                    inorder_traversal.append(current_node.value)
                    current_node = current_node.right
        return inorder_traversal


if __name__ == "__main__":
    import doctest

    doctest.testmod()
