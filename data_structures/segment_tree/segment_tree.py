"""Segment Tree Data Structure.

A Segment Tree is a binary tree used for storing intervals or segments.
It allows querying which of the stored segments contain a given point.
Typically used for range queries and updates.

Time Complexity:
- Build: O(n)
- Query: O(log n)
- Update: O(log n)

Space Complexity: O(n)
"""

from typing import Callable


class SegmentTree:
    """Segment Tree implementation for range queries.

    This implementation supports range sum queries and point updates.
    Can be extended to support other operations like min/max queries.

    Attributes:
        tree: List storing the segment tree nodes
        n: Size of the input array
        operation: Function to combine two values (default: addition)

    >>> st = SegmentTree([1, 3, 5, 7, 9, 11])
    >>> st.query(1, 3)
    15
    >>> st.update(1, 10)
    >>> st.query(1, 3)
    22
    >>> st.query(0, 5)
    42
    >>> st2 = SegmentTree([2, 4, 6, 8], operation=min)
    >>> st2.query(0, 3)
    2
    >>> st2.update(0, 10)
    >>> st2.query(0, 3)
    4
    """

    def __init__(
        self, arr: list[int], operation: Callable[[int, int], int] = lambda a, b: a + b
    ) -> None:
        """Initialize segment tree with given array.

        Args:
            arr: Input array of integers
            operation: Binary operation to combine values (default: addition)

        >>> st = SegmentTree([1, 2, 3])
        >>> len(st.tree)
        8
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Allocate space for segment tree
        self.operation = operation
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr: list[int], node: int, start: int, end: int) -> None:
        """Build segment tree recursively.

        Args:
            arr: Input array
            node: Current node index in tree
            start: Start index of current segment
            end: End index of current segment
        """
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)
            self.tree[node] = self.operation(
                self.tree[left_child], self.tree[right_child]
            )

    def query(self, left: int, right: int) -> int:
        """Query for value in range [left, right].

        Args:
            left: Left boundary of query range (inclusive)
            right: Right boundary of query range (inclusive)

        Returns:
            Result of applying operation over the range

        >>> st = SegmentTree([1, 2, 3, 4, 5])
        >>> st.query(0, 2)
        6
        >>> st.query(2, 4)
        12
        """
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """Recursive helper for range query.

        Args:
            node: Current node index
            start: Start of current segment
            end: End of current segment
            left: Query left boundary
            right: Query right boundary

        Returns:
            Query result for current segment
        """
        if right < start or left > end:
            # No overlap
            return 0 if self.operation(0, 0) == 0 else float('inf')

        if left <= start and end <= right:
            # Complete overlap
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_result = self._query(left_child, start, mid, left, right)
        right_result = self._query(right_child, mid + 1, end, left, right)
        return self.operation(left_result, right_result)

    def update(self, index: int, value: int) -> None:
        """Update value at given index.

        Args:
            index: Index to update
            value: New value

        >>> st = SegmentTree([1, 2, 3, 4, 5])
        >>> st.query(0, 4)
        15
        >>> st.update(2, 10)
        >>> st.query(0, 4)
        22
        """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node: int, start: int, end: int, index: int, value: int) -> None:
        """Recursive helper for point update.

        Args:
            node: Current node index
            start: Start of current segment
            end: End of current segment
            index: Index to update
            value: New value
        """
        if start == end:
            # Leaf node
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)
            self.tree[node] = self.operation(
                self.tree[left_child], self.tree[right_child]
            )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
