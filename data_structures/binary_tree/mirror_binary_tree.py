from __future__ import annotations
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    """A Node has a value and pointers to its left and right Nodes."""

    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def mirror(self, inplace: bool = True) -> Node:
        """
        Mirror the binary tree rooted at this node by swapping left and right children.

        Args:
            inplace (bool): If True, mirror the tree in place. If False, create a new mirrored tree.

        Returns:
            Node: The mirrored tree root node.
        """
        if inplace:
            self.left, self.right = self.right, self.left
        else:
            mirrored_node = Node(self.value)
            mirrored_node.left = self.right.mirror(False) if self.right else None
            mirrored_node.right = self.left.mirror(False) if self.left else None
            return mirrored_node

def make_tree_seven() -> Node:
    """Return a binary tree with 7 nodes."""
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    return tree

def make_tree_nine() -> Node:
    """Return a binary tree with 9 nodes."""
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.right = Node(6)
    tree.left.left.left = Node(7)
    tree.left.left.right = Node(8)
    tree.left.right.right = Node(9)
    return tree

def main() -> None:
    """Mirror binary trees and print the results."""
    trees = {
        "zero": Node(0),
        "seven": make_tree_seven(),
        "nine": make_tree_nine(),
    }
    for name, tree in trees.items():
        print(f"The {name} tree: {list(tree)}")
        mirrored_tree = tree.mirror(False)
        print(f"Mirror of {name} tree: {list(mirrored_tree)}")

if __name__ == "__main__":
    main()
