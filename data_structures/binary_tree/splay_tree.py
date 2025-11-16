"""
Splay Tree implementation (Self Adjusting BST)
Solves GitHub Issue #13760
For Hacktoberfest contribution. Please label 'hacktoberfest-accepted'.
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

    def __repr__(self):
        return f"Node({self.key})"


class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        if not y:
            return
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, x):
        y = x.right
        if not y:
            return
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _splay(self, x):
        while x and x.parent:
            p = x.parent
            g = p.parent
            # Zig step (p is root)
            if not g:
                if p.left == x:
                    self._right_rotate(p)
                else:
                    self._left_rotate(p)
            elif p.left == x and g.left == p:  # Zig-Zig
                if p.left == x and g.left == p:
                    self._right_rotate(g)
                    self._right_rotate(p)
                elif p.right == x and g.right == p:
                    self._left_rotate(g)
                    self._left_rotate(p)
                # Zig-Zag
                elif p.left == x and g.right == p:
                    self._right_rotate(p)
                    self._left_rotate(g)
                else:  # p.right == x and g.left == p
                    self._left_rotate(p)
                    self._right_rotate(g)

    def insert(self, key):
        z = self.root
        p = None
        while z:
            p = z
            z = z.left if key < z.key else z.right
        z = Node(key)
        z.parent = p
        if not p:
            self.root = z
        elif key < p.key:
            p.left = z
        else:
            p.right = z
        self._splay(z)

    def search(self, key):
        z = self.root
        last = None
        while z:
            last = z
            if key == z.key:
                self._splay(z)
                return z
            elif key < z.key:
                z = z.left
            else:
                z = z.right
        # splay the last accessed node (closest) if present
        if last:
            self._splay(last)
        return None

    def inorder(self, node=None, result=None):
        if result is None:
            result = []
        # if node is explicitly passed as None and tree is empty, return empty result
        if node is None:
            node = self.root
        if node is None:
            return result
        if node.left:
            self.inorder(node.left, result)
        result.append(node.key)
        if node.right:
            self.inorder(node.right, result)
        return result


# Example Usage / Test
if __name__ == "__main__":
    tree = SplayTree()
    # empty tree -> inorder should return []
    print(tree.inorder())  # []

    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
    print(tree.inorder())  # Output should be the inorder traversal of tree
    found = tree.search(30)
    print(f"Found: {found.key if found else None}")
