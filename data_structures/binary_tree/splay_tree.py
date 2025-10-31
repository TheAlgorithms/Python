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

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
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
        while x.parent:
            if not x.parent.parent:
                if x.parent.left == x:
                    self._right_rotate(x.parent)
                else:
                    self._left_rotate(x.parent)
            else:
                if x.parent.left == x and x.parent.parent.left == x.parent:
                    self._right_rotate(x.parent.parent)
                    self._right_rotate(x.parent)
                elif x.parent.right == x and x.parent.parent.right == x.parent:
                    self._left_rotate(x.parent.parent)
                    self._left_rotate(x.parent)
                elif x.parent.left == x and x.parent.parent.right == x.parent:
                    self._right_rotate(x.parent)
                    self._left_rotate(x.parent)
                else:
                    self._left_rotate(x.parent)
                    self._right_rotate(x.parent)

    def insert(self, key):
        z = self.root
        p = None
        while z:
            p = z
            if key < z.key:
                z = z.left
            else:
                z = z.right
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
        while z:
            if key == z.key:
                self._splay(z)
                return z
            elif key < z.key:
                if not z.left:
                    self._splay(z)
                    return None
                z = z.left
            else:
                if not z.right:
                    self._splay(z)
                    return None
                z = z.right
        return None

    def inorder(self, node=None, result=None):
        if result is None:
            result = []
        node = node or self.root
        if node.left:
            self.inorder(node.left, result)
        result.append(node.key)
        if node.right:
            self.inorder(node.right, result)
        return result

# Example Usage / Test
if __name__ == "__main__":
    tree = SplayTree()
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
    print(tree.inorder())   # Output should be the inorder traversal of tree
    found = tree.search(30)
    print(f"Found: {found.key if found else None}")
