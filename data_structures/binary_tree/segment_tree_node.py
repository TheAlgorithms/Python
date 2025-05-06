class Node:
    def __init__(self, start: int, end: int) -> None:
        # Initializes a segment tree node with start and end indices
        self.start = start
        self.end = end
        self.value: int = 0
        self.left: Node = self
        self.right: Node = self


class SegmentTree:
    def __init__(self, nums: list[int], mode: str = "max") -> None:
        """
        Initializes the Segment Tree.
        :param nums: List of integers to build the tree from.
        :param mode: Operation mode of the tree ('max' or 'sum').
        """
        self.size = len(nums)
        self.mode = mode
        if mode not in {"max", "sum"}:
            self.mode = "max"  # Default to max if invalid mode is given

        # Build the tree from the input list
        self.root: Node = self.build(0, self.size - 1, nums)

    def build(self, start: int, end: int, nums: list[int]) -> Node:
        """
        Recursively builds the segment tree.
        :param start: Start index of the segment.
        :param end: End index of the segment.
        :param nums: Original input array.
        :return: Root node of the constructed subtree.

        >>> tree = SegmentTree([1, 2, 3, 4, 5], mode="max")
        >>> tree.root.value
        5
        """
        if start > end:
            return Node(0, 0)

        if start == end:
            # Leaf node
            n = Node(start, end)
            n.value = nums[start]
            return n

        mid = (start + end) // 2
        root = Node(start, end)
        root.left = self.build(start, mid, nums)
        root.right = self.build(mid + 1, end, nums)

        # Set the value according to the mode
        if self.mode == "max":
            root.value = max(root.left.value, root.right.value)
        else:
            root.value = root.left.value + root.right.value

        return root

    def max_in_range(self, start_index: int, end_index: int) -> int:
        """
        Queries the maximum value in a given range.
        Only works in 'max' mode.

        >>> tree = SegmentTree([1, 2, 3, 4, 5], mode="max")
        >>> tree.max_in_range(1, 3)
        4
        """
        if self.mode == "sum":
            raise Exception("Current Segment Tree doesn't support finding max")

        if start_index > end_index or start_index < 0 or end_index >= self.size:
            raise Exception("Invalid index")

        if self.root is None:
            raise ValueError("Tree not initialized")

        return self.query(self.root, start_index, end_index, 0, self.size - 1)

    def sum_in_range(self, start_index: int, end_index: int) -> int:
        """
        Queries the sum of values in a given range.
        Only works in 'sum' mode.

        >>> tree = SegmentTree([1, 2, 3, 4, 5], mode="sum")
        >>> tree.sum_in_range(1, 3)
        9
        """
        if self.mode == "max":
            raise Exception("Current Segment Tree doesn't support summing")

        if start_index > end_index or start_index < 0 or end_index >= self.size:
            raise Exception("Invalid index")

        if self.root is None:
            raise ValueError("Tree not initialized")

        return self.query(self.root, start_index, end_index, 0, self.size - 1)

    def query(
        self, node: Node, start_index: int, end_index: int, start: int, end: int
    ) -> int:
        """
        Recursively queries a value (max or sum) in a given range.
        :param node: Current node in the tree.
        :param start_index: Query start index.
        :param end_index: Query end index.
        :param start: Node's segment start.
        :param end: Node's segment end.
        :return: Result of query in the range.

        >>> tree = SegmentTree([1, 2, 3, 4, 5], mode="max")
        >>> tree.query(tree.root, 1, 3, 0, 4)
        4
        """
        # Complete overlap
        if start_index <= start and end <= end_index:
            return node.value

        mid = (start + end) // 2

        if end_index <= mid:
            # Entire range is in the left child
            return self.query(node.left, start_index, end_index, start, mid)
        elif start_index > mid:
            # Entire range is in the right child
            return self.query(node.right, start_index, end_index, mid + 1, end)
        elif self.mode == "max":
            return max(
                self.query(node.left, start_index, end_index, start, mid),
                self.query(node.right, start_index, end_index, mid + 1, end),
            )
        else:
            return self.query(
                node.left, start_index, end_index, start, mid
            ) + self.query(node.right, start_index, end_index, mid + 1, end)

    def update(self, index: int, new_value: int) -> None:
        """
        Updates a value at a specific index in the segment tree.
        :param index: Index to update.
        :param new_value: New value to set.

        >>> tree = SegmentTree([1, 2, 3, 4, 5], mode="max")
        >>> tree.update(2, 6)
        >>> tree.max_in_range(1, 3)
        6
        """
        if index < 0 or index >= self.size:
            raise Exception("Invalid index")

        self.modify(self.root, index, new_value, 0, self.size - 1)

    def modify(
        self, node: Node, index: int, new_value: int, start: int, end: int
    ) -> None:
        """
        Recursively updates the tree to reflect a change at a specific index.
        :param node: Current node being processed.
        :param index: Index to update.
        :param new_value: New value to assign.
        :param start: Start index of node's segment.
        :param end: End index of node's segment.

        >>> tree = SegmentTree([1, 2, 3, 4, 5], mode="max")
        >>> tree.modify(tree.root, 2, 6, 0, 4)
        >>> tree.max_in_range(0, 4)
        6
        """
        if start == end:
            node.value = new_value
            return

        mid = (start + end) // 2

        if index <= mid:
            self.modify(node.left, index, new_value, start, mid)
        else:
            self.modify(node.right, index, new_value, mid + 1, end)

        # Recompute current node's value after update
        if self.mode == "max":
            node.value = max(node.left.value, node.right.value)
        else:
            node.value = node.left.value + node.right.value
