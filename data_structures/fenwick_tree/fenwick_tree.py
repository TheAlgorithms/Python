"""Fenwick Tree (Binary Indexed Tree) Data Structure.

A Fenwick Tree is a data structure that can efficiently update elements
and calculate prefix sums in a table of numbers. It is also known as a
Binary Indexed Tree (BIT).

Time Complexity:
- Update: O(log n)
- Query (prefix sum): O(log n)
- Construction: O(n log n)

Space Complexity: O(n)
"""


class FenwickTree:
    """Fenwick Tree implementation for range sum queries.

    This implementation supports efficient prefix sum queries and point updates.
    The tree uses 1-based indexing internally for simpler implementation.

    Attributes:
        size: Size of the input array
        tree: List storing the Fenwick tree values

    >>> ft = FenwickTree(5)
    >>> ft.update(0, 3)
    >>> ft.update(1, 2)
    >>> ft.update(2, 5)
    >>> ft.update(3, 1)
    >>> ft.update(4, 4)
    >>> ft.prefix_sum(2)
    10
    >>> ft.range_sum(1, 3)
    8
    >>> ft2 = FenwickTree([1, 3, 5, 7, 9])
    >>> ft2.prefix_sum(2)
    9
    >>> ft2.range_sum(1, 3)
    15
    """

    def __init__(self, size_or_array: int | list[int]) -> None:
        """Initialize Fenwick Tree.

        Args:
            size_or_array: Either size of array (int) or initial array values (list)

        >>> ft = FenwickTree(5)
        >>> len(ft.tree)
        6
        >>> ft2 = FenwickTree([1, 2, 3])
        >>> ft2.prefix_sum(2)
        6
        """
        if isinstance(size_or_array, int):
            self.size = size_or_array
            self.tree = [0] * (self.size + 1)  # 1-indexed
        else:
            self.size = len(size_or_array)
            self.tree = [0] * (self.size + 1)
            for i, val in enumerate(size_or_array):
                self.update(i, val)

    def update(self, index: int, delta: int) -> None:
        """Add delta to element at given index.

        Args:
            index: Index to update (0-based)
            delta: Value to add to the element

        >>> ft = FenwickTree(5)
        >>> ft.update(0, 5)
        >>> ft.prefix_sum(0)
        5
        >>> ft.update(0, 3)
        >>> ft.prefix_sum(0)
        8
        """
        index += 1  # Convert to 1-based indexing
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)  # Add last set bit

    def prefix_sum(self, index: int) -> int:
        """Calculate sum of elements from 0 to index (inclusive).

        Args:
            index: End index for prefix sum (0-based, inclusive)

        Returns:
            Sum of elements from index 0 to given index

        >>> ft = FenwickTree([1, 2, 3, 4, 5])
        >>> ft.prefix_sum(0)
        1
        >>> ft.prefix_sum(2)
        6
        >>> ft.prefix_sum(4)
        15
        """
        index += 1  # Convert to 1-based indexing
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & (-index)  # Remove last set bit
        return result

    def range_sum(self, left: int, right: int) -> int:
        """Calculate sum of elements in range [left, right].

        Args:
            left: Left boundary of range (0-based, inclusive)
            right: Right boundary of range (0-based, inclusive)

        Returns:
            Sum of elements in the given range

        >>> ft = FenwickTree([1, 2, 3, 4, 5])
        >>> ft.range_sum(0, 2)
        6
        >>> ft.range_sum(2, 4)
        12
        >>> ft.range_sum(1, 1)
        2
        """
        if left == 0:
            return self.prefix_sum(right)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def set_value(self, index: int, value: int) -> None:
        """Set element at index to given value.

        Args:
            index: Index to set (0-based)
            value: New value to set

        >>> ft = FenwickTree([1, 2, 3, 4, 5])
        >>> ft.set_value(2, 10)
        >>> ft.prefix_sum(2)
        13
        >>> ft.range_sum(2, 2)
        10
        """
        current_value = self.range_sum(index, index)
        delta = value - current_value
        self.update(index, delta)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
