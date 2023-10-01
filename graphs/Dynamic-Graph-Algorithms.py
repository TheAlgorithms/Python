class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class DynamicConnectivity:
    def __init__(self, n):
        self.uf = UnionFind(n)
        self.removed = [False] * n

    def add_edge(self, u, v):
        if not self.removed[u]:
            self.uf.union(u, v)

    def remove_edge(self, u, v):
        if not self.removed[u] and self.uf.find(u) == self.uf.find(v):
            self.removed[u] = True

    def are_connected(self, u, v):
        return not self.removed[u] and self.uf.find(u) == self.uf.find(v)


if __name__ == "__main__":
    n = 5
    dc = DynamicConnectivity(n)

    dc.add_edge(0, 1)
    dc.add_edge(1, 2)
    dc.add_edge(3, 4)

    print(dc.are_connected(0, 2))  # True
    print(dc.are_connected(0, 3))  # False

    dc.remove_edge(0, 1)
    print(dc.are_connected(0, 2))  # False
