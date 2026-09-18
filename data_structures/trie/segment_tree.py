"""
A Segment Tree is a binary tree used for storing intervals or segments.
It allows querying the sum, minimum, or maximum of elements in a range efficiently.

Time Complexity:
- Build: O(n)
- Query: O(log n)
- Update: O(log n)
"""


class SegmentTree:
    def __init__(self, data: list[int]) -> None:
        """
        Initializes the Segment Tree from a list of integers.
        :param data: List of integer elements.
        :return: None
        """
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data: list[int], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node + 1, start, mid)
            self._build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index: int, value: int) -> None:
        """
        Updates the value at the given index and updates the tree.
        :param index: Index to update.
        :param value: New value.
        :return: None
        """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node: int, start: int, end: int, index: int, value: int) -> None:
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self._update(2 * node + 1, start, mid, index, value)
            else:
                self._update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left: int, right: int) -> int:
        """
        Returns the sum of elements in the range [left, right].
        :param left: Left index (inclusive).
        :param right: Right index (inclusive).
        :return: Sum of the range.

        >>> data = [1, 2, 3, 4, 5]
        >>> st = SegmentTree(data)
        >>> st.query(1, 3)
        9
        >>> st.update(2, 10)
        >>> st.query(1, 3)
        16
        """
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self._query(2 * node + 1, start, mid, left, right) + self._query(
            2 * node + 2, mid + 1, end, left, right
        )


def test_segment_tree() -> bool:
    data = [1, 2, 3, 4, 5]
    st = SegmentTree(data)
    assert st.query(0, 2) == 6
    assert st.query(1, 4) == 14
    st.update(2, 10)
    assert st.query(1, 3) == 16
    assert st.query(0, 4) == 22
    return True


def print_results(msg: str, passes: bool) -> None:
    print(str(msg), "works!" if passes else "doesn't work :(")


def pytests() -> None:
    assert test_segment_tree()


def main() -> None:
    """
    >>> pytests()
    """
    print_results("Testing Segment Tree functionality", test_segment_tree())


if __name__ == "__main__":
    main()
