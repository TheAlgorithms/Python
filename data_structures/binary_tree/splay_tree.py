"""
Splay Tree implementation in Python.

A Splay Tree is a self-adjusting binary search tree where recently accessed
elements are moved closer to the root through rotations (splaying).
This improves access times for frequently used elements.

Author:yeshuawm999
Repository: https://github.com/TheAlgorithms/Python
"""


# class node
class Node:
    """A node in the Splay Tree."""

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key  # The value stored in the node
        self.parent = parent  # Pointer to the parent node
        self.left = left  # Pointer to the left child
        self.right = right  # Pointer to the right child


# Spary Tree class
class SplayTree:
    """A self-adjusting Binary Search Tree."""

    def __init__(self):
        self.root = None  # The root of the tree

    # --- Basic Rotation Operations ---

    def _rotate_left(self, x):
        """Perform a left rotation around node x (moving x down and right)."""
        y = x.right
        # 1. Update x's right child to be y's left child
        x.right = y.left
        if y.left:
            y.left.parent = x

        # 2. Update y's parent to be x's parent
        y.parent = x.parent
        if not x.parent:
            self.root = y  # y becomes the new root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # 3. Update y's left child to be x
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        """Perform a right rotation around node x (moving x down and left)."""
        y = x.left
        # 1. Update x's left child to be y's right child
        x.left = y.right
        if y.right:
            y.right.parent = x

        # 2. Update y's parent to be x's parent
        y.parent = x.parent
        if not x.parent:
            self.root = y  # y becomes the new new root
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        # 3. Update y's right child to be x
        y.right = x
        x.parent = y

    # --- Core Splay Operation ---

    def _splay(self, x):
        """Moves node x to the root of the tree using a sequence of rotations."""
        while x.parent:
            parent = x.parent
            grandparent = parent.parent

            if not grandparent:
                # Zig Case (x is a child of the root)
                # One single rotation (Right if x is left child, Left if x is right child)
                if x == parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)

            else:
                # Two rotations are performed: Zig-Zig or Zig-Zag

                # Case 1: Zig-Zig (x, parent, and grandparent are all on one side)
                if x == parent.left and parent == grandparent.left:
                    # x and parent are both left children (Left-Left)
                    self._rotate_right(grandparent)  # Rotate grandparent down
                    self._rotate_right(parent)  # Rotate parent down
                elif x == parent.right and parent == grandparent.right:
                    # x and parent are both right children (Right-Right)
                    self._rotate_left(grandparent)  # Rotate grandparent down
                    self._rotate_left(parent)  # Rotate parent down

                # Case 2: Zig-Zag (x is on one side, parent is on the other)
                elif x == parent.left and parent == grandparent.right:
                    # x is left child, parent is right child
                    self._rotate_right(parent)  # Rotate parent first
                    self._rotate_left(grandparent)  # Rotate grandparent next
                else:  # x == parent.right and parent == grandparent.left
                    # x is right child, parent is left child
                    self._rotate_left(parent)  # Rotate parent first
                    self._rotate_right(grandparent)  # Rotate grandparent next

    # --- Example Search Method (Uses splay) ---

    def search(self, key):
        """Searches for a key. If found, splays it to the root."""
        current = self.root
        found_node = None
        while current:
            if key == current.key:
                found_node = current
                break
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        if found_node:
            self._splay(found_node)  # Node is brought to the root
            return True
        return False


if __name__ == "__main__":
    tree = SplayTree()
    # Manually create nodes to demonstrate splay
    tree.root = Node(10)
    tree.root.left = Node(5, parent=tree.root)
    tree.root.right = Node(15, parent=tree.root)

    print("Before search:", tree.root.key)
    found = tree.search(5)
    print("Found:", found)
    print("After splay, new root:", tree.root.key)
