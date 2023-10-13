from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Optional[Node] = None  # noqa: UP007
        self.right: Optional[Node] = None  # noqa: UP007

    def display(self, node: Optional[Node] = None) -> None:  # noqa: UP007
        if node is None:
            node = self
        if node:
            self.display(node.left)
            print(node.data)
            self.display(node.right)


class BinaryTree:
    def __init__(self, root: Optional[Node] = None) -> None:  # noqa: UP007
        self.root: Optional[Node] = root  # noqa: UP007

    def display(self, node: Optional[Node] = None) -> None:  # noqa: UP007
        """
        Prints the tree in order traversal

        Examples:
        >>> tree = BinaryTree(Node(1))
        >>> tree.display()
        1

        >>> tree.root.left = Node(2)
        >>> tree.root.right = Node(3)
        >>> tree.display()
        2
        1
        3
        """
        if node is None:
            node = self.root
        if node:
            self.display(node.left)
            print(node.data)
            self.display(node.right)

    def depth(self) -> int:
        """
        Returns the depth of the tree

        Examples:

        >>> tree = BinaryTree(Node(1))
        >>> tree.depth()
        1

        >>> tree.root.left = Node(2)
        >>> tree.depth()
        2

        >>> tree.root.right = Node(3)
        >>> tree.depth()
        2
        """
        if self.root is None:
            return 0
        else:
            return self._depth(self.root)

    def _depth(self, node: Optional[Node]) -> int:  # noqa: UP007
        if node is None:
            return 0
        else:
            return 1 + max(self._depth(node.left), self._depth(node.right))

    def is_full(self) -> bool:
        """
        Returns True if the tree is full

        Examples:

        >>> tree = BinaryTree(Node(1))
        >>> tree.is_full()
        True

        >>> tree.root.left = Node(2)
        >>> tree.is_full()
        False

        >>> tree.root.right = Node(3)
        >>> tree.is_full()
        True
        """
        if self.root is None:
            return True
        else:
            return self._is_full(self.root)

    def _is_full(self, node: Node) -> bool:
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full(node.left) and self._is_full(node.right)
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
