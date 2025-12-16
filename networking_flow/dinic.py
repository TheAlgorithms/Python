"""
Dinic's Algorithm for Maximum Flow Problem.
Refined by Even and Itai for efficient blocking flow computation.

Description:
    The algorithm computes the maximum flow in a flow network.
    It constructs a level graph using BFS and then finds a blocking flow
    using DFS (incorporating the logic of Advance and Retreat).

    Time Complexity: O(V^2 * E), or O(E * sqrt(V)) for unit networks.

Reference:
    - E. A. Dinic, "Algorithm for solution of a problem of maximum flow...", 1970.
    - S. Even and A. Itai, "Theoretical improvements in algorithmic efficiency...",
        1976.
    - https://en.wikipedia.org/wiki/Dinic%27s_algorithm
"""


class Dinic:
    """
    Implements Dinic's Algorithm for finding the Maximum Flow in a flow network.
    """

    def __init__(self, n: int) -> None:
        """
        Initialize the Dinic algorithm with n nodes.

        Args:
            n: Total number of nodes in the network. Nodes are 0-indexed.
        """
        self.n = n
        self.graph: list[list[list[int]]] = [[] for _ in range(n)]
        self.level: list[int] = []

    def add_edge(self, u: int, v: int, capacity: int) -> None:
        """
        Adds a directed edge with a specified capacity to the graph.

        Note: This stores indices to handle residual edges efficiently.

        Args:
            u: Source node index.
            v: Destination node index.
            capacity: Capacity of the edge.
        """
        # Forward edge: [v, capacity, index_of_reverse_edge]
        self.graph[u].append([v, capacity, len(self.graph[v])])
        # Backward edge: [u, 0, index_of_forward_edge]
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, source: int, sink: int) -> bool:
        """
        Builds the Level Graph (L_G) using BFS.
        Corresponds to the INITIALIZE step in the Even-Itai refinement.

        Args:
            source: The source node index.
            sink: The sink (target) node index.

        Returns:
            True if the sink is reachable from the source in the residual graph,
            False otherwise.
        """
        self.level = [-1] * self.n
        self.level[source] = 0
        # Using list as queue to avoid importing collections.deque
        # to adhere to "no external imports" policy.
        queue = [source]

        while queue:
            u = queue.pop(0)
            for v, cap, _ in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)

        return self.level[sink] >= 0

    def dfs(self, u: int, sink: int, flow: int, ptr: list[int]) -> int:
        """
        Finds a blocking flow in the Level Graph using DFS.
        Combines the ADVANCE and RETREAT steps.

        Args:
            u: Current node.
            sink: Target node.
            flow: Current flow bottleneck along the path.
            ptr: List of current arc pointers for each node (to implement
                 'Remove saturated edges' optimization).

        Returns:
            The amount of flow successfully pushed from u to sink.
        """
        if u == sink or flow == 0:
            return flow

        for i in range(ptr[u], len(self.graph[u])):
            # 'ptr[u] = i' updates the current edge pointer (pruning L_G)
            # This is the "Current Arc Optimization"
            ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]

            # Condition: Edge exists in L_G (level[v] == level[u] + 1) and has capacity
            if self.level[v] == self.level[u] + 1 and cap > 0:
                # ADVANCE step: recurse to v
                pushed = self.dfs(v, sink, min(flow, cap), ptr)

                if pushed > 0:
                    # AUGMENT step: Update residual capacities
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed

        # RETREAT step: If no flow can be pushed, this node is dead for this phase.
        return 0

    def max_flow(self, source: int, sink: int) -> int:
        """
        Computes the maximum flow from source to sink.

        Time Complexity:
            - O(V^2 * E) for general networks.
            - O(E * sqrt(V)) for unit networks (e.g., Bipartite Matching).

        Args:
            source: The source node index.
            sink: The sink (target) node index.

        Returns:
            The maximum flow value.

        Examples:
            >>> dinic = Dinic(6)
            >>> dinic.add_edge(0, 1, 16)
            >>> dinic.add_edge(0, 2, 13)
            >>> dinic.add_edge(1, 2, 10)
            >>> dinic.add_edge(1, 3, 12)
            >>> dinic.add_edge(2, 1, 4)
            >>> dinic.add_edge(2, 4, 14)
            >>> dinic.add_edge(3, 2, 9)
            >>> dinic.add_edge(3, 5, 20)
            >>> dinic.add_edge(4, 3, 7)
            >>> dinic.add_edge(4, 5, 4)
            >>> dinic.max_flow(0, 5)
            23
        """
        max_f = 0
        # While we can build a Level Graph (source can reach sink)
        while self.bfs(source, sink):
            # ptr (pointer) array stores the index of the next edge to explore.
            # This implements the "Delete v" optimization efficiently
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(source, sink, int(float("inf")), ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    dn = Dinic(6)
    edges = [
        (0, 1, 16),
        (0, 2, 13),
        (1, 2, 10),
        (1, 3, 12),
        (2, 1, 4),
        (2, 4, 14),
        (3, 2, 9),
        (3, 5, 20),
        (4, 3, 7),
        (4, 5, 4),
    ]
    for u, v, c in edges:
        dn.add_edge(u, v, c)

    print(f"Maximum Flow: {dn.max_flow(0, 5)}")
