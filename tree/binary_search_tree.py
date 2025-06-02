"""
Binary Search Tree Implementation

This implementation provides a binary search tree (BST) with basic operations
including insertion, search, deletion, and in-order traversal. Each operation
leverages recursive helper functions.
"""


class BSTNode:
    """
    A node in a binary search tree.

    Attributes
    ----------
    key : int
        The key value stored in the node.
    left : BSTNode or None
        The left child node.
    right : BSTNode or None
        The right child node.
    """

    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) class that supports basic operations such as
    insertion, search, deletion, and in-order traversal.

    Methods
    -------
    insert(key: int) -> None
        Inserts a new key into the BST.
    search(key: int) -> BSTNode or None
        Searches for a key in the BST and returns the node if found.
    delete(key: int) -> None
        Deletes a key from the BST if it exists.
    inorder_traversal() -> list
        Returns a list of keys representing the in-order traversal of the BST.
    """

    def __init__(self):
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
        """
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: BSTNode, key: int) -> None:
        """
        Recursively inserts the new key into the subtree rooted at the given node.

        Parameters
        ----------
        node : BSTNode
            The current node in the BST.
        key : int
            The key to be inserted.
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

    def search(self, key: int) -> BSTNode:
        """
        Searches for a key in the BST.

        Parameters
        ----------
        key : int
            The key to search for.

        Returns
        -------
        BSTNode or None
            The node containing the key if found, or None otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: BSTNode, key: int) -> BSTNode:
        """
        Recursively searches for a key in the tree.

        Parameters
        ----------
        node : BSTNode or None
            The current node in the BST.
        key : int
            The key to search for.

        Returns
        -------
        BSTNode or None
            The node containing the key if found, otherwise None.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def delete(self, key: int) -> None:
        """
        Deletes a key from the BST if it exists.

        Parameters
        ----------
        key : int
            The key to be deleted.
        """
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: BSTNode, key: int) -> BSTNode:
        """
        Recursively deletes a key from the subtree rooted at the given node.

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
        """
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node found; handle deletions for nodes with 0 or 1 child.
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: get the inorder successor (smallest in the right subtree)
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
            The root of the subtree.

        Returns
        -------
        BSTNode
            The node with the smallest key in the subtree.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self) -> list:
        """
        Performs an in-order traversal of the BST.

        Returns
        -------
        list
            A list of keys in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: BSTNode, result: list) -> None:
        """
        Recursively performs an in-order traversal of the BST and appends keys to the result list.

        Parameters
        ----------
        node : BSTNode or None
            The current node in the BST.
        result : list
            The list that accumulates the keys.
        """
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    """
    Testing the Binary Search Tree (BST) implementation.

    Example:
    --------
    1. Insert nodes with keys: [50, 30, 70, 20, 40, 60, 80]
    2. Display the in-order traversal after insertion.
    3. Search for a key (e.g., 40).
    4. Delete a key (e.g., 30) and display the new in-order traversal.
    """
    bst = BinarySearchTree()

    # Insert nodes into the BST
    nodes_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for key in nodes_to_insert:
        bst.insert(key)
    print("In-order traversal after insertion:", bst.inorder_traversal())

    # Search for a key in the BST
    search_key = 40
    result = bst.search(search_key)
    if result:
        print(f"Node with key {search_key} found.")
    else:
        print(f"Node with key {search_key} not found.")

    # Delete a node from the BST
    bst.delete(30)
    print("In-order traversal after deleting 30:", bst.inorder_traversal())
