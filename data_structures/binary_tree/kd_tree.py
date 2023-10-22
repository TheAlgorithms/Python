class MinimumCostCalculator:
    def calculate_min_cost(self, points) -> int:
        """
        Calculate the minimum cost to connect all points using the Manhattan distance.

        Args:
            points (List[List[int]]): A list of points represented as [x, y] coordinates.

        Returns:
            int: The minimum cost to connect all points.

        Example:
        >>> calculator = MinimumCostCalculator()
        >>> calculator.calculate_min_cost([[0, 0], [2, 2], [3, 1], [4, 5], [1, 4]])
        10
        """

        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent: List[int], rank: List[int], u: int, v: int) -> None:
            """
            Unite two sets by linking their roots based on rank.

            Args:
                parent (List[int]): A list representing the parent of each element.
                rank (List[int]): A list representing the rank of each element.
                u (int): The first element to be united.
                v (int): The second element to be united.
            """
            root_u = find(parent, u)
            if root_u != (root_v := find(parent, v)):
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1

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


# Define test cases
test_cases = [
    ([[0, 0], [2, 2], [3, 1], [4, 5], [1, 4]], 10),
    # Add more test cases here
]

# Run tests
for points, expected_result in test_cases:
    calculator = MinimumCostCalculator()
    result = calculator.calculate_min_cost(points)
    assert result == expected_result, f"Test failed: {result} != {expected_result}"
print("All tests passed")
