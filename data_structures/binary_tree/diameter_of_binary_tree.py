"""
The diameter/width of a tree is defined as the number of nodes on the longest path
between two end nodes.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def depth(self) -> int:
        """
        >>> root = Node(1)
        >>> root.depth()
        1
        >>> root.left = Node(2)
        >>> root.depth()
        2
        >>> root.left.depth()
        1
        >>> root.right = Node(3)
        >>> root.depth()
        2
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def diameter(self) -> int:
        """
        >>> root = Node(1)
        >>> root.diameter()
        1
        >>> root.left = Node(2)
        >>> root.diameter()
        2
        >>> root.left.diameter()
        1
        >>> root.right = Node(3)
        >>> root.diameter()
        3
        """
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth + right_depth + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    r"""
    Constructed binary tree is
        1
       / \
      2	  3
     / \
    4	 5
    """
    print(f"{root.diameter() = }")  # 4
    print(f"{root.left.diameter() = }")  # 3
    print(f"{root.right.diameter() = }")  # 1
