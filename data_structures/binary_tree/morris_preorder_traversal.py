"""
Problem Statement: Given a binary perform an preorder traversal using Morris Preorder
traversal algorithm. (Iterative version of Preorder traversal of tree)

https://www.geeksforgeeks.org/morris-traversal-for-preorder/
"""


class TreeNode:
    """
    Class representing a node in a binary tree.

    Attributes:
    -----------
    value : The value stored at the node.
    left :  Pointer to the left child node (default is None).
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
    >>> bt.morris_preorder_traversal()
    [9, 6, 3, 2, 5, 4, 7, 10, 12]

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

    def morris_preorder_traversal(self) -> list[int]:
        """
        Function for preorder traversal using morris preorder traversal.

        Algorithm :
        ------------
        First initialize current as root node.

        while current node is not empty
            If the current node has no left child.
                print the current node.
                point the current node to its right child

            else.
                find predecssor node of the current node.
                if predecessor right child points to current node,
                    remove the link of the right child of predecessor node.
                    point the current node to its right child.
                else,
                    print the current node
                    make the current node as the right child of the predecessor node.
                    point current node to its left child.

        Returns:
        --------
        A list of integers representing the preorder traversal.



        """
        preorder_traversal = []
        current_node = self.root

        while current_node:
            if current_node.left is None:
                preorder_traversal.append(current_node.value)
                current_node = current_node.right
            else:
                predecessor_node = self._predecessor(current_node)
                if predecessor_node.right == current_node:
                    predecessor_node.right = None
                    current_node = current_node.right
                else:
                    preorder_traversal.append(current_node.value)
                    predecessor_node.right = current_node
                    current_node = current_node.left
        return preorder_traversal


if __name__ == "__main__":
    import doctest

    doctest.testmod()
