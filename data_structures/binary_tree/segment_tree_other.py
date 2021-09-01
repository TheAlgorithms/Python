"""
Segment_tree creates a segment tree with a given array and function,
allowing queries to be done later in log(N) time
function takes 2 values and returns a same type value
"""
from collections.abc import Sequence
from functools import reduce
from queue import Queue
from typing import Optional, TypeVar

IntOrFloat = TypeVar("IntOrFloat", int, float)


class SegmentTreeNode:
    def __init__(
        self,
        start: int,
        end: int,
        val: IntOrFloat,
        left: "SegmentTreeNode" = None,
        right: "SegmentTreeNode" = None,
    ):
        self.start = start
        self.end = end
        self.val = val
        self.mid = (start + end) // 2
        self.left = left
        self.right = right
        self.lazy: Optional[IntOrFloat] = None

    def __str__(self):
        return f"val: {self.val}, start: {self.start}, end: {self.end}"


class SegmentTree:
    """
    >>> import operator
    >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
    >>> for node in num_arr.traverse():
    ...     print(node)
    ...
    val: 15, start: 0, end: 4
    val: 8, start: 0, end: 2
    val: 7, start: 3, end: 4
    val: 3, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 1, start: 1, end: 1
    >>>
    >>> num_arr.update(1, 5)
    >>> for node in num_arr.traverse():
    ...     print(node)
    ...
    val: 19, start: 0, end: 4
    val: 12, start: 0, end: 2
    val: 7, start: 3, end: 4
    val: 7, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 5, start: 1, end: 1
    >>>
    >>> num_arr.query_range(3, 4)
    7
    >>> num_arr.query_range(2, 2)
    5
    >>> num_arr.query_range(1, 3)
    13
    >>>
    >>> max_arr = SegmentTree([2, 1, 5, 3, 4], max)
    >>> for node in max_arr.traverse():
    ...     print(node)
    ...
    val: 5, start: 0, end: 4
    val: 5, start: 0, end: 2
    val: 4, start: 3, end: 4
    val: 2, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 1, start: 1, end: 1
    >>>
    >>> max_arr.update(1, 5)
    >>> for node in max_arr.traverse():
    ...     print(node)
    ...
    val: 5, start: 0, end: 4
    val: 5, start: 0, end: 2
    val: 4, start: 3, end: 4
    val: 5, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 5, start: 1, end: 1
    >>>
    >>> max_arr.query_range(3, 4)
    4
    >>> max_arr.query_range(2, 2)
    5
    >>> max_arr.query_range(1, 3)
    5
    >>>
    >>> min_arr = SegmentTree([2, 1, 5, 3, 4], min)
    >>> for node in min_arr.traverse():
    ...     print(node)
    ...
    val: 1, start: 0, end: 4
    val: 1, start: 0, end: 2
    val: 3, start: 3, end: 4
    val: 1, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 1, start: 1, end: 1
    >>>
    >>> min_arr.update(1, 5)
    >>> for node in min_arr.traverse():
    ...     print(node)
    ...
    val: 2, start: 0, end: 4
    val: 2, start: 0, end: 2
    val: 3, start: 3, end: 4
    val: 2, start: 0, end: 1
    val: 5, start: 2, end: 2
    val: 3, start: 3, end: 3
    val: 4, start: 4, end: 4
    val: 2, start: 0, end: 0
    val: 5, start: 1, end: 1
    >>>
    >>> min_arr.query_range(3, 4)
    3
    >>> min_arr.query_range(2, 2)
    5
    >>> min_arr.query_range(1, 3)
    3
    >>>

    """

    def __init__(self, collection: Sequence, function):
        self.collection = collection
        self.fn = function
        if self.collection:
            self.root = self._build_tree(0, len(collection) - 1)

    def update(self, i, val):
        """
        Update an element in log(N) time
        :param i: position to be update
        :param val: new value
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.update(1, 5)
        >>> num_arr.query_range(1, 3)
        13
        """
        self._update_tree(self.root, i, val)

    def update_range(self, i: int, j: int, val: IntOrFloat) -> None:
        """
        Update range [i, j] with val in log(N) time, range ends included
        :param i: left element index
        :param j: right element index
        :param val: new value
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.update_range(1, 3, 5)
        >>> num_arr.collection
        [2, 5, 5, 5, 4]
        >>> num_arr.query_range(1, 3)
        15
        >>> num_arr.query_range(3, 4)
        9
        >>> num_arr.query_range(0, 1)
        7
        """
        self.collection[i : j + 1] = [val] * (j - i + 1)
        self._update_tree_range(self.root, i, j, val)

    def query_range(self, i, j):
        """
        Get range query value in log(N) time
        :param i: left element index
        :param j: right element index
        :return: element combined in the range [i, j]
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.update(1, 5)
        >>> num_arr.query_range(3, 4)
        7
        >>> num_arr.query_range(2, 2)
        5
        >>> num_arr.query_range(1, 3)
        13
        >>>
        """
        return self._query_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.collection[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, self.fn(left.val, right.val), left, right)

    def _update_tree(self, node, i, val):
        if node.start == i and node.end == i:
            node.val = val
            return
        if i <= node.mid:
            self._update_tree(node.left, i, val)
        else:
            self._update_tree(node.right, i, val)
        node.val = self.fn(node.left.val, node.right.val)

    def _update_tree_range(
        self,
        node: SegmentTreeNode,
        i: int,
        j: int,
        val: IntOrFloat,
    ) -> None:
        """
        Update range recursively in log(N) time, range ends included.
        :param node: root node of current subtree
        :param i: left element index
        :param j: right element index
        :param val: new value
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr._update_tree_range(num_arr.root, 1, 3, 5)
        >>> num_arr.query_range(1, 3)
        15
        >>> num_arr.query_range(3, 4)
        9
        >>> num_arr.query_range(0, 1)
        7
        """
        if node.lazy is not None:
            # The node has lazy update value
            self._update_lazy(node, node.lazy)
            # No longer lazy
            node.lazy = None

        if node.start > j or node.end < i:
            # Not overlapping at all
            return

        if node.start >= i and node.end <= j:
            # Completely overlapping
            self._update_lazy(node, val)
            return

        self._update_tree_range(node.left, i, j, val)
        self._update_tree_range(node.right, i, j, val)
        node.val = self.fn(node.left.val, node.right.val)

    def _update_lazy(self, node: SegmentTreeNode, val: IntOrFloat) -> None:
        """Update node and mark it's subtrees for a lazy update.

        :param node: node to update.
        :param val: new value.

        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr._update_lazy(num_arr.root, 5)
        >>> num_arr.root.val
        25
        >>> l_subtree = num_arr.root.left
        >>> r_subtree = num_arr.root.right
        >>> l_subtree.lazy
        5
        >>> r_subtree.lazy
        5
        >>> num_arr._update_lazy(l_subtree, l_subtree.lazy)
        >>> l_subtree.val
        15
        >>> num_arr._update_lazy(r_subtree, r_subtree.lazy)
        >>> r_subtree.val
        10
        >>> l_subtree.left.lazy
        5
        >>> l_subtree.right.lazy
        5
        >>> r_subtree.left.lazy
        5
        >>> r_subtree.right.lazy
        5
        """
        node.val = reduce(self.fn, [val] * (node.end - node.start + 1))
        if node.start != node.end:
            # Not a leaf node
            node.left.lazy = val
            node.right.lazy = val

    def _query_range(self, node, i, j):
        if node.lazy is not None:
            # The node has lazy update value, update before querying
            self._update_lazy(node, node.lazy)
            # No longer lazy
            node.lazy = None

        if node.start == i and node.end == j:
            return node.val

        if i <= node.mid:
            if j <= node.mid:
                # range in left child tree
                return self._query_range(node.left, i, j)
            else:
                # range in left child tree and right child tree
                return self.fn(
                    self._query_range(node.left, i, node.mid),
                    self._query_range(node.right, node.mid + 1, j),
                )
        else:
            # range in right child tree
            return self._query_range(node.right, i, j)

    def traverse(self):
        if self.root is not None:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                yield node

                if node.left is not None:
                    queue.put(node.left)

                if node.right is not None:
                    queue.put(node.right)


if __name__ == "__main__":
    import operator

    for fn in [operator.add, max, min]:
        print("*" * 50)
        arr = SegmentTree([2, 1, 5, 3, 4], fn)
        for node in arr.traverse():
            print(node)
        print()

        arr.update(1, 5)
        for node in arr.traverse():
            print(node)
        print()

        print(arr.query_range(3, 4))  # 7
        print(arr.query_range(2, 2))  # 5
        print(arr.query_range(1, 3))  # 13
        print()
