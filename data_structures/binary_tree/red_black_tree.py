from __future__ import annotations

from collections.abc import Iterator


class RedBlackTree:
    """
    A Red-Black tree, which is a self-balancing BST (binary search
    tree).
    This tree has similar performance to AVL trees, but the balancing is
    less strict, so it will perform faster for writing/deleting nodes
    and slower for reading in the average case, though, because they're
    both balanced binary search trees, both will get the same asymptotic
    performance.
    To read more about them, https://en.wikipedia.org/wiki/Red-black_tree
    Unless otherwise specified, all asymptotic runtimes are specified in
    terms of the size of the tree.
    """

    def __init__(
        self,
        label: int | None = None,
        color: int = 0,
        parent: RedBlackTree | None = None,
        left: RedBlackTree | None = None,
        right: RedBlackTree | None = None,
    ) -> None:
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

    # Here are functions which are specific to red-black trees

    def rotate_left(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the left and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).
        """
        parent = self.parent
        right = self.right
        if right is None:
            return self
        self.right = right.left
        if self.right:
            self.right.parent = self
        self.parent = right
        right.left = self
        if parent is not None:
            if parent.left == self:
                parent.left = right
            else:
                parent.right = right
        right.parent = parent
        return right

    def rotate_right(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the right and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).
        """
        if self.left is None:
            return self
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

    def insert(self, label: int) -> RedBlackTree:
        """Inserts label into the subtree rooted at self, performs any
        rotations necessary to maintain balance, and then returns the
        new root to this subtree (likely self).
        This is guaranteed to run in O(log(n)) time.
        """
        if self.label is None:
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
        elif self.right:
            self.right.insert(label)
        else:
            self.right = RedBlackTree(label, 1, self)
            self.right._insert_repair()
        return self.parent or self

    def _insert_repair(self) -> None:
        """Repair the coloring from inserting into a tree."""
        if self.parent is None:
            self.color = 0
        elif color(self.parent) == 0:
            self.color = 1
        else:
            uncle = self.parent.sibling
            if color(uncle) == 0:
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    if self.right:
                        self.right._insert_repair()
                elif self.is_right() and self.parent.is_left():
                    self.parent.rotate_left()
                    if self.left:
                        self.left._insert_repair()
                elif self.is_left():
                    if self.grandparent:
                        self.grandparent.rotate_right()
                        self.parent.color = 0
                    if self.parent.right:
                        self.parent.right.color = 1
                else:
                    if self.grandparent:
                        self.grandparent.rotate_left()
                        self.parent.color = 0
                    if self.parent.left:
                        self.parent.left.color = 1
            else:
                self.parent.color = 0
                if uncle and self.grandparent:
                    uncle.color = 0
                    self.grandparent.color = 1
                    self.grandparent._insert_repair()

    def remove(self, label: int) -> "RedBlackTree":
        """Remove label from this tree"""
        if self.label is None:
            return self

        target = self.search(label)
        if target is None:
            return self.parent or self

        target._remove_node()
        return self.parent or self

    def _remove_node(self) -> None:
        """
        Physically remove the current node from the tree,
        preserving all the invariants of the red-black tree
        """
        if self.left and self.right:
            self._remove_with_two_children()
        else:
            self._remove_with_zero_or_one_child()

    def _remove_with_two_children(self) -> None:
        """
        Handling the case when a node has two non-empty children:
        Find the maximum in the left subtree, copy the value,
        Delete the maximum in the left subtree
        """
        left = self.left
        if left is None:
            # Logically this should not happen if the caller knows that
            # the node has two children, but this guard keeps type
            # checkers happy and makes the method safer.
            return

        value = left.get_max()
        if value is None:
            # No value in the left subtree - nothing to do.
            return

        # Copy the predecessor value into the current node and
        # delete the predecessor from the left subtree.
        self.label = value
        left.remove(value)

    def _remove_with_zero_or_one_child(self) -> None:
        """
        Handling the case when a node has 0 or 1 child
        """
        child = self.left or self.right

        if self.color == 1:
            self._remove_red_leaf()
            return

        if child is None:
            self._remove_black_leaf()
            return

        self._remove_black_node_with_red_child(child)

    def _remove_red_leaf(self) -> None:
        """
        delete red leaf
        """
        if self.parent is None:
            self.label = None
            return

        if self.is_left():
            self.parent.left = None
        else:
            self.parent.right = None
        self.parent = None

    def _remove_black_leaf(self) -> None:
        """
        delete black leaf
        """
        if self.parent is None:
            self.label = None
            return

        self._remove_repair()

        if self.is_left():
            self.parent.left = None
        else:
            self.parent.right = None
        self.parent = None

    def _remove_black_node_with_red_child(self, child: "RedBlackTree") -> None:
        """
        Black knot with a single red child:
        Move the child to the top and paint it black.
        """
        self.label = child.label
        self.left = child.left
        self.right = child.right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
        self.color = 0

    def _remove_repair(self) -> None:
        """Repair the coloring of the tree that may have been messed up
        after deleting a black node.
        """
        if (
            self.parent is None
            or self.sibling is None
            or self.parent.grandparent is None
        ):
            return

        self._repair_red_sibling()

        if self._repair_black_parent_black_sibling_black_children():
            return

        if self._repair_red_parent_black_sibling_black_children():
            return

        self._repair_inner_nephew()

        self._repair_outer_nephew()

    def _repair_red_sibling(self) -> None:
        """Case 1: sibling is red.

        We rotate around the parent so that the sibling becomes black,
        and then we continue with a configuration where the sibling is
        black and the parent is red.
        """
        sibling = self.sibling
        parent = self.parent

        if sibling is None or parent is None:
            return

        if color(sibling) != 1:
            return

        sibling.color = 0
        parent.color = 1

        if self.is_left():
            parent.rotate_left()
        else:
            parent.rotate_right()

    def _repair_black_parent_black_sibling_black_children(self) -> bool:
        """Case 2:
        parent black, sibling black, sibling.left & sibling.right black.

        In this case we recolor the sibling red and propagate the
        "double black" upwards to the parent.
        """
        parent = self.parent
        sibling = self.sibling

        if parent is None or sibling is None:
            return False

        if color(parent) != 0:
            return False
        if color(sibling) != 0:
            return False
        if color(sibling.left) != 0:
            return False
        if color(sibling.right) != 0:
            return False

        sibling.color = 1
        parent._remove_repair()
        return True

    def _repair_red_parent_black_sibling_black_children(self) -> bool:
        """Case 3:
        parent red, sibling black, sibling.left & sibling.right black.

        We just swap the colors of the parent and sibling and finish.
        """
        parent = self.parent
        sibling = self.sibling

        if parent is None or sibling is None:
            return False

        if color(parent) != 1:
            return False
        if color(sibling) != 0:
            return False
        if color(sibling.left) != 0:
            return False
        if color(sibling.right) != 0:
            return False

        sibling.color = 1
        parent.color = 0
        return True

    def _repair_inner_nephew(self) -> None:
        """Case 4: inner nephew is red.

        We rotate around the sibling to turn this into the outer-nephew
        case (case 5), which can then be fixed by a rotation around
        the parent.
        """
        sibling = self.sibling
        if sibling is None:
            return

        # Left child, red left (inner) nephew
        if (
            self.is_left()
            and color(sibling) == 0
            and color(sibling.right) == 0
            and color(sibling.left) == 1
        ):
            sibling.rotate_right()
            sibling.color = 0
            if sibling.right:
                sibling.right.color = 1

        # Right child, red right (inner) nephew
        if (
            self.is_right()
            and color(sibling) == 0
            and color(sibling.right) == 1
            and color(sibling.left) == 0
        ):
            sibling.rotate_left()
            sibling.color = 0
            if sibling.left:
                sibling.left.color = 1

    def _repair_outer_nephew(self) -> None:
        """Case 5: outer nephew is red.

        This is the final case: a rotation around the parent and
        recoloring of parent / sibling / grandparent fixes the violation.
        """
        sibling = self.sibling
        parent = self.parent
        grandparent = self.grandparent

        if sibling is None or parent is None or grandparent is None:
            return

        # Left child, red right (outer) nephew
        if self.is_left() and color(sibling) == 0 and color(sibling.right) == 1:
            parent.rotate_left()
            grandparent.color = parent.color
            parent.color = 0

            parent_sibling = parent.sibling
            if parent_sibling is not None:
                parent_sibling.color = 0

        # Right child, red left (outer) nephew
        if self.is_right() and color(sibling) == 0 and color(sibling.left) == 1:
            parent.rotate_right()
            grandparent.color = parent.color
            parent.color = 0

            parent_sibling = parent.sibling
            if parent_sibling is not None:
                parent_sibling.color = 0

    def check_color_properties(self) -> bool:
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
            print("Property 2")
            return False
        # Property 3 does not need to be checked, because None is assumed
        # to be black and is all the leaves.
        # Property 4
        if not self.check_coloring():
            print("Property 4")
            return False
        # Property 5
        if self.black_height() is None:
            print("Property 5")
            return False
        # All properties were met
        return True

    def check_coloring(self) -> bool:
        """A helper function to recursively check Property 4 of a
        Red-Black Tree. See check_color_properties for more info.
        """
        if self.color == 1 and 1 in (color(self.left), color(self.right)):
            return False
        if self.left and not self.left.check_coloring():
            return False
        return not (self.right and not self.right.check_coloring())

    def black_height(self) -> int | None:
        """Returns the number of black nodes from this node to the
        leaves of the tree, or None if there isn't one such value (the
        tree is color incorrectly).
        """
        if self is None or self.left is None or self.right is None:
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
        return left + (1 - self.color)

    # Here are functions which are general to all binary search trees

    def __contains__(self, label: int) -> bool:
        """Search through the tree for label, returning True iff it is
        found somewhere in the tree.
        Guaranteed to run in O(log(n)) time.
        """
        return self.search(label) is not None

    def search(self, label: int) -> RedBlackTree | None:
        """Search through the tree for label, returning its node if
        it's found, and None otherwise.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self
        elif self.label is not None and label > self.label:
            if self.right is None:
                return None
            else:
                return self.right.search(label)
        elif self.left is None:
            return None
        else:
            return self.left.search(label)

    def floor(self, label: int) -> int | None:
        """Returns the largest element in this tree which is at most label.
        This method is guaranteed to run in O(log(n)) time."""
        if self.label == label:
            return self.label
        elif self.label is not None and self.label > label:
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

    def ceil(self, label: int) -> int | None:
        """Returns the smallest element in this tree which is at least label.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self.label
        elif self.label is not None and self.label < label:
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

    def get_max(self) -> int | None:
        """Returns the largest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.right:
            # Go as far right as possible
            return self.right.get_max()
        else:
            return self.label

    def get_min(self) -> int | None:
        """Returns the smallest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.left:
            # Go as far left as possible
            return self.left.get_min()
        else:
            return self.label

    @property
    def grandparent(self) -> RedBlackTree | None:
        """Get the current node's grandparent, or None if it doesn't exist."""
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    @property
    def sibling(self) -> RedBlackTree | None:
        """Get the current node's sibling, or None if it doesn't exist."""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def is_left(self) -> bool:
        """Returns true iff this node is the left child of its parent."""
        if self.parent is None:
            return False
        return self.parent.left is self

    def is_right(self) -> bool:
        """Returns true iff this node is the right child of its parent."""
        if self.parent is None:
            return False
        return self.parent.right is self

    def __bool__(self) -> bool:
        return True

    def __len__(self) -> int:
        """
        Return the number of nodes in this tree.
        """
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        return ln

    def preorder_traverse(self) -> Iterator[int | None]:
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()

    def inorder_traverse(self) -> Iterator[int | None]:
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()

    def postorder_traverse(self) -> Iterator[int | None]:
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return f"'{self.label} {(self.color and 'red') or 'blk'}'"
        return pformat(
            {
                f"{self.label} {(self.color and 'red') or 'blk'}": (
                    self.left,
                    self.right,
                )
            },
            indent=1,
        )

    def __eq__(self, other: object) -> bool:
        """Test if two trees are equal."""
        if not isinstance(other, RedBlackTree):
            return NotImplemented
        if self.label == other.label:
            return self.left == other.left and self.right == other.right
        else:
            return False


def color(node: RedBlackTree | None) -> int:
    """Returns the color of a node, allowing for None leaves."""
    if node is None:
        return 0
    else:
        return node.color


"""
Code for testing the various
functions of the red-black tree.
"""


def test_rotations() -> bool:
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
    return tree == right_rot


def test_insertion_speed() -> bool:
    """Test that the tree balances inserts to O(log(n)) by doing a lot
    of them.
    """
    tree = RedBlackTree(-1)
    for i in range(300000):
        tree = tree.insert(i)
    return True


def test_insert() -> bool:
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


def test_insert_and_search() -> bool:
    """Tests searching through the tree for values."""
    tree = RedBlackTree(0)
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    if any(i in tree for i in (5, -6, -10, 13)):
        # Found something not in there
        return False
    # Find all these things in there
    return all(i in tree for i in (11, 12, -8, 0))


def test_insert_delete() -> bool:
    """Test the insert() and delete() method of the tree, verifying the
    insertion and removal of elements, and the balancing of the tree.
    """
    tree = RedBlackTree(0)
    tree = tree.insert(-12)
    tree = tree.insert(8)
    tree = tree.insert(-8)
    tree = tree.insert(15)
    tree = tree.insert(4)
    tree = tree.insert(12)
    tree = tree.insert(10)
    tree = tree.insert(9)
    tree = tree.insert(11)
    tree = tree.remove(15)
    tree = tree.remove(-12)
    tree = tree.remove(9)
    if not tree.check_color_properties():
        return False
    return list(tree.inorder_traverse()) == [-8, 0, 4, 8, 10, 11, 12]


def test_floor_ceil() -> bool:
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


def test_min_max() -> bool:
    """Tests the min and max functions in the tree."""
    tree = RedBlackTree(0)
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    return not (tree.get_max() != 22 or tree.get_min() != -16)


def test_tree_traversal() -> bool:
    """Tests the three different tree traversal functions."""
    tree = RedBlackTree(0)
    tree = tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    if list(tree.inorder_traverse()) != [-16, 0, 8, 16, 20, 22, 24]:
        return False
    if list(tree.preorder_traverse()) != [0, -16, 16, 8, 22, 20, 24]:
        return False
    return list(tree.postorder_traverse()) == [-16, 8, 20, 24, 22, 16, 0]


def test_tree_chaining() -> bool:
    """Tests the three different tree chaining functions."""
    tree = RedBlackTree(0)
    tree = tree.insert(-16).insert(16).insert(8).insert(24).insert(20).insert(22)
    if list(tree.inorder_traverse()) != [-16, 0, 8, 16, 20, 22, 24]:
        return False
    if list(tree.preorder_traverse()) != [0, -16, 16, 8, 22, 20, 24]:
        return False
    return list(tree.postorder_traverse()) == [-16, 8, 20, 24, 22, 16, 0]


def print_results(msg: str, passes: bool) -> None:
    print(str(msg), "works!" if passes else "doesn't work :(")


def pytests() -> None:
    assert test_rotations()
    assert test_insert()
    assert test_insert_and_search()
    assert test_insert_delete()
    assert test_floor_ceil()
    assert test_tree_traversal()
    assert test_tree_chaining()


def main() -> None:
    """
    >>> pytests()
    """
    print_results("Rotating right and left", test_rotations())
    print_results("Inserting", test_insert())
    print_results("Searching", test_insert_and_search())
    print_results("Deleting", test_insert_delete())
    print_results("Floor and ceil", test_floor_ceil())
    print_results("Tree traversal", test_tree_traversal())
    print_results("Tree traversal", test_tree_chaining())
    print("Testing tree balancing...")
    print("This should only be a few seconds.")
    test_insertion_speed()
    print("Done!")


if __name__ == "__main__":
    main()
