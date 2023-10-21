"""
Intuition
1. Edge Calculation: The code starts by calculating all possible edges between the given points. It iterates through the points and computes the Manhattan distance (L1 distance) between each pair of points. These distances represent the cost of connecting each pair of points directly. The resulting list of edges contains information about which points are connected and the cost associated with each connection.

2. Edge Sorting: After calculating all edges,the code sorts them in ascending order based on their costs. This step is essential for Kruskal's algorithm,which aims to build a minimum spanning tree by adding edges in increasing order of cost.

3. Kruskal's Algorithm: The core of the code is Kruskal's algorithm,a greedy algorithm for finding the minimum spanning tree of a graph. The algorithm processes edges in ascending order of cost while ensuring that adding an edge does not create a cycle in the tree. The minimum spanning tree is a subset of the edges that connect all the points with the minimum possible total cost.

4. Union−FindDataStructure:Union-Find Data Structure:Union−FindDataStructure: To efficiently detect and prevent cycles when adding edges,the code uses a union-find (disjoint-set) data structure. The parent array keeps track of the parent node for each point,and the rank array is used to maintain the depth of each node in the tree. The find operation finds the representative (root) of the set to which a point belongs,and the union operation merges two sets by updating their representatives and ranks.

5. AddingEdgestotheMinimumSpanningTreeAdding Edges to the Minimum Spanning TreeAddingEdgestotheMinimumSpanningTree: The code iterates through the sorted edges and adds them to the minimum spanning tree if adding the edge does not create a cycle (i.e.,if the endpoints of the edge are not already in the same set). This process continues until the minimum spanning tree contains exactly n - 1 edges,where n is the number of points. At this point,the algorithm has connected all points with the minimum total cost.

6. Minimum Cost Calculation: The code keeps track of the sum of edge costs as edges are added to the minimum spanning tree. This sum represents the minimum cost to connect all the given points.

Complexity
Time complexity: O(n^2 * log(n))
Space complexity: O(n^2)

"""
from typing import List


class Solution:
    def mincost(self, points: List[List[int]]) -> int:
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
