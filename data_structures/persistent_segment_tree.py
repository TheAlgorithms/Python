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
        """
        new_root = self._update(self.roots[version], 0, self.n - 1, index, value)
        self.roots.append(new_root)
        return len(self.roots) - 1

    def _update(
        self, node: Node | None, start: int, end: int, index: int, value: int
    ) -> Node:
        """
        Updates the node for the specified index and value and returns the new node.
        """
        if node is None:  # Handle the None case
            node = Node()  # Create a new node if None

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
        """
        return self._query(self.roots[version], 0, self.n - 1, left, right)

    def _query(
        self, node: Node | None, start: int, end: int, left: int, right: int
    ) -> int:
        """
        Queries the sum of values in the range [left, right] for the given node.
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
