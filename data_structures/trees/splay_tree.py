# the_algorithms/trees/splay_tree.py

class Node:
    """A single node in the Splay Tree."""
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class SplayTree:
    """
    A self-adjusting Binary Search Tree (BST) that uses the splay operation
    to move the most recently accessed node to the root of the tree.
    """
    def __init__(self):
        self.root = None

    def _rotate(self, x: Node):
        """Performs a single rotation (left or right) around node x."""
        p = x.parent  # Parent of x
        g = p.parent  # Grandparent of x

        if p.left == x:  # Right rotation (x is left child)
            p.left = x.right
            if x.right:
                x.right.parent = p
            x.right = p
        else:  # Left rotation (x is right child)
            p.right = x.left
            if x.left:
                x.left.parent = p
            x.left = p

        # Update parent pointers
        p.parent = x
        x.parent = g

        # Update grandparent pointer to x
        if g:
            if g.left == p:
                g.left = x
            else:
                g.right = x
        else:
            self.root = x # x is the new root

    def _splay(self, x: Node):
        """Moves node x to the root of the tree using zig, zig-zig, or zig-zag operations."""
        while x.parent:
            p = x.parent
            g = p.parent

            if not g:
                # Zig operation (p is the root)
                self._rotate(x)
            elif (p.left == x and g.left == p) or (p.right == x and g.right == p):
                # Zig-zig operation (x, p, g are all on the left or all on the right)
                self._rotate(p)  # Rotate p first
                self._rotate(x)  # Then rotate x
            else:
                # Zig-zag operation (x is left/right and p is right/left)
                self._rotate(x)  # Rotate x first
                self._rotate(x)  # Then rotate x again

    def search(self, key):
        """
        Searches for a node with the given key. If found, the node is splayed to the root.
        If not found, the last accessed node (parent of where the key would be) is splayed.
        Returns the node if found, otherwise None.
        """
        curr = self.root
        last = None # Keeps track of the last node accessed

        while curr:
            last = curr
            if key == curr.key:
                self._splay(curr)
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if last:
            self._splay(last) # Splay the last accessed node if key was not found
        return None

    def insert(self, key):
        """Inserts a new key and then splays it to the root."""
        if not self.root:
            self.root = Node(key)
            return

        # Regular BST insertion
        curr = self.root
        parent = None
        while curr:
            parent = curr
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else: # Key already exists, splay it and return (or update value)
                self._splay(curr)
                return

        new_node = Node(key, parent=parent)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._splay(new_node) 
