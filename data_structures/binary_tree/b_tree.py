"""
B-Tree Implementation

A B-Tree is a self-balancing tree data structure that maintains sorted data and allows
searches, sequential access, insertions, and deletions in logarithmic time.

B-Trees are commonly used in databases and file systems.

Reference: https://en.wikipedia.org/wiki/B-tree
Time Complexity:
    - Search: O(log n)
    - Insert: O(log n)
    - Delete: O(log n)
"""

from __future__ import annotations


class BTreeNode:
    """
    A node in the B-Tree.

    Attributes:
        keys: List of keys stored in the node
        children: List of child nodes
        is_leaf: Boolean indicating if this is a leaf node
    """

    def __init__(self, is_leaf: bool = True) -> None:
        self.keys: list[int] = []
        self.children: list[BTreeNode] = []
        self.is_leaf = is_leaf

    def split(self, parent: BTreeNode, index: int) -> None:
        """
        Split this node and move the median key up to the parent.

        Args:
            parent: The parent node
            index: The index in parent's children where this node is located
        """
        new_node = BTreeNode(is_leaf=self.is_leaf)
        mid_index = len(self.keys) // 2
        median_key = self.keys[mid_index]

        new_node.keys = self.keys[mid_index + 1 :]
        self.keys = self.keys[:mid_index]

        if not self.is_leaf:
            new_node.children = self.children[mid_index + 1 :]
            self.children = self.children[: mid_index + 1]

        parent.keys.insert(index, median_key)
        parent.children.insert(index + 1, new_node)


class BTree:
    """
    B-Tree data structure.

    A B-Tree of order m has the following properties:
    - Every node has at most m children
    - Every non-leaf node (except root) has at least ⌈m/2⌉ children
    - The root has at least 2 children if it is not a leaf
    - All leaves appear on the same level
    - A non-leaf node with k children contains k-1 keys

    Examples:
    >>> btree = BTree(order=3)
    >>> btree.insert(10)
    >>> btree.insert(20)
    >>> btree.insert(5)
    >>> btree.insert(6)
    >>> btree.insert(12)
    >>> btree.insert(30)
    >>> btree.insert(7)
    >>> btree.insert(17)
    >>> btree.search(6)
    True
    >>> btree.search(15)
    False
    >>> btree.search(12)
    True
    >>> btree.search(100)
    False
    """

    def __init__(self, order: int = 3) -> None:
        """
        Initialize a B-Tree.

        Args:
            order: The maximum number of children a node can have (must be >= 3)

        Raises:
            ValueError: If order is less than 3
        """
        if order < 3:
            msg = "Order must be at least 3"
            raise ValueError(msg)

        self.order = order
        self.min_keys = (order + 1) // 2 - 1
        self.max_keys = order - 1
        self.root = BTreeNode()

    def search(self, key: int, node: BTreeNode | None = None) -> bool:
        """
        Search for a key in the B-Tree.

        Args:
            key: The key to search for
            node: The node to start searching from (defaults to root)

        Returns:
            True if the key exists, False otherwise

        Time Complexity: O(log n)

        >>> btree = BTree(order=3)
        >>> btree.insert(50)
        >>> btree.search(50)
        True
        >>> btree.search(25)
        False
        """
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.is_leaf:
            return False

        return self.search(key, node.children[i])

    def insert(self, key: int) -> None:
        """
        Insert a key into the B-Tree.

        Args:
            key: The key to insert

        Time Complexity: O(log n)

        >>> btree = BTree(order=3)
        >>> btree.insert(10)
        >>> btree.insert(20)
        >>> btree.insert(30)
        >>> btree.search(20)
        True
        """
        if len(self.root.keys) >= self.max_keys:
            new_root = BTreeNode(is_leaf=False)
            new_root.children.append(self.root)
            self.root.split(new_root, 0)
            self.root = new_root

        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node: BTreeNode, key: int) -> None:
        """
        Insert a key into a node that is not full.

        Args:
            node: The node to insert into
            key: The key to insert
        """
        i = len(node.keys) - 1

        if node.is_leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) >= self.max_keys:
                node.children[i].split(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key)

    def traverse(self, node: BTreeNode | None = None) -> list[int]:
        """
        Traverse the B-Tree in sorted order.

        Args:
            node: The node to start traversal from (defaults to root)

        Returns:
            List of all keys in sorted order

        >>> btree = BTree(order=3)
        >>> for i in [10, 20, 5, 6, 12, 30, 7, 17]:
        ...     btree.insert(i)
        >>> btree.traverse()
        [5, 6, 7, 10, 12, 17, 20, 30]
        """
        if node is None:
            node = self.root

        result: list[int] = []

        for i in range(len(node.keys)):
            if not node.is_leaf and i < len(node.children):
                result.extend(self.traverse(node.children[i]))
            result.append(node.keys[i])

        if not node.is_leaf and len(node.children) > len(node.keys):
            result.extend(self.traverse(node.children[len(node.keys)]))

        return result

    def get_height(self, node: BTreeNode | None = None) -> int:
        """
        Get the height of the B-Tree.

        Args:
            node: The node to start from (defaults to root)

        Returns:
            The height of the tree

        >>> btree = BTree(order=3)
        >>> btree.get_height()
        0
        >>> btree.insert(10)
        >>> btree.get_height()
        0
        >>> for i in range(20):
        ...     btree.insert(i)
        >>> btree.get_height() > 0
        True
        """
        if node is None:
            node = self.root

        if node.is_leaf:
            return 0

        return 1 + self.get_height(node.children[0])

    def __str__(self) -> str:
        """
        String representation of the B-Tree.

        Returns:
            String showing all keys in sorted order
        """
        return f"BTree(order={self.order}, keys={self.traverse()})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    btree = BTree(order=3)
    keys = [10, 20, 5, 6, 12, 30, 7, 17, 3, 8, 15, 25, 35, 40]

    print("Inserting keys:", keys)
    for key in keys:
        btree.insert(key)

    print("\nB-Tree traversal (sorted):", btree.traverse())
    print("B-Tree height:", btree.get_height())
    print("\nSearching for 12:", btree.search(12))
    print("Searching for 100:", btree.search(100))
