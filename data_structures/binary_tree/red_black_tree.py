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
    Examples:
    >>> tree = RedBlackTree(0)
    >>> tree = tree.insert(8).insert(-8).insert(4).insert(12)
    >>> tree.check_color_properties()
    True
    >>> list(tree.inorder_traverse())
    [-8, 0, 4, 8, 12]
    >>> tree.search(4).label
    4
    >>> tree.floor(5)
    4
    >>> tree.ceil(5)
    8
    >>> tree.get_min()
    -8
    >>> tree.get_max()
    12
    >>> tree = tree.remove(4)
    >>> 4 in tree
    False
    """

    def __init__(
        self,
        label: int | None = None,
        color: int = 0,
        parent: RedBlackTree | None = None,
        left: RedBlackTree | None = None,
        right: RedBlackTree | None = None,
    ) -> None:
        """Initialize a new Red-Black Tree node.

        Args:
            label: The value associated with this node
            color: 0 if black, 1 if red
            parent: The parent to this node
            left: This node's left child
            right: This node's right child

        Examples:
        >>> node = RedBlackTree(5)
        >>> node.label
        5
        >>> node.color
        0
        """
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def rotate_left(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the left.

        Returns:
            The new root of the subtree

        Examples:
        >>> root = RedBlackTree(2)
        >>> root.right = RedBlackTree(4)
        >>> root.right.left = RedBlackTree(3)
        >>> new_root = root.rotate_left()
        >>> new_root.label
        4
        >>> new_root.left.label
        2
        >>> new_root.left.right.label
        3
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
        """Rotate the subtree rooted at this node to the right.

        Returns:
            The new root of the subtree

        Examples:
        >>> root = RedBlackTree(4)
        >>> root.left = RedBlackTree(2)
        >>> root.left.right = RedBlackTree(3)
        >>> new_root = root.rotate_right()
        >>> new_root.label
        2
        >>> new_root.right.label
        4
        >>> new_root.right.left.label
        3
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
        """Insert a label into the tree.

        Args:
            label: The value to insert

        Returns:
            The root of the tree

        Examples:
        >>> tree = RedBlackTree()
        >>> tree = tree.insert(5).insert(3).insert(7)
        >>> list(tree.inorder_traverse())
        [3, 5, 7]
        >>> tree.check_color_properties()
        True
        """
        if self.label is None:
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
        """Repair the coloring after insertion."""
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

    def remove(self, label: int) -> RedBlackTree:
        """Remove a label from the tree.

        Args:
            label: The value to remove

        Returns:
            The root of the tree

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3).insert(7)
        >>> tree = tree.remove(3)
        >>> 3 in tree
        False
        >>> tree.check_color_properties()
        True
        """
        if self.label == label:
            if self.left and self.right:
                # It's easier to balance a node with at most one child,
                # so we replace this node with the greatest one less than
                # it and remove that.

                value = self.left.get_max()
                if value is not None:
                    self.label = value
                    self.left.remove(value)
            else:
                child = self.left or self.right
                if self.color == 1:
                    if self.parent:
                        if self.is_left():
                            self.parent.left = None
                        else:
                            self.parent.right = None
                elif child is None:
                    if self.parent is None:
                        return RedBlackTree(None)
                    else:
                        self._remove_repair()
                        if self.is_left():
                            self.parent.left = None
                        else:
                            self.parent.right = None
                        self.parent = None
                else:
                    self.label = child.label
                    self.left = child.left
                    self.right = child.right
                    if self.left:
                        self.left.parent = self
                    if self.right:
                        self.right.parent = self
        elif self.label is not None and self.label > label:
            if self.left:
                self.left.remove(label)
        elif self.right:
            self.right.remove(label)
        return self.parent or self

    def _remove_repair(self) -> None:
        """Repair the coloring after removal."""
        if (
            self.parent is None
            or self.sibling is None
            or self.parent.sibling is None
            or self.grandparent is None
        ):
            return
        if color(self.sibling) == 1:
            self.sibling.color = 0
            self.parent.color = 1
            if self.is_left():
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
        if (
            color(self.parent) == 0
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent._remove_repair()
            return
        if (
            color(self.parent) == 1
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent.color = 0
            return
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 0
            and color(self.sibling.left) == 1
        ):
            self.sibling.rotate_right()
            self.sibling.color = 0
            if self.sibling.right:
                self.sibling.right.color = 1
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
            and color(self.sibling.left) == 0
        ):
            self.sibling.rotate_left()
            self.sibling.color = 0
            if self.sibling.left:
                self.sibling.left.color = 1
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
        ):
            self.parent.rotate_left()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.left) == 1
        ):
            self.parent.rotate_right()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0

    def check_color_properties(self) -> bool:
        """
        Verify that all Red-Black Tree properties are satisfied:
        1. Root node is black
        2. No two consecutive red nodes
        3. All paths have same black height

        Returns:
            True if all properties are satisfied, False otherwise
        """
        # Property 1: Root must be black
        if self.parent is None and self.color != 0:
            return False

        # Property 2: No two consecutive red nodes
        if not self.check_coloring():
            return False

        # Property 3: All paths have same black height
        return self.black_height() is not None

    def check_coloring(self) -> bool:
        """Check if the tree satisfies Red-Black property 4."""
        if self.color == 1 and 1 in (color(self.left), color(self.right)):
            return False
        if self.left and not self.left.check_coloring():
            return False
        return not (self.right and not self.right.check_coloring())

    def black_height(self) -> int | None:
        """
        Calculate the black height of the tree and verify consistency
        - Black height = number of black nodes from current node to any leaf
        - Returns None if any path has different black height

        Returns:
            Black height if consistent, None otherwise
        """
        # Leaf node case (both children are None)
        if self.left is None and self.right is None:
            # Count: current node (if black) + leaf (black)
            return 1 + (1 - self.color)  # 2 if black, 1 if red

        # Get black heights from both subtrees
        left_bh = self.left.black_height() if self.left else 1
        right_bh = self.right.black_height() if self.right else 1

        # Validate consistency
        if left_bh is None or right_bh is None or left_bh != right_bh:
            return None

        # Add current node's contribution (1 if black, 0 if red)
        return left_bh + (1 - self.color)

    def __contains__(self, label: int) -> bool:
        """Check if the tree contains a label.

        Args:
            label: The value to check

        Returns:
            True if the label is in the tree, False otherwise

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3)
        >>> 3 in tree
        True
        >>> 4 in tree
        False
        """
        return self.search(label) is not None

    def search(self, label: int) -> RedBlackTree | None:
        """Search for a label in the tree.

        Args:
            label: The value to search for

        Returns:
            The node containing the label, or None if not found

        Examples:
        >>> tree = RedBlackTree(5)
        >>> node = tree.search(5)
        >>> node.label
        5
        >>> tree.search(10) is None
        True
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
        """Find the largest element <= label.

        Args:
            label: The value to find the floor of

        Returns:
            The floor value, or None if no such element exists

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3).insert(7)
        >>> tree.floor(6)
        5
        >>> tree.floor(2) is None
        True
        """
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
        """Find the smallest element >= label.

        Args:
            label: The value to find the ceil of

        Returns:
            The ceil value, or None if no such element exists

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3).insert(7)
        >>> tree.ceil(6)
        7
        >>> tree.ceil(8) is None
        True
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
        """Get the maximum element in the tree.

        Returns:
            The maximum value, or None if the tree is empty

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3).insert(7)
        >>> tree.get_max()
        7
        """
        if self.right:
            return self.right.get_max()
        else:
            return self.label

    def get_min(self) -> int | None:
        """Get the minimum element in the tree.

        Returns:
            The minimum value, or None if the tree is empty

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3).insert(7)
        >>> tree.get_min()
        3
        """
        if self.left:
            return self.left.get_min()
        else:
            return self.label

    @property
    def grandparent(self) -> RedBlackTree | None:
        """Get the grandparent of this node."""
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    @property
    def sibling(self) -> RedBlackTree | None:
        """Get the sibling of this node."""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def is_left(self) -> bool:
        """Check if this node is the left child of its parent."""
        if self.parent is None:
            return False
        return self.parent.left is self

    def is_right(self) -> bool:
        """Check if this node is the right child of its parent."""
        if self.parent is None:
            return False
        return self.parent.right is self

    def __bool__(self) -> bool:
        """Return True if the tree is not empty."""
        return True

    def __len__(self) -> int:
        """Return the number of nodes in the tree.

        Examples:
        >>> tree = RedBlackTree(5)
        >>> tree = tree.insert(3).insert(7)
        >>> len(tree)
        3
        """
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        return ln

    def preorder_traverse(self) -> Iterator[int | None]:
        """Traverse the tree in pre-order.

        Yields:
            The values in pre-order

        Examples:
        >>> tree = RedBlackTree(2)
        >>> tree.left = RedBlackTree(1)
        >>> tree.right = RedBlackTree(3)
        >>> list(tree.preorder_traverse())
        [2, 1, 3]
        """
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()

    def inorder_traverse(self) -> Iterator[int | None]:
        """Traverse the tree in in-order.

        Yields:
            The values in in-order

        Examples:
        >>> tree = RedBlackTree(2)
        >>> tree.left = RedBlackTree(1)
        >>> tree.right = RedBlackTree(3)
        >>> list(tree.inorder_traverse())
        [1, 2, 3]
        """
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()

    def postorder_traverse(self) -> Iterator[int | None]:
        """Traverse the tree in post-order.

        Yields:
            The values in post-order

        Examples:
        >>> tree = RedBlackTree(2)
        >>> tree.left = RedBlackTree(1)
        >>> tree.right = RedBlackTree(3)
        >>> list(tree.postorder_traverse())
        [1, 3, 2]
        """
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label

    def __repr__(self) -> str:
        """Return a string representation of the tree."""
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

    def __hash__(self):
        """Return a hash value for the node."""
        return hash((self.label, self.color))


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
    tree = RedBlackTree(0)
    tree.left = RedBlackTree(-10, parent=tree)
    tree.right = RedBlackTree(10, parent=tree)
    tree.left.left = RedBlackTree(-20, parent=tree.left)
    tree.left.right = RedBlackTree(-5, parent=tree.left)
    tree.right.left = RedBlackTree(5, parent=tree.right)
    tree.right.right = RedBlackTree(20, parent=tree.right)
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
        return False
    return all(i in tree for i in (11, 12, -8, 0))


def test_insert_delete() -> bool:
    """Test the insert() and delete() method of the tree."""
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
    import doctest

    failures, _ = doctest.testmod()
    if failures == 0:
        print("All doctests passed!")
    else:
        print(f"{failures} doctests failed!")

    print_results("Rotating right and left", test_rotations())
    print_results("Inserting", test_insert())
    print_results("Searching", test_insert_and_search())
    print_results("Deleting", test_insert_delete())
    print_results("Floor and ceil", test_floor_ceil())
    print_results("Tree traversal", test_tree_traversal())
    print_results("Tree chaining", test_tree_chaining())
    print("Testing tree balancing...")
    print("This should only be a few seconds.")
    test_insertion_speed()
    print("Done!")


if __name__ == "__main__":
    main()
