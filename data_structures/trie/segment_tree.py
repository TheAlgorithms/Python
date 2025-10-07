"""
A Segment Tree is a binary tree data structure used for efficiently answering
range queries and updates on an array, such as sum, minimum, or maximum over
a subrange. It offers O(log n) time complexity for both queries and updates,
making it very efficient compared to a naive O(n) approach.

While building the tree takes O(n) time and the tree requires O(n) space,
this preprocessing enables fast range queries that would otherwise be slow.
Segment Trees are especially useful when the array is mutable and queries
and updates are intermixed.

Time Complexity:
- Build: O(n)
- Query: O(log n)
- Update: O(log n)

Example usage and doctests:

>>> data = [1, 2, 3, 4, 5]
>>> st = SegmentTree(data)
>>> st.query(1, 4)
9
>>> st.update(2, 10)
>>> st.query(1, 4)
16
"""


class SegmentTree:
    """Segment Tree for efficient range sum queries."""

    def __init__(self, data: list[int]):
        """Initialize the segment tree with the input data.

        Args:
            data (list[int]): List of integers to build the segment tree.
        """
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index: int, value: int) -> None:
        """Update element at index with a new value.

        Args:
            index (int): Index of the element to update.
            value (int): New value to set at the given index.
        """
        if index < 0 or index >= self.n:
            raise ValueError("Index out of bounds")
        index += self.n
        self.tree[index] = value
        while index > 1:
            index >>= 1
            self.tree[index] = self.tree[index << 1] + self.tree[index << 1 | 1]

    def query(self, left: int, right: int) -> int:
        """Compute the sum of elements in the interval [left, right).

        Args:
            left (int): Left index (inclusive).
            right (int): Right index (exclusive).

        Returns:
            int: Sum of elements from left to right-1.

        Raises:
            ValueError: If indices are out of bounds or left >= right.
        """
        if left < 0 or right > self.n or left >= right:
            raise ValueError("Invalid query range")
        res = 0
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res


if __name__ == "__main__":
    import doctest

    data = [1, 2, 3, 4, 5]
    st = SegmentTree(data)
    print("Initial sum 1-4:", st.query(1, 4))
    st.update(2, 10)
    print("Updated sum 1-4:", st.query(1, 4))

    doctest.testmod()
