"""
Segment Tree implementation for range queries and updates.

A Segment Tree is a data structure that allows efficient range queries
and range updates on an array. It supports operations like:
- Range sum queries
- Range minimum/maximum queries
- Range updates (lazy propagation)

Time Complexity:
    - Build: O(n)
    - Query: O(log n)
    - Update: O(log n)
    - Range Update: O(log n) with lazy propagation
Space Complexity: O(n)

Reference: https://en.wikipedia.org/wiki/Segment_tree
"""

from typing import List, Callable, Any
import math


class SegmentTree:
    """
    Segment Tree implementation with configurable operations.

    Attributes:
        data: Original array
        tree: Segment tree array
        size: Size of the original array
        operation: Function for combining values (e.g., sum, min, max)
        default_value: Default value for empty ranges
    """

    def __init__(
        self,
        data: List[int],
        operation: Callable[[int, int], int] = None,
        default_value: int = 0,
    ):
        """
        Initialize Segment Tree.

        Args:
            data: Input array
            operation: Function to combine two values (default: addition)
            default_value: Default value for empty ranges

        Examples:
            >>> st = SegmentTree([1, 2, 3, 4, 5])
            >>> st.query(0, 4)
            15
        """
        self.data = data.copy()
        self.size = len(data)
        self.operation = operation or (lambda x, y: x + y)
        self.default_value = default_value

        # Calculate tree size (next power of 2)
        self.tree_size = 2 * (2 ** math.ceil(math.log2(self.size))) - 1
        self.tree = [self.default_value] * self.tree_size

        self._build(0, 0, self.size - 1)

    def _build(self, node: int, start: int, end: int) -> None:
        """Build the segment tree recursively."""
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self._build(left_child, start, mid)
            self._build(right_child, mid + 1, end)

            self.tree[node] = self.operation(
                self.tree[left_child], self.tree[right_child]
            )

    def query(self, left: int, right: int) -> int:
        """
        Query range from left to right (0-indexed).

        Args:
            left: Left boundary (inclusive)
            right: Right boundary (inclusive)

        Returns:
            Result of the operation over the range

        Examples:
            >>> st = SegmentTree([1, 2, 3, 4, 5])
            >>> st.query(1, 3)
            9
        """
        if left < 0 or right >= self.size or left > right:
            raise ValueError(f"Invalid range [{left}, {right}]")

        return self._query(0, 0, self.size - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """Internal query method."""
        if right < start or left > end:
            return self.default_value

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_result = self._query(left_child, start, mid, left, right)
        right_result = self._query(right_child, mid + 1, end, left, right)

        return self.operation(left_result, right_result)

    def update(self, index: int, value: int) -> None:
        """
        Update element at given index.

        Args:
            index: Index to update (0-indexed)
            value: New value

        Examples:
            >>> st = SegmentTree([1, 2, 3, 4, 5])
            >>> st.update(2, 10)
            >>> st.query(2, 2)
            10
        """
        if index < 0 or index >= self.size:
            raise ValueError(f"Index {index} out of range")

        self.data[index] = value
        self._update(0, 0, self.size - 1, index, value)

    def _update(self, node: int, start: int, end: int, index: int, value: int) -> None:
        """Internal update method."""
        if start == end:
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


class LazySegmentTree:
    """
    Segment Tree with lazy propagation for range updates.

    Supports:
    - Range queries
    - Range updates
    - Lazy propagation for efficient range updates
    """

    def __init__(
        self,
        data: List[int],
        operation: Callable[[int, int], int] = None,
        default_value: int = 0,
    ):
        """
        Initialize Lazy Segment Tree.

        Args:
            data: Input array
            operation: Function to combine two values (default: addition)
            default_value: Default value for empty ranges
        """
        self.data = data.copy()
        self.size = len(data)
        self.operation = operation or (lambda x, y: x + y)
        self.default_value = default_value

        # Calculate tree size
        self.tree_size = 2 * (2 ** math.ceil(math.log2(self.size))) - 1
        self.tree = [self.default_value] * self.tree_size
        self.lazy = [0] * self.tree_size

        self._build(0, 0, self.size - 1)

    def _build(self, node: int, start: int, end: int) -> None:
        """Build the segment tree recursively."""
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self._build(left_child, start, mid)
            self._build(right_child, mid + 1, end)

            self.tree[node] = self.operation(
                self.tree[left_child], self.tree[right_child]
            )

    def _push_lazy(self, node: int, start: int, end: int) -> None:
        """Push lazy updates to children."""
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)

            if start != end:
                left_child = 2 * node + 1
                right_child = 2 * node + 2
                self.lazy[left_child] += self.lazy[node]
                self.lazy[right_child] += self.lazy[node]

            self.lazy[node] = 0

    def range_update(self, left: int, right: int, delta: int) -> None:
        """
        Update range from left to right by adding delta.

        Args:
            left: Left boundary (0-indexed)
            right: Right boundary (0-indexed)
            delta: Value to add to the range
        """
        if left < 0 or right >= self.size or left > right:
            raise ValueError(f"Invalid range [{left}, {right}]")

        self._range_update(0, 0, self.size - 1, left, right, delta)

    def _range_update(
        self, node: int, start: int, end: int, left: int, right: int, delta: int
    ) -> None:
        """Internal range update method."""
        self._push_lazy(node, start, end)

        if right < start or left > end:
            return

        if left <= start and end <= right:
            self.lazy[node] += delta
            self._push_lazy(node, start, end)
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self._range_update(left_child, start, mid, left, right, delta)
        self._range_update(right_child, mid + 1, end, left, right, delta)

        self._push_lazy(left_child, start, mid)
        self._push_lazy(right_child, mid + 1, end)

        self.tree[node] = self.operation(self.tree[left_child], self.tree[right_child])

    def query(self, left: int, right: int) -> int:
        """
        Query range from left to right.

        Args:
            left: Left boundary (0-indexed)
            right: Right boundary (0-indexed)

        Returns:
            Result of the operation over the range
        """
        if left < 0 or right >= self.size or left > right:
            raise ValueError(f"Invalid range [{left}, {right}]")

        return self._query(0, 0, self.size - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """Internal query method."""
        self._push_lazy(node, start, end)

        if right < start or left > end:
            return self.default_value

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_result = self._query(left_child, start, mid, left, right)
        right_result = self._query(right_child, mid + 1, end, left, right)

        return self.operation(left_result, right_result)


class MinSegmentTree(SegmentTree):
    """Segment Tree for range minimum queries."""

    def __init__(self, data: List[int]):
        super().__init__(data, min, float("inf"))


class MaxSegmentTree(SegmentTree):
    """Segment Tree for range maximum queries."""

    def __init__(self, data: List[int]):
        super().__init__(data, max, float("-inf"))


if __name__ == "__main__":
    # Example usage
    print("Segment Tree Example")
    print("=" * 50)

    # Create Segment Tree
    data = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(data)

    print(f"Original data: {data}")
    print(f"Tree size: {st.tree_size}")

    # Range sum queries
    print(f"\nRange sum queries:")
    queries = [(0, 2), (1, 4), (0, 5), (2, 3)]
    for left, right in queries:
        result = st.query(left, right)
        print(f"Sum from {left} to {right}: {result}")

    # Update element
    print(f"\nUpdating element at index 2 to 10:")
    st.update(2, 10)
    print(f"New data: {st.data}")
    print(f"Sum from 0 to 2: {st.query(0, 2)}")

    # Min Segment Tree
    print(f"\nMin Segment Tree Example")
    print("=" * 50)

    min_st = MinSegmentTree([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Original data: {min_st.data}")

    min_queries = [(0, 3), (2, 5), (0, 7)]
    for left, right in min_queries:
        result = min_st.query(left, right)
        print(f"Min from {left} to {right}: {result}")

    # Lazy Segment Tree
    print(f"\nLazy Segment Tree Example")
    print("=" * 50)

    lazy_st = LazySegmentTree([1, 2, 3, 4, 5])
    print(f"Original data: {lazy_st.data}")

    # Range update
    print(f"\nAdding 2 to range [1, 3]:")
    lazy_st.range_update(1, 3, 2)

    # Query after update
    print(f"Sum from 0 to 4: {lazy_st.query(0, 4)}")
    print(f"Sum from 1 to 3: {lazy_st.query(1, 3)}")

    # Another range update
    print(f"\nAdding 1 to range [0, 2]:")
    lazy_st.range_update(0, 2, 1)
    print(f"Sum from 0 to 4: {lazy_st.query(0, 4)}")

    print(f"\nSegment Tree implementation completed successfully!")
