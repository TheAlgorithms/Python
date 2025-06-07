from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    """Node of a Binary Search Tree (BST) for sorting."""
    val: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        """In-order traversal generator for BST."""
        # Traverse left subtree first (smaller values)
        if self.left:
            yield from self.left
            
        # Current node value
        yield self.val
        
        # Traverse right subtree last (larger values)
        if self.right:
            yield from self.right

    def insert(self, val: int) -> None:
        """Insert value into BST while maintaining sort order."""
        # Values <= current go to left subtree
        if val <= self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        # Values > current go to right subtree
        elif self.right is None:
            self.right = Node(val)
        else:
            self.right.insert(val)


def tree_sort(arr: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    """
    Sort sequence using Binary Search Tree (BST) traversal.
    
    Args:
        arr: Input sequence (list or tuple of integers)
    
    Returns:
        Tuple of sorted integers
    
    Examples:
        >>> tree_sort([])
        ()
        >>> tree_sort((1,))
        (1,)
        >>> tree_sort((1, 2))
        (1, 2)
        >>> tree_sort([5, 2, 7])
        (2, 5, 7)
        >>> tree_sort((5, -4, 9, 2, 7))
        (-4, 2, 5, 7, 9)
        >>> tree_sort([5, 6, 1, -1, 4, 37, 2, 7])
        (-1, 1, 2, 4, 5, 6, 7, 37)
        >>> tree_sort([5, 2, 7, 5])  # Test duplicate handling
        (2, 5, 5, 7)
    """
    # Handle empty input immediately
    if not arr:
        return ()
    
    # Convert to list for uniform processing
    items = list(arr)
    
    # Initialize BST root with first element
    root = Node(items[0])
    
    # Insert remaining items into BST
    for item in items[1:]:
        root.insert(item)
    
    # Convert BST traversal to sorted tuple
    return tuple(root)
