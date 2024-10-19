class Node:
    def __init__(self, value=0):
        """
        Initialize a segment tree node.

        Args:
            value (int): The value of the node.
        """
        self.value = value
        self.left = None
        self.right = None


class PersistentSegmentTree:
    def __init__(self, arr):
        """
        Initialize the persistent segment tree with the given array.

        Args:
            arr (list): The initial array to build the segment tree.
        """
        self.n = len(arr)
        self.roots = []
        self.roots.append(self._build(arr, 0, self.n - 1))

    def _build(self, arr, start, end):
        """
        Recursively build the segment tree.

        Args:
            arr (list): The input array.
            start (int): The starting index of the segment.
            end (int): The ending index of the segment.

        Returns:
            Node: The root node of the segment tree for the current segment.
        """
        if start == end:
            return Node(arr[start])

        mid = (start + end) // 2
        node = Node()
        node.left = self._build(arr, start, mid)
        node.right = self._build(arr, mid + 1, end)
        node.value = node.left.value + node.right.value
        return node

    def update(self, version, index, value):
        """
        Update the value at the specified index in the specified version.

        Args:
            version (int): The version of the segment tree to update.
            index (int): The index to update.
            value (int): The new value to set at the index.

        Returns:
            int: The index of the new version of the root node.
        """
        new_root = self._update(self.roots[version], 0, self.n - 1, index, value)
        self.roots.append(new_root)
        return len(self.roots) - 1  # return the index of the new version

    def _update(self, node, start, end, index, value):
        """
        Recursively update the segment tree.

        Args:
            node (Node): The current node of the segment tree.
            start (int): The starting index of the segment.
            end (int): The ending index of the segment.
            index (int): The index to update.
            value (int): The new value to set at the index.

        Returns:
            Node: The new root node after the update.
        """
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

    def query(self, version, left, right):
        """
        Query the sum of values in the range [left, right] for the specified version.

        Args:
            version (int): The version of the segment tree to query.
            left (int): The left index of the range.
            right (int): The right index of the range.

        Returns:
            int: The sum of the values in the specified range.
        """
        return self._query(self.roots[version], 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        """
        Recursively query the segment tree.

        Args:
            node (Node): The current node of the segment tree.
            start (int): The starting index of the segment.
            end (int): The ending index of the segment.
            left (int): The left index of the range.
            right (int): The right index of the range.

        Returns:
            int: The sum of the values in the specified range.
        """
        if right < start or end < left:
            return 0  # out of range

        if left <= start and end <= right:
            return node.value  # completely within range

        mid = (start + end) // 2
        sum_left = self._query(node.left, start, mid, left, right)
        sum_right = self._query(node.right, mid + 1, end, left, right)
        return sum_left + sum_right


# Example usage and doctests
if __name__ == "__main__":
    import doctest

    # Creating an initial array
    arr = [1, 2, 3, 4, 5]
    pst = PersistentSegmentTree(arr)

    # Querying the initial version
    assert pst.query(0, 0, 4) == 15  # sum of [1, 2, 3, 4, 5]

    # Updating index 2 to value 10 in version 0
    new_version = pst.update(0, 2, 10)

    # Querying the updated version
    assert pst.query(new_version, 0, 4) == 22  # sum of [1, 2, 10, 4, 5]
    assert pst.query(0, 0, 4) == 15  # original version unchanged

