class Node:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.left = None
        self.right = None


class PersistentSegmentTree:
    def __init__(self, arr: list[int]) -> None:
        self.n = len(arr)
        self.roots: list[Node] = []
        self.roots.append(self._build(arr, 0, self.n - 1))

    def _build(self, arr: list[int], start: int, end: int) -> Node:
        """
        Builds a segment tree from the provided array.

        >>> pst = PersistentSegmentTree([1, 2, 3])
        >>> root = pst._build([1, 2, 3], 0, 2)
        >>> root.value  # Sum of the whole array
        6
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
        Updates the segment tree with a new value at the specified index.

        >>> pst = PersistentSegmentTree([1, 2, 3])
        >>> version_1 = pst.update(0, 1, 5)
        >>> pst.query(version_1, 0, 2)  # Query sum from index 0 to 2
        9
        """
        new_root = self._update(self.roots[version], 0, self.n - 1, index, value)
        self.roots.append(new_root)
        return len(self.roots) - 1  # return the index of the new version

    def _update(self, node: Node, start: int, end: int, index: int, value: int) -> Node:
        if start == end:
            new_node = Node(value)
            return new_node
        mid = (start + end) // 2
        new_node = Node()
        if index <= mid:
            new_node.left = self._update(node.left, start, mid, index, value)
            new_node.right = node.right
        else:
            new_node.left = node.left
            new_node.right = self._update(node.right, mid + 1, end, index, value)
        new_node.value = new_node.left.value + new_node.right.value
        return new_node

    def query(self, version: int, left: int, right: int) -> int:
        """
        Queries the sum in the given range for the specified version.

        >>> pst = PersistentSegmentTree([1, 2, 3])
        >>> version_1 = pst.update(0, 1, 5)
        >>> pst.query(version_1, 0, 1)  # Query sum from index 0 to 1
        6
        >>> pst.query(version_1, 0, 2)  # Query sum from index 0 to 2
        9
        """
        return self._query(self.roots[version], 0, self.n - 1, left, right)

    def _query(self, node: Node, start: int, end: int, left: int, right: int) -> int:
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return node.value
        mid = (start + end) // 2
        return (self._query(node.left, start, mid, left, right) +
                self._query(node.right, mid + 1, end, left, right))
