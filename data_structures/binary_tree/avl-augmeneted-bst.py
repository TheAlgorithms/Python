#AVL Augmented Binary Search Tree 
class Tree:
    # Create a Node: value, left link and right link
    # Empty node has self.value, self.left, self.right = None
    # Leaf has self.value != None, and self.left, self.right point to empty node

    def __init__(self, initval=None):
        self.value = initval
        self.parent = None
        if self.value:
            self.left = Tree()
            self.right = Tree()
            self.left.parent = self
            self.right.parent = self
            self.height = 0
        else:
            self.left = None
            self.right = None
            self.height = -1
        return

    # To CHECK WHETHER A NODE IS EMPTY OR NOT
    def isempty(self):
        return self.value is None

    # Leaf nodes have both children empty
    def isleaf(self):
        return self.left.isempty() and self.right.isempty()

    # Convert a leaf node to an empty node
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        self.height = -1
        return

    # Copy right child values to current node which is used in delete method primarily
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        self.left.parent = self
        self.right.parent = self
        self.height = self.height - 1
        return

    # Check if value v occurs in tree
    def find(self, v):
        if self.isempty():
            return False

        if self.value == v:
            return True

        if v < self.value:
            return self.left.find(v)

        if v > self.value:
            return self.right.find(v)

    # Insert value v in tree
    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
            self.left.parent = self
            self.right.parent = self
            self.update_heights()
            self.rebalance()
            return

        elif v < self.value:
            return self.left.insert(v)

        elif v > self.value:
            return self.right.insert(v)
        else:
            return

    # Find maximum value in a nonempty tree
    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return self.right.maxval()

    # Find minimum value in a nonempty tree
    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            return self.left.minval()

    # Delete value v from tree
    def delete(self, v):
        if self.isempty():
            return

        if v < self.value:
            self.left.delete(v)
            return

        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            if self.parent is None:
                return
            self.parent.update_heights()
            self.parent.rebalance()
            return

    # Inorder traversal, Gives the values in Sorted order, Ascending
    def inorder(self):
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    def update_heights(self):
        self.height = max(self.left.height, self.right.height) + 1
        if self.parent is None:
            return
        return self.parent.update_heights()

    def diff_height(self):
        return self.left.height - self.right.height

    def unbalanced(self):
        return abs(self.diff_height()) > 1

    def ll_rotation(self):
        self.value, self.left.value = self.left.value, self.value
        var1 = self.right
        var2 = self.left
        # rotation operations
        self.left = var2.left
        self.right = var2
        self.right.left = var2.right
        self.right.right = var1
        # Fixing parent links
        self.left.parent, self.right.right.parent = self, self.right
        return

    def lr_rotation(self):
        self.value, self.left.right.value = self.left.right.value, self.value
        var1 = self.right
        var2 = self.left.right
        # rotation operations
        self.left.right = var2.left
        self.right = var2
        self.right.left = var2.right
        self.right.right = var1
        # Fixing parent links
        self.left.right.parent, self.right.parent, self.right.right.parent = self.left, self, self.right
        return

    def rr_rotation(self):
        self.value, self.right.value = self.right.value, self.value
        var1 = self.left
        var2 = self.right
        # rotation operations
        self.right = var2.right
        self.left = var2
        self.left.right = var2.left
        self.left.left = var1
        # Fixing parent links
        self.right.parent, self.left.left.parent = self, self.left
        return

    def rl_rotation(self):
        self.value, self.right.left.value = self.right.left.value, self.value
        var1 = self.left
        var2 = self.right.left
        # rotation operations
        self.right.left = var2.right
        self.left = var2
        self.left.right = var2.left
        self.left.left = var1
        # Fixing parent links
        self.right.left.parent, self.left.parent, self.left.left.parent = self.right, self, self.left
        return

    def rotation(self):
        var1 = self.diff_height()
        if var1 > 0:
            var2 = self.left.diff_height()
            if var2 >= 0:
                self.ll_rotation()  # LL Unbalanced rotation
                if var2 != 0:  # Fixing heights
                    self.height = self.height - 1
                    self.right.height = self.right.height - 1
            else:
                self.lr_rotation()  # LR Unbalanced rotation
                self.height = self.height - 1  # Fixing heights
                self.left.height = self.left.height - 1
        else:
            var2 = self.right.diff_height()
            if var2 <= 0:
                self.rr_rotation()  # RR Unbalanced rotation
                if var2 != 0:  # Fixing heights
                    self.height = self.height - 1
                    self.left.height = self.left.height - 1
            else:
                self.rl_rotation()  # RL Unbalanced rotation
                self.height = self.height - 1  # Fixing heights
                self.right.height = self.right.height - 1
        if self.parent is None:
            return
        self.parent.update_heights()
        return

    def rebalance(self):
        if self.unbalanced():
            self.rotation()
        if self.parent is None:
            return
        return self.parent.rebalance()

l = Tree()

for i in range(255):
    l.insert(i)
    print(l.value)
    print(l.height)
