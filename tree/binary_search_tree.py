"""
Binary Search Tree Implementation

This implementation provides a binary search tree (BST) with basic operations
including insertion, search, deletion, and in-order traversal. Each operation
leverages recursive helper functions.

Binary Search Tree Implementation with Doctest Examples
For more information on binary search trees, please see:
https://en.wikipedia.org/wiki/Binary_search_tree

To run the doctests:
    python -m doctest -v binary_search_tree.py
"""


class BSTNode:
    """
    A node in the binary search tree.

    Attributes
    ----------
    key : int
        The key value stored in the node.
    left : BSTNode or None
        The left child node.
    right : BSTNode or None
        The right child node.
    """

    def __init__(self, key: int) -> None:
        """
        Initializes a new BST node.

        Parameters
        ----------
        key : int
            The key value for the new node.
        """
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) class that supports basic operations such as
    insertion, search, deletion, and in-order traversal.

    For details on BSTs, see:
    https://en.wikipedia.org/wiki/Binary_search_tree
    """

    def __init__(self) -> None:
        """
        Initializes an empty Binary Search Tree.
        """
        self.root = None

    def insert(self, key: int) -> None:
        """
        Inserts a new key into the BST.

        Parameters
        ----------
        key : int
            The key to be inserted into the BST.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.inorder_traversal()
        [5, 10, 15]
        """
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: BSTNode, key: int) -> None:
        """
        Recursively inserts a new key into the subtree rooted at the given node.

        Parameters
        ----------
        node : BSTNode
            The current node in the BST.
        key : int
            The key to be inserted.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.root = BSTNode(10)
        >>> bst._insert_recursive(bst.root, 5)
        >>> bst._insert_recursive(bst.root, 15)
        >>> bst.inorder_traversal()
        [5, 10, 15]
        """
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self) -> list:
        """
        Performs an in-order traversal of the BST and returns the keys in sorted order.

        Returns
        -------
        list
            A list of keys in increasing order.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.inorder_traversal()  # For an empty BST.
        []
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.inorder_traversal()
        [5, 10, 15]
        >>> bst.insert(7)
        >>> bst.inorder_traversal()
        [5, 7, 10, 15]
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: BSTNode, result: list) -> None:
        """
        Helper function for recursively performing in-order traversal by
        accumulating the keys in the provided list.

        Parameters
        ----------
        node : BSTNode or None
            The current node being visited.
        result : list
            The list to accumulate the keys.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> # Manually build a simple BST.
        >>> bst.root = BSTNode(20)
        >>> bst.root.left = BSTNode(10)
        >>> bst.root.right = BSTNode(30)
        >>> result = []
        >>> bst._inorder_recursive(bst.root, result)
        >>> result
        [10, 20, 30]
        >>> # If the subtree is empty, the result remains unchanged.
        >>> result = [1, 2, 3]
        >>> bst._inorder_recursive(None, result)
        >>> result
        [1, 2, 3]
        """
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def search(self, key: int):
        """
        Searches for a given key in the BST using a recursive approach.

        Parameters
        ----------
        key : int
            The key to search for.

        Returns
        -------
        BSTNode or None
            The node containing the key if found; otherwise, None.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> node = bst.search(5)
        >>> node.key
        5
        >>> bst.search(20) is None
        True
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: BSTNode, key: int):
        """
        Helper function to recursively search for a key in the BST.

        Parameters
        ----------
        node : BSTNode or None
            The current node in the BST.
        key : int
            The key to search for.

        Returns
        -------
        BSTNode or None
            The node containing the key if found; otherwise, None.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.root = BSTNode(10)
        >>> bst.root.left = BSTNode(5)
        >>> bst._search_recursive(bst.root, 5).key
        5
        >>> bst._search_recursive(bst.root, 20) is None
        True
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def delete(self, key: int) -> None:
        """
        Deletes the node with the specified key from the BST if it exists.

        Parameters
        ----------
        key : int
            The key to be deleted.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> for key in [10, 5, 15, 2, 7]:
        ...     bst.insert(key)
        >>> bst.inorder_traversal()
        [2, 5, 7, 10, 15]
        >>> bst.delete(5)
        >>> bst.inorder_traversal()
        [2, 7, 10, 15]
        >>> bst.delete(20)  # Deleting a non-existent key leaves the tree unchanged.
        >>> bst.inorder_traversal()
        [2, 7, 10, 15]
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: BSTNode, key: int):
        """
        Recursively deletes the node with the specified key from the subtree.

        Parameters
        ----------
        node : BSTNode or None
            The current node in the BST.
        key : int
            The key to be deleted.

        Returns
        -------
        BSTNode or None
            The new root of the subtree after deletion.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.root = BSTNode(10)
        >>> bst.root.left = BSTNode(5)
        >>> bst.root.right = BSTNode(15)
        >>> # Deleting a node in this simple tree; the new root will be unchanged as 10.
        >>> bst._delete_recursive(bst.root, 5).key
        10
        """
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child.
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the in-order successor.
            temp = self._find_min(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        return node

    def _find_min(self, node: BSTNode) -> BSTNode:
        """
        Finds the node with the minimum key in the subtree.

        Parameters
        ----------
        node : BSTNode
            The root of the subtree from which to find the minimum key.

        Returns
        -------
        BSTNode
            The node with the smallest key.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.root = BSTNode(10)
        >>> bst.root.left = BSTNode(5)
        >>> bst.root.right = BSTNode(15)
        >>> bst._find_min(bst.root).key
        5
        >>> bst.root.left.left = BSTNode(2)
        >>> bst._find_min(bst.root).key
        2
        """
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    import doctest

    doctest.testmod()
