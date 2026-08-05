"""
Implementation of the Dancing Links algorithm (Algorithm X) by Donald Knuth.

>>> universe = [1, 2, 3, 4, 5, 6, 7]
>>> subsets = [
...     [1, 4, 7],
...     [1, 4],
...     [4, 5, 7],
...     [3, 5, 6],
...     [2, 3, 6, 7],
... ]
>>> dlx = DancingLinks(universe, subsets)
>>> sols = dlx.solve()
>>> len(sols) == 0
True
"""


class DLXNode:
    """Represents a node in the Dancing Links structure."""

    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None


class ColumnNode(DLXNode):
    """Represents a column header node, keeping track of its column size."""

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.size = 0


class DancingLinks:
    """Dancing Links structure for solving the Exact Cover problem."""

    def __init__(self, universe, subsets):
        self.header = ColumnNode("header")
        self.columns = {}
        self.solution = []
        self.solutions = []

        # Create column headers for each element in the universe
        prev = self.header
        for u in universe:
            col = ColumnNode(u)
            self.columns[u] = col
            col.left, col.right = prev, self.header
            prev.right = col
            self.header.left = col
            prev = col

        # Add rows (subsets)
        for subset in subsets:
            first_node = None
            for item in subset:
                col = self.columns[item]
                node = DLXNode()
                node.column = col

                # Insert node into column
                node.down = col
                node.up = col.up
                col.up.down = node
                col.up = node
                col.size += 1

                # Link nodes in the same row
                if first_node is None:
                    first_node = node
                else:
                    node.left = first_node.left
                    node.right = first_node
                    first_node.left.right = node
                    first_node.left = node

    def _cover(self, col):
        """Covers a column (removes it from the matrix)."""
        col.right.left = col.left
        col.left.right = col.right
        row = col.down
        while row != col:
            node = row.right
            while node != row:
                node.down.up = node.up
                node.up.down = node.down
                node.column.size -= 1
                node = node.right
            row = row.down

    def _uncover(self, col):
        """Uncovers a column (reverses _cover)."""
        row = col.up
        while row != col:
            node = row.left
            while node != row:
                node.column.size += 1
                node.down.up = node
                node.up.down = node
                node = node.left
            row = row.up
        col.right.left = col
        col.left.right = col

    def _choose_column(self):
        """Select the column with the smallest size (heuristic)."""
        min_size = float("inf")
        chosen = None
        col = self.header.right
        while col != self.header:
            if col.size < min_size:
                min_size = col.size
                chosen = col
            col = col.right
        return chosen

    def _search(self):
        """Recursive Algorithm X search."""
        if self.header.right == self.header:
            # All columns covered -> valid solution
            self.solutions.append([node.column.name for node in self.solution])
            return

        col = self._choose_column()
        if col is None:
            return

        self._cover(col)

        row = col.down
        while row != col:
            self.solution.append(row)

            node = row.right
            while node != row:
                self._cover(node.column)
                node = node.right

            self._search()

            # Backtrack
            self.solution.pop()
            node = row.left
            while node != row:
                self._uncover(node.column)
                node = node.left

            row = row.down

        self._uncover(col)

    def solve(self):
        """Find all exact cover solutions."""
        self._search()
        return self.solutions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
