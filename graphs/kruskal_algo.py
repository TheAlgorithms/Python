class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        if root_u != (root_v := self.find(v)):
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_algorithm(vertices, edges):
    # Step 1: Sort edges based on weight
    edges.sort(key=lambda x: x[2])

    # Step 2: Initialize Disjoint Set
    ds = DisjointSet(vertices)

    mst = []
    mst_weight = 0

    # Step 3: Iterate through sorted edges
    for u, v, weight in edges:
        # Check if adding this edge creates a cycle
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight


# Example usage:
vertices = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

mst, total_weight = kruskal_algorithm(vertices, edges)
print("Edges in the MST:", mst)
print("Total weight of the MST:", total_weight)
