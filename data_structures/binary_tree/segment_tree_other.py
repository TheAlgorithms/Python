"""
Segment_tree creates a segment tree with a given array and function,
allowing queries to be done later in log(N) time
function takes 2 values and returns a same type value
"""

from queue import Queue
from collections.abc import Sequence


class SegmentTreeNode(object):
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.mid = (start + end) // 2
        self.left = left
        self.right = right

    def __str__(self):
        return 'val: %s, start: %s, end: %s' % (self.val, self.start, self.end)


class SegmentTree(object):
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
        update value in collection
        :param i: index of collection
        :param val: new value
        :return:
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.update(1, 5)
        """
        self._update_tree(self.root, i, val)

    def query_range(self, i, j):
        """
        Sum, Max, Min operation in intervals i and j([i, j])
        :param i:  left index
        :param j:  right index
        :return:  Sum, Max, Min
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

    def _update_tree(self, root, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        if i <= root.mid:
            self._update_tree(root.left, i, val)
        else:
            self._update_tree(root.right, i, val)
        root.val = self.fn(root.left.val, root.right.val)

    def _query_range(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        """
         [i, j] [i, j] [i, j]
        [start mid] [mid+1 end]
        """
        if j <= root.mid:
            return self._query_range(root.left, i, j)
        elif i > root.mid:
            return self._query_range(root.right, i, j)
        else:
            return self.fn(self._query_range(root.left, i, root.mid), self._query_range(root.right, root.mid + 1, j))

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


if __name__ == '__main__':
    import operator
    for fn in [operator.add, max, min]:
        print('*' * 50)
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
