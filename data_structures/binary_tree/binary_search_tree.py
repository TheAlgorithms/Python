#Binary_Search_Tree
from __future__ import annotations
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Self

@dataclass
class Node:
    value: int  # The value stored in the node
    left: Node | None = None  # Left child node
    right: Node | None = None  # Right child node
    parent: Node | None = None  # Parent node to facilitate easier deletion

    def __iter__(self) -> Iterator[int]:
        """Yield values in the node using in-order traversal."""
        yield from self.left or []  # Traverse left subtree
        yield self.value  # Yield current node value
        yield from self.right or []  # Traverse right subtree

    def __repr__(self) -> str:
        """Return a string representation of the node and its children."""
        from pprint import pformat
        if self.left is None and self.right is None:
            return str(self.value)  # If no children, return value
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    @property
    def is_right(self) -> bool:
        """Check if the node is a right child of its parent."""
        return bool(self.parent and self is self.parent.right)

@dataclass
class BinarySearchTree:
    root: Node | None = None  # The root node of the tree

    def __bool__(self) -> bool:
        """Return True if the tree has nodes, False otherwise."""
        return bool(self.root)

    def __iter__(self) -> Iterator[int]:
        """Yield values of the nodes using in-order traversal."""
        yield from self.root or []

    def __str__(self) -> str:
        """Return a string representation of the tree using in-order traversal."""
        return str(self.root)

    def __reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        """Reassign the children of the given node."""
        if new_children is not None:  # If there are new children
            new_children.parent = node.parent  # Set new child's parent
        if node.parent is not None:  # If the node has a parent
            if node.is_right:  # If it's a right child
                node.parent.right = new_children  # Assign new child to right
            else:
                node.parent.left = new_children  # Assign new child to left
        else:
            self.root = new_children  # If it's the root, set new root

    def empty(self) -> bool:
        """Check if the tree is empty."""
        return not self.root  # Return True if root is None

    def __insert(self, value) -> None:
        """Insert a new value into the Binary Search Tree."""
        new_node = Node(value)  # Create a new Node with the value
        if self.empty():  # If the tree is empty
            self.root = new_node  # Set it as the root
        else:  # If the tree is not empty
            parent_node = self.root  # Start from the root
            while True:  # Continue until we find a place for the new node
                if value < parent_node.value:  # Go left
                    if parent_node.left is None:  # If no left child
                        parent_node.left = new_node  # Insert the new node
                        break
                    else:
                        parent_node = parent_node.left  # Move to left child
                elif parent_node.right is None:  # Go right
                    parent_node.right = new_node  # Insert the new node
                    break
                else:
                    parent_node = parent_node.right  # Move to right child
            new_node.parent = parent_node  # Set parent for new node

    def insert(self, *values) -> Self:
        """Insert multiple values into the Binary Search Tree."""
        for value in values:  # Loop through all values provided
            self.__insert(value)  # Insert each value
        return self  # Return the instance for method chaining

    def search(self, value) -> Node | None:
        """Search for a node with a specific value."""
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root  # Start searching from the root
            # Continue searching until the value is found or the node is None
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right  # Navigate the tree
            return node  # Return the found node or None

    def get_max(self, node: Node | None = None) -> Node | None:
        """Find the node with the maximum value."""
        if node is None:  # If no node is provided, start from root
            if self.root is None:
                return None  # If tree is empty
            node = self.root

        # Go as far right as possible to find the maximum
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node  # Return the node with maximum value

    def get_min(self, node: Node | None = None) -> Node | None:
        """Find the node with the minimum value."""
        if node is None:  # If no node is provided, start from root
            node = self.root
        if self.root is None:
            return None  # If tree is empty
        # Go as far left as possible to find the minimum
        if not self.empty():
            while node.left is not None:
                node = node.left
        return node  # Return the node with minimum value

    def remove(self, value: int) -> None:
        """Remove a node with a specific value from the tree."""
        node = self.search(value)  # Search for the node to remove
        if node is None:
            msg = f"Value {value} not found"
            raise ValueError(msg)  # Raise an error if not found

        # Handle the three cases of node removal
        if node.left is None and node.right is None:  # No children
            self.__reassign_nodes(node, None)  # Remove the node
        elif node.left is None:  # Only right child
            self.__reassign_nodes(node, node.right)
        elif node.right is None:  # Only left child
            self.__reassign_nodes(node, node.left)
        else:  # Node with two children
            predecessor = self.get_max(node.left)  # Find predecessor
            self.remove(predecessor.value)  # Remove predecessor
            node.value = predecessor.value  # Replace value with predecessor's value

    def preorder_traverse(self, node: Node | None) -> Iterable:
        """Perform a pre-order traversal of the tree."""
        if node is not None:
            yield node  # Visit the current node
            yield from self.preorder_traverse(node.left)  # Traverse left subtree
            yield from self.preorder_traverse(node.right)  # Traverse right subtree

    def traversal_tree(self, traversal_function=None) -> Any:
        """Traverse the tree using a specified function."""
        if traversal_function is None:
            return self.preorder_traverse(self.root)  # Default to pre-order
        else:
            return traversal_function(self.root)  # Use the provided function

    def inorder(self, arr: list, node: Node | None) -> None:
        """Perform an in-order traversal and store values in arr."""
        if node:
            self.inorder(arr, node.left)  # Traverse left
            arr.append(node.value)  # Add current node's value
            self.inorder(arr, node.right)  # Traverse right

    def find_kth_smallest(self, k: int, node: Node) -> int:
        """Find the k-th smallest value in the tree."""
        # Initialize a list to hold the in-order traversal values
        arr = []
        self.inorder(arr, node)  # Fill the list with in-order traversal
        return arr[k - 1]  # Return the k-th smallest value (1-indexed)
