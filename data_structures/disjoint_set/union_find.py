"""
Union-Find (Disjoint Set Union) with Path Compression and Union by Rank

Use Case:
- Efficient structure to manage disjoint sets
- Useful in network connectivity, Kruskal's MST, and clustering

Time Complexity:
- Nearly constant: O(α(n)) where α is the inverse Ackermann function

Author: Michael Alexander Montoya
"""


class UnionFind:
    def __init__(self, size: int) -> None:
        """
        Initializes a Union-Find data structure with `size` elements.

        >>> uf = UnionFind(5)
        >>> uf.find(0)
        0
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        """
        Finds the representative/root of the set that `node` belongs to.

        >>> uf = UnionFind(5)
        >>> uf.find(3)
        3
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node_a: int, node_b: int) -> bool:
        """
        Unites the sets that contain elements `node_a` and `node_b`.

        >>> uf = UnionFind(5)
        >>> uf.union(0, 1)
        True
        >>> uf.find(1) == uf.find(0)
        True
        >>> uf.union(0, 1)
        False
        """
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a == root_b:
            return False  # Already connected

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)

    print("1 and 3 connected:", uf.find(1) == uf.find(3))  # True
    print("1 and 5 connected:", uf.find(1) == uf.find(5))  # False

    uf.union(3, 5)

    print("1 and 5 connected after union:", uf.find(1) == uf.find(5))  # True
