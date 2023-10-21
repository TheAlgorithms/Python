class Solution:
    def mincost(self, points):
        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            if root_x != (root_y := find(parent, y)):
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = manhattan_distance(points[i], points[j])
                edges.append((i, j, cost))
        edges.sort(key=lambda x: x[2])
        parent = list(range(n))
        rank = [0] * n
        min_cost = 0
        edges_added = 0
        for edge in edges:
            u, v, cost = edge
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                min_cost += cost
                edges_added += 1
                if edges_added == n - 1:
                    break
        return min_cost

points = [[0, 0], [2, 2], [3, 1], [4, 5], [1, 4]]
solution = Solution()
result = solution.mincost(points)
print("Minimum Cost:", result)
