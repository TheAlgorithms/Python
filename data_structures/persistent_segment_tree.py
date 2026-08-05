from __future__ import annotations


class Node:
    def __init__(self, value: int = 0) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class PersistentSegmentTree:
    def __init__(self, arr: list[int]) -> None:
        self.n: int = len(arr)
        self.roots: list[Node] = []
        self.roots.append(self._build(arr, 0, self.n - 1))

    def _build(self, arr: list[int], start: int, end: int) -> Node:
        """
        Builds a segment tree from the provided array.

        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> root = pst._build([1, 2, 3, 4], 0, 3)
        >>> root.value  # Sum of the whole array
        10
        >>> root.left.value  # Sum of the left half
        3
        >>> root.right.value  # Sum of the right half
        7
        """
        if start == end:
            return Node(arr[start])
        mid = (start + end) // 2
        node = Node()
        node.left = self._build(arr, start, mid)
        node.right = self._build(arr, mid + 1, end)
        node.value = node.left.value + node.right.value
        return node

    def update(self, version: int, index: int, value: int) -> int:
        """
        Updates the value at the given index and returns the new version.

        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> version_1 = pst.update(0, 1, 5)  # Update index 1 to 5
        >>> pst.query(version_1, 0, 3)  # Query sum of all elements in new version
        13
        >>> pst.query(0, 0, 3)  # Original version remains unchanged
        10
        >>> version_2 = pst.update(version_1, 3, 6)  # Update index 3 to 6 in version_1
        >>> pst.query(version_2, 0, 3)  # Query sum of all elements in newest version
        15
        """
        new_root = self._update(self.roots[version], 0, self.n - 1, index, value)
        self.roots.append(new_root)
        return len(self.roots) - 1

    def _update(self, node: Node, start: int, end: int, index: int, value: int) -> Node:
        """
        Updates the node for the specified index and value and returns the new node.

        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> old_root = pst.roots[0]
        >>> new_root = pst._update(old_root, 0, 3, 1, 5)  # Update index 1 to 5
        >>> new_root.value  # New sum after update
        13
        >>> old_root.value  # Old root remains unchanged
        10
        >>> new_root.left.value  # Updated left child
        6
        >>> new_root.right.value  # Right child remains the same
        7
        """
        if start == end:
            return Node(value)

        mid = (start + end) // 2
        new_node = Node()

        if index <= mid:
            new_node.left = self._update(node.left, start, mid, index, value)
            new_node.right = node.right  # Ensure right node is the same as the original
        else:
            new_node.left = node.left  # Ensure left node is the same as the original
            new_node.right = self._update(node.right, mid + 1, end, index, value)

        new_node.value = new_node.left.value + (
            new_node.right.value if new_node.right else 0
        )

        return new_node

    def query(self, version: int, left: int, right: int) -> int:
        """
        Queries the sum in the given range for the specified version.

        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> pst.query(0, 0, 3)  # Sum of all elements in original version
        10
        >>> pst.query(0, 1, 2)  # Sum of elements at index 1 and 2 in original version
        5
        >>> version_1 = pst.update(0, 1, 5)  # Update index 1 to 5
        >>> pst.query(version_1, 0, 3)  # Sum of all elements in new version
        13
        >>> pst.query(version_1, 1, 2)  # Sum of elements at index 1 and 2
        8
        """
        return self._query(self.roots[version], 0, self.n - 1, left, right)

    def _query(self, node: Node, start: int, end: int, left: int, right: int) -> int:
        """
        Queries the sum of values in the range [left, right] for the given node.

        >>> pst = PersistentSegmentTree([1, 2, 3, 4])
        >>> root = pst.roots[0]
        >>> pst._query(root, 0, 3, 1, 2)  # Sum of elements at index 1 and 2
        5
        >>> pst._query(root, 0, 3, 0, 3)  # Sum of all elements
        10
        >>> pst._query(root, 0, 3, 2, 3)  # Sum of elements at index 2 and 3
        7
        """
        if node is None or left > end or right < start:
            return 0
        if left <= start and right >= end:
            return node.value
        mid = (start + end) // 2
        return self._query(node.left, start, mid, left, right) + self._query(
            node.right, mid + 1, end, left, right
        )


# Running the doctests
if __name__ == "__main__":
    import doctest

    print("Running doctests...")
    result = doctest.testmod()
    print(f"Ran {result.attempted} tests, {result.failed} failed.")
