"""
Problem Statement: Given a binary perform an postorder traversal using Morris Postorder
traversal algorithm. (Iterative version of Postorder traversal of tree)

https://www.geeksforgeeks.org/morris-traversal-for-postorder/
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
    >>> bt.morris_postorder_traversal()
    [2, 4, 5, 3, 7, 6, 12, 10, 9]

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

    def _successor(self, node: TreeNode) -> TreeNode:
        """
        Helper Function to return successor of the given node in a binary tree

        Parameters:
        -----------
        node : A node in the binary tree.

        Returns:
        --------
        The successor of the node passed in the parameter
        """
        temp_node = node.right
        while temp_node and temp_node.left and temp_node.left != node:
            temp_node = temp_node.left
        assert temp_node is not None, "Successor should not be None"
        return temp_node

    def morris_postorder_traversal(self) -> list[int]:
        """
        Function for postorder traversal using morris postorder traversal.

        Algorithm :
        ------------
        First set current node as root node.

        while current node is not empty
            If the current node has no right child.
                push the current node to temp.
                point the current node to its left child

            else.
                find successor node of the current node.
                if successor left child points to current node,
                    remove the link of the left child of successor node.
                    point the current node to its left child.
                else,
                    push the current node to temp.
                    make the current node as the left child of the successor node.
                    point current node to its right child.

        Reverse the temp array to get postorder traversaol.

        Returns:
        --------
        A list of integers representing the postorder traversal.



        """
        postorder_traversal = []
        current_node = self.root

        while current_node:
            if current_node.right is None:
                postorder_traversal.append(current_node.value)
                current_node = current_node.left
            else:
                successor_node = self._successor(current_node)
                if successor_node.left == current_node:
                    successor_node.left = current_node
                    current_node = current_node.left
                else:
                    postorder_traversal.append(current_node.value)
                    successor_node.left = current_node
                    current_node = current_node.right
        return postorder_traversal[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
