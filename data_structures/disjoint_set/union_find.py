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
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  # Already connected

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True


# Example usage
if __name__ == "__main__":
    uf = UnionFind(10)

    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)

    print("1 and 3 connected:", uf.find(1) == uf.find(3))  # True
    print("1 and 5 connected:", uf.find(1) == uf.find(5))  # False

    uf.union(3, 5)

    print("1 and 5 connected after union:", uf.find(1) == uf.find(5))  # True
