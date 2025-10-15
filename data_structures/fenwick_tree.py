"""
Fenwick Tree (Binary Indexed Tree) implementation.

A Fenwick Tree is a data structure that can efficiently update elements
and calculate prefix sums in a table of numbers. It supports two main
operations:
1. Update an element at a given index
2. Query the sum of elements from index 1 to a given index

Time Complexity:
    - Update: O(log n)
    - Query: O(log n)
Space Complexity: O(n)

Reference: https://en.wikipedia.org/wiki/Fenwick_tree
"""

from typing import Optional


class FenwickTree:
    """
    Fenwick Tree implementation for efficient range sum queries and updates.

    Attributes:
        tree: Internal array representing the Fenwick Tree
        size: Size of the tree
    """

    def __init__(self, size: int):
        """
        Initialize Fenwick Tree with given size.

        Args:
            size: Size of the tree (1-indexed)

        Examples:
            >>> ft = FenwickTree(10)
            >>> ft.size
            10
        """
        self.size = size
        self.tree = [0] * (size + 1)  # 1-indexed

    def update(self, index: int, delta: int) -> None:
        """
        Update element at given index by adding delta.

        Args:
            index: 1-indexed position to update
            delta: Value to add to the element

        Examples:
            >>> ft = FenwickTree(5)
            >>> ft.update(1, 5)
            >>> ft.query(1)
            5
        """
        if index < 1 or index > self.size:
            msg = f"Index {index} out of range [1, {self.size}]"
            raise ValueError(msg)

        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)  # Add least significant bit

    def query(self, index: int) -> int:
        """
        Query sum from index 1 to given index (inclusive).

        Args:
            index: 1-indexed position to query up to

        Returns:
            Sum of elements from index 1 to index

        Examples:
            >>> ft = FenwickTree(5)
            >>> ft.update(1, 3)
            >>> ft.update(2, 4)
            >>> ft.query(2)
            7
        """
        if index < 1 or index > self.size:
            msg = f"Index {index} out of range [1, {self.size}]"
            raise ValueError(msg)

        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & (-index)  # Remove least significant bit

        return result

    def range_query(self, left: int, right: int) -> int:
        """
        Query sum from left to right (inclusive).

        Args:
            left: 1-indexed left boundary
            right: 1-indexed right boundary

        Returns:
            Sum of elements from left to right

        Examples:
            >>> ft = FenwickTree(5)
            >>> ft.update(1, 1)
            >>> ft.update(2, 2)
            >>> ft.update(3, 3)
            >>> ft.range_query(2, 3)
            5
        """
        if left < 1 or right > self.size or left > right:
            msg = f"Invalid range [{left}, {right}]"
            raise ValueError(msg)

        return self.query(right) - self.query(left - 1)

    def get(self, index: int) -> int:
        """
        Get value at given index.

        Args:
            index: 1-indexed position

        Returns:
            Value at the given index

        Examples:
            >>> ft = FenwickTree(5)
            >>> ft.update(1, 5)
            >>> ft.get(1)
            5
        """
        return self.range_query(index, index)

    def set_value(self, index: int, value: int) -> None:
        """
        Set value at given index.

        Args:
            index: 1-indexed position
            value: New value to set

        Examples:
            >>> ft = FenwickTree(5)
            >>> ft.set_value(1, 10)
            >>> ft.get(1)
            10
        """
        current_value = self.get(index)
        delta = value - current_value
        self.update(index, delta)

    def clear(self) -> None:
        """Clear all values in the tree."""
        self.tree = [0] * (self.size + 1)

    def __len__(self) -> int:
        """Return the size of the tree."""
        return self.size

    def __repr__(self) -> str:
        """String representation of the Fenwick Tree."""
        return f"FenwickTree(size={self.size})"


class FenwickTree2D:
    """
    2D Fenwick Tree for 2D range sum queries and updates.

    Supports:
    - Update element at (row, col)
    - Query sum from (1, 1) to (row, col)
    - Query sum in rectangle from (r1, c1) to (r2, c2)
    """

    def __init__(self, rows: int, cols: int):
        """
        Initialize 2D Fenwick Tree.

        Args:
            rows: Number of rows
            cols: Number of columns
        """
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, row: int, col: int, delta: int) -> None:
        """
        Update element at (row, col) by adding delta.

        Args:
            row: Row index (1-indexed)
            col: Column index (1-indexed)
            delta: Value to add
        """
        if row < 1 or row > self.rows or col < 1 or col > self.cols:
            msg = f"Position ({row}, {col}) out of range"
            raise ValueError(msg)

        i = row
        while i <= self.rows:
            j = col
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def query(self, row: int, col: int) -> int:
        """
        Query sum from (1, 1) to (row, col).

        Args:
            row: Row index (1-indexed)
            col: Column index (1-indexed)

        Returns:
            Sum from (1, 1) to (row, col)
        """
        if row < 1 or row > self.rows or col < 1 or col > self.cols:
            msg = f"Position ({row}, {col}) out of range"
            raise ValueError(msg)

        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)

        return result

    def range_query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        Query sum in rectangle from (r1, c1) to (r2, c2).

        Args:
            r1: Top-left row (1-indexed)
            c1: Top-left column (1-indexed)
            r2: Bottom-right row (1-indexed)
            c2: Bottom-right column (1-indexed)

        Returns:
            Sum in the rectangle
        """
        return (
            self.query(r2, c2)
            - self.query(r1 - 1, c2)
            - self.query(r2, c1 - 1)
            + self.query(r1 - 1, c1 - 1)
        )


if __name__ == "__main__":
    # Example usage
    print("Fenwick Tree Example")
    print("=" * 50)

    # Create Fenwick Tree
    ft = FenwickTree(10)

    # Add some values
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, val in enumerate(values, 1):
        ft.update(i, val)
        print(f"Added {val} at position {i}")

    print("\nPrefix sums:")
    for i in range(1, 11):
        prefix_sum = ft.query(i)
        print(f"Sum from 1 to {i}: {prefix_sum}")

    print("\nRange queries:")
    ranges = [(2, 5), (1, 10), (3, 7)]
    for left, right in ranges:
        range_sum = ft.range_query(left, right)
        print(f"Sum from {left} to {right}: {range_sum}")

    print("\nIndividual values:")
    for i in range(1, 11):
        value = ft.get(i)
        print(f"Value at position {i}: {value}")

    # Test update
    print("\nUpdating position 3 by adding 5:")
    ft.update(3, 5)
    print(f"New value at position 3: {ft.get(3)}")
    print(f"New prefix sum from 1 to 3: {ft.query(3)}")

    # 2D Fenwick Tree example
    print("\n2D Fenwick Tree Example")
    print("=" * 50)

    ft2d = FenwickTree2D(3, 3)

    # Add some values
    matrix_values = [
        (1, 1, 1),
        (1, 2, 2),
        (1, 3, 3),
        (2, 1, 4),
        (2, 2, 5),
        (2, 3, 6),
        (3, 1, 7),
        (3, 2, 8),
        (3, 3, 9),
    ]

    for row, col, val in matrix_values:
        ft2d.update(row, col, val)
        print(f"Added {val} at position ({row}, {col})")

    print("\n2D Range queries:")
    queries = [
        (1, 1, 2, 2),  # Top-left 2x2
        (2, 2, 3, 3),  # Bottom-right 2x2
        (1, 1, 3, 3),  # Entire matrix
    ]

    for r1, c1, r2, c2 in queries:
        result = ft2d.range_query(r1, c1, r2, c2)
        print(f"Sum from ({r1}, {c1}) to ({r2}, {c2}): {result}")

    print("\nFenwick Tree implementation completed successfully!")
