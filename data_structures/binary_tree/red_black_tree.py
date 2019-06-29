class RedBlackTree:
    """
    A Red-Black tree, which is a self-balancing BST (binary search
    tree).

    This tree has similar performance to AVL trees, but the balancing is
    less strict, so it will perform faster for writing/deleting nodes
    and slower for reading in the average case, though, because they're
    both balanced binary search trees, both will get the same asymptotic
    perfomance.

    To read more about them, https://en.wikipedia.org/wiki/Red–black_tree

    Unless otherwise specified, all asymptotic runtimes are specified in
    terms of the size of the tree.
    """
    def __init__(self, label=None, color=0, parent=None, left=None, right=None):
        """Initialize a new Red-Black Tree node with the given values:
            label: The value associated with this node
            color: 0 if black, 1 if red
            parent: The parent to this node
            left: This node's left child
            right: This node's right child
        """
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def rotate_left(self):
        """Rotate the subtree rooted at this node to the left and
        returns the new root to this subtree.

        Perfoming one rotation can be done in O(1).
        """
        parent = self.parent
        right = self.right
        self.right = right.left
        if self.right:
            self.right.parent = self
        self.parent = right
        right.left = self
        if parent is not None:
            if parent.left is self:
                parent.left = right
            else:
                parent.right = right
        right.parent = parent
        return right
    
    def rotate_right(self):
        """Rotate the subtree rooted at this node to the right and
        returns the new root to this subtree.

        Performing one rotation can be done in O(1).
        """
        parent = self.parent
        left = self.left
        self.left = left.right
        if self.left:
            self.left.parent = self
        self.parent = left
        left.right = self
        if parent is not None:
            if parent.right is self:
                parent.right = left
            else:
                parent.left = left
        left.parent = parent
        return left

    def insert(self, label):
        """Inserts label into the subtree rooted at self, performs any
        rotations necessary to maintain balance, and then returns the
        new root to this subtree (likely self).

        This is guaranteed to run in O(log(n)) time.
        """
        if self.label == None:
            # Only possible with an empty tree
            self.label = label
            return self
        if self.label == label:
            return self
        elif self.label > label:
            if self.left:
                self.left.insert(label)
            else:
                self.left = RedBlackTree(label, 1, self)
                self.left._insert_repair()
        else:
            if self.right:
                self.right.insert(label)
            else:
                self.right = RedBlackTree(label, 1, self)
                self.right._insert_repair()
        return self.parent or self

    def _insert_repair(self):
        """Repair the coloring from inserting into a tree."""
        if self.parent is None:
            # This node is the root, so it just needs to be black
            self.color = 0
        elif color(self.parent) == 0:
            # If the parent is black, then it just needs to be red
            self.color = 1
        else:
            uncle = self.parent.sibling
            if color(uncle) == 0:
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    self.right._insert_repair()
                elif self.is_right() and self.parent.is_left():
                    self.parent.rotate_left()
                    self.left._insert_repair()
                elif self.is_left():
                    self.grandparent.rotate_right()
                    self.parent.color = 0
                    self.parent.right.color = 1
                else:
                    self.grandparent.rotate_left()
                    self.parent.color = 0
                    self.parent.left.color = 1
            else:
                self.parent.color = 0
                uncle.color = 0
                self.grandparent.color = 1
                self.grandparent._insert_repair()

    def check_color_properties(self):
        """Check the coloring of the tree, and return True iff the tree
        is colored in a way which matches these five properties:
        (wording stolen from wikipedia article)
         1. Each node is either red or black.
         2. The root node is black.
         3. All leaves are black.
         4. If a node is red, then both its children are black.
         5. Every path from any node to all of its descendent NIL nodes
            has the same number of black nodes.

        This function runs in O(n) time, because properties 4 and 5 take
        that long to check.
        """
        # I assume property 1 to hold because there is nothing that can
        # make the color be anything other than 0 or 1.

        # Property 2
        if self.color:
            # The root was red
            return False;

        # Property 3 does not need to be checked, because None is assumed
        # to be black and is all the leaves.

        # Property 4
        if not self.check_coloring():
            return False

        # Property 5
        if black_height(self) is None:
            return False

    def check_coloring(self):
        """A helper function to recursively check Property 4 of a
        Red-Black Tree. See check_color_properties for more info.
        """
        if self.color == 1:
            if color(self.left) == 1 or color(self.right) == 1:
                return False
        if self.left and not check_coloring(self.left):
            return False
        if self.right and not check_coloring(self.right):
            return False
        return True

    def black_height(self):
        """Returns the number of black nodes from this node to the
        leaves of the tree, or None if there isn't one such value (the
        tree is color incorrectly).
        """
        if self is None:
            # If we're already at a leaf, there is no path
            return 1
        left = RedBlackTree.black_height(self.left)
        right = RedBlackTree.black_height(self.right)
        if left is None or right is None:
            # There are issues with coloring below children nodes
            return None
        if left != right:
            # The two children have unequal depths
            return None
        # Return the black depth of children, plus one if this node is
        # black
        return left + (1-self.color)

    def __contains__(self, label):
        """Search through the tree for label, returning True iff it is
        found somewhere in the tree.
        
        Guaranteed to run in O(log(n)) time.
        """
        return self.search(label) is not None

    def search(self, label):
        """Search through the tree for label, returning its node if
        it's found, and None otherwise.

        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self
        elif label > self.label:
            if self.right is None:
                return None
            else:
                return self.right.search(label)
        else:
            if self.left is None:
                return None
            else:
                return self.left.search(label)

    def floor(self, label):
        """Returns the largest element in this tree which is at most label.
        
        This method is guaranteed to run in O(log(n)) time."""
        if self.label == label:
            return self.label
        elif self.label > label:
            if self.left:
                return self.left.floor(label)
            else:
                return None
        else:
            if self.right:
                attempt = self.right.floor(label)
                if attempt is not None:
                    return attempt
            return self.label

    def ceil(self, label):
        """Returns the smallest element in this tree which is at least label.
        
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self.label
        elif self.label < label:
            if self.right:
                return self.right.ceil(label)
            else:
                return None
        else:
            if self.left:
                attempt = self.left.ceil(label)
                if attempt is not None:
                    return attempt
            return self.label

    def get_max(self):
        """Returns the largest element in this tree.

        This method is guaranteed to run in O(log(n)) time.
        """
        if self.right:
            # Go as far right as possible
            return self.right.get_max()
        else:
            return self.label

    def get_min(self):
        """Returns the smallest element in this tree.

        This method is guaranteed to run in O(log(n)) time.
        """
        if self.left:
            # Go as far left as possible
            return self.left.get_min()
        else:
            return self.label

    @property
    def grandparent(self):
        """Get the current node's grandparent, or None if it doesn't exist."""
        if self.parent is None:
            return None
        else:
            return self.parent.parent
    
    @property
    def sibling(self):
        """Get the current node's sibling, or None if it doesn't exist."""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def is_left(self):
        """Returns true iff this node is the left child of its parent."""
        return self.parent and self.parent.left is self

    def is_right(self):
        """Returns true iff this node is the right child of its parent."""
        return self.parent and self.parent.right is self

    def __bool__(self):
        return True

    def __len__(self):
        """
        Return the number of nodes in this tree.
        """
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        return ln

    def preorder_traverse(self):
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()

    def inorder_traverse(self):
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()


    def postorder_traverse(self):
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label

    def __repr__(self):
        from pprint import pformat
        if self.left is None and self.right is None:
            return "'%s %s'" % (self.label, (self.color and 'red') or 'blk')
        return pformat({'%s %s' % (self.label, (self.color and 'red') or 'blk'):
                            (self.left, self.right)},
                       indent=1)

    def __eq__(self, other):
        """Test if two trees are equal."""
        if self.label == other.label:
            return self.left == other.left and self.right == other.right
        else:
            return False

def color(node):
    """Returns the color of a node, allowing for None leaves."""
    if node is None:
        return 0
    else:
        return node.color

"""
Code for testing the various functions of the red-black tree.
"""

def test_rotations():
    """Test that the rotate_left and rotate_right functions work."""
    # Make a tree to test on
    tree = RedBlackTree(0)
    tree.left = RedBlackTree(-10, parent=tree)
    tree.right = RedBlackTree(10, parent=tree)
    tree.left.left = RedBlackTree(-20, parent=tree.left)
    tree.left.right = RedBlackTree(-5, parent=tree.left)
    tree.right.left = RedBlackTree(5, parent=tree.right)
    tree.right.right = RedBlackTree(20, parent=tree.right)
    # Make the right rotation
    left_rot = RedBlackTree(10)
    left_rot.left = RedBlackTree(0, parent=left_rot)
    left_rot.left.left = RedBlackTree(-10, parent=left_rot.left)
    left_rot.left.right = RedBlackTree(5, parent=left_rot.left)
    left_rot.left.left.left = RedBlackTree(-20, parent=left_rot.left.left)
    left_rot.left.left.right = RedBlackTree(-5, parent=left_rot.left.left)
    left_rot.right = RedBlackTree(20, parent=left_rot)
    tree = tree.rotate_left()
    if tree != left_rot:
        return False
    tree = tree.rotate_right()
    tree = tree.rotate_right()
    # Make the left rotation
    right_rot = RedBlackTree(-10)
    right_rot.left = RedBlackTree(-20, parent=right_rot)
    right_rot.right = RedBlackTree(0, parent=right_rot)
    right_rot.right.left = RedBlackTree(-5, parent=right_rot.right)
    right_rot.right.right = RedBlackTree(10, parent=right_rot.right)
    right_rot.right.right.left = RedBlackTree(5, parent=right_rot.right.right)
    right_rot.right.right.right = RedBlackTree(20, parent=right_rot.right.right)
    if tree != right_rot:
        return False
    return True

def test_insertion_speed():
    """Test that the tree balances inserts to O(log(n)) by doing a lot
    of them.
    """
    tree = RedBlackTree(-1)
    for i in range(300000):
        tree = tree.insert(i)
    return True

def test_insert():
    """Test the insert() method of the tree correctly balances, colors,
    and inserts.
    """
    tree = RedBlackTree(0)
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    ans = RedBlackTree(0, 0)
    ans.left = RedBlackTree(-8, 0, ans)
    ans.right = RedBlackTree(8, 1, ans)
    ans.right.left = RedBlackTree(4, 0, ans.right)
    ans.right.right = RedBlackTree(11, 0, ans.right)
    ans.right.right.left = RedBlackTree(10, 1, ans.right.right)
    ans.right.right.right = RedBlackTree(12, 1, ans.right.right)
    return tree == ans

def test_insert_and_search():
    """Tests searching through the tree for values."""
    tree = RedBlackTree(0)
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    if 5 in tree or -6 in tree or -10 in tree or 13 in tree:
        # Found something not in there
        return False
    if not (11 in tree and 12 in tree and -8 in tree and 0 in tree):
        # Didn't find something in there
        return False
    return True

def test_floor_ceil():
    """Tests the floor and ceiling functions in the tree."""
    tree = RedBlackTree(0)
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    tuples = [(-20, None, -16), (-10, -16, 0), (8, 8, 8), (50, 24, None)]
    for val, floor, ceil in tuples:
        if tree.floor(val) != floor or tree.ceil(val) != ceil:
            return False
    return True

def test_min_max():
    """Tests the min and max functions in the tree."""
    tree = RedBlackTree(0)
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    if tree.get_max() != 22 or tree.get_min() != -16:
        return False
    return True

def test_tree_traversal():
    """Tests the three different tree traversal functions."""
    tree = RedBlackTree(0)
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    if list(tree.inorder_traverse()) != [-16, 0, 8, 16, 20, 22, 24]:
        return False
    if list(tree.preorder_traverse()) != [0, -16, 16, 8, 22, 20, 24]:
        return False
    if list(tree.postorder_traverse()) != [-16, 8, 20, 24, 22, 16, 0]:
        return False
    return True

def main():
    if test_rotations():
        print('Rotating right and left works!')
    else:
        print('Rotating right and left doesn\'t work. :(')
    if test_insert():
        print('Inserting works!')
    else:
        print('Inserting doesn\'t work :(')
    if test_insert_and_search():
        print('Searching works!')
    else:
        print('Searching doesn\'t work :(')
    if test_floor_ceil():
        print('Floor and ceil work!')
    else:
        print('Floor and ceil don\'t work :(')
    if test_tree_traversal():
        print('Tree traversal works!')
    else:
        print('Tree traversal doesn\'t work :(')
    print('Testing tree balancing...')
    print('This should only be a few seconds.')
    test_insertion_speed()
    print('Done!')

if __name__ == '__main__':
    main()
