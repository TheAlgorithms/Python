class DisjointSet:
    def __init__(self, set_sizes: list[int]) -> None:
        """
        Initialize a disjoint set data structure with set sizes.

        Examples:
        >>> d = DisjointSet([1, 2, 3, 4])
        >>> d.find(0)
        0
        >>> d.find(1)
        1
        >>> d.find(2)
        2
        >>> d.find(3)
        3
        """
        self.set_sizes = set_sizes
        self.parents = {i: i for i in range(len(set_sizes))}
        self.ranks = [0] * len(set_sizes)

    def find(self, x: int) -> int:
        """
        Find the representative of the set containing x, with path compression.

        Examples:
        >>> d = DisjointSet([1, 2, 3, 4])
        >>> d.find(0)
        0
        >>> d.union(0, 1)
        True
        >>> d.find(1)
        0
        >>> d.find(0)
        0
        >>> d.union(2, 3)
        True
        >>> d.find(2)
        2
        >>> d.union(1, 2)
        True
        >>> d.find(1)
        0
        >>> d.find(2)
        0
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        """
        Merge the sets containing x and y using union by rank.

        Examples:
        >>> d = DisjointSet([1, 2, 3, 4])
        >>> d.union(0, 1)
        True
        >>> d.find(0) == d.find(1)
        True
        >>> d.union(2, 3)
        True
        >>> d.find(2) == d.find(3)
        True
        >>> d.union(1, 2)
        True
        >>> d.find(0) == d.find(1) == d.find(2) == d.find(3)
        True
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.ranks[x_root] < self.ranks[y_root]:
            x_root, y_root = y_root, x_root

        self.parents[y_root] = x_root
        self.set_sizes[x_root] += self.set_sizes[y_root]

        if self.ranks[x_root] == self.ranks[y_root]:
            self.ranks[x_root] += 1

        return True
