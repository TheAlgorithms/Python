"""
ISAP (Improved Shortest Augmenting Path) Algorithm for Maximum Flow.

ISAP is an improvement over the Dinic algorithm. It avoids the need to
repeatedly run BFS to build a level graph by maintaining distance labels
and updating them dynamically (Relabeling) during the DFS traversal.
It also includes the GAP optimization to terminate early if a gap in
distance levels appears.

Time Complexity: O(V^2 * E)

While widely used in the Chinese competitive programming community
for Maximum Flow problems, the original academic source of this
algorithm is obscure.

Reference: https://en.wikipedia.org/wiki/Maximum_flow_problem
           https://www.luogu.com.cn/article/v2yahmsa

"""

from collections import deque


class ISAP:
    """
    Implements the ISAP algorithm to find the maximum flow in a flow network.
    """

    def __init__(self, graph: list[list[int]], source: int, sink: int) -> None:
        """
        Initialize the ISAP algorithm with a capacity matrix.

        :param graph: Adjacency matrix where graph[u][v] is the capacity of edge u->v.
        :param source: The source node index.
        :param sink: The sink node index.
        """
        self.graph = graph
        self.num_nodes = len(graph)
        self.source = source
        self.sink = sink
        # Residual graph capacity
        self.capacity = [row[:] for row in graph]

        # FIX: Allocate more space for height and gap arrays.
        # During relabeling, heights can technically exceed num_nodes when
        # nodes become unreachable. 2 * num_nodes is a safe upper bound to
        # prevent IndexError.
        self.height = [0] * (2 * self.num_nodes)
        self.gap = [0] * (2 * self.num_nodes)

    def _bfs_init(self) -> None:
        """
        Perform a backward BFS from the sink to initialize height labels.
        This sets the shortest distance from each node to the sink.
        """
        # Initialize with a value larger than any valid path (num_nodes)
        self.height = [self.num_nodes] * (2 * self.num_nodes)
        self.height[self.sink] = 0

        # Reset gap array
        self.gap = [0] * (2 * self.num_nodes)

        queue = deque([self.sink])
        self.gap[0] = 1  # The sink is at height 0

        while queue:
            u = queue.popleft()

            for v in range(self.num_nodes):
                # Check reverse edges in residual graph (capacity[v][u] > 0)
                # and if v is unvisited (height is still initial large value)
                if self.capacity[v][u] > 0 and self.height[v] == self.num_nodes:
                    self.height[v] = self.height[u] + 1
                    self.gap[self.height[v]] += 1
                    queue.append(v)

    def _dfs(self, u: int, flow_in: int) -> int:
        """
        Perform DFS to find augmenting paths in the residual graph.

        :param u: Current node.
        :param flow_in: Current flow bottleneck.
        :return: The flow pushed through this path.
        """
        if u == self.sink:
            return flow_in

        flow_pushed = 0
        for v in range(self.num_nodes):
            # If there is residual capacity and v is the next level closer to sink
            if self.capacity[u][v] > 0 and self.height[u] == self.height[v] + 1:
                bottleneck = min(flow_in - flow_pushed, self.capacity[u][v])
                pushed = self._dfs(v, bottleneck)

                if pushed > 0:
                    self.capacity[u][v] -= pushed
                    self.capacity[v][u] += pushed
                    flow_pushed += pushed
                    if flow_pushed == flow_in:
                        return flow_pushed

        # Relabel logic
        # If we couldn't push enough flow, we need to raise the height of u.
        if flow_pushed == 0:
            # GAP Optimization:
            # If the count of nodes at the current height becomes 0,
            # it means the path to sink is broken for all nodes above this height.
            if self.gap[self.height[u]] == 0:
                self.height[self.source] = self.num_nodes
                return 0

            self.gap[self.height[u]] -= 1

            # Find the minimum height among neighbors to set new height
            min_height = self.num_nodes
            for v in range(self.num_nodes):
                if self.capacity[u][v] > 0:
                    min_height = min(min_height, self.height[v])

            self.height[u] = min_height + 1
            self.gap[self.height[u]] += 1

        return flow_pushed

    def max_flow(self) -> int:
        """
        Compute the maximum flow from source to sink.

        :return: The maximum flow value.

        >>> graph = [
        ...     [0, 16, 13, 0, 0, 0],
        ...     [0, 0, 10, 12, 0, 0],
        ...     [0, 4, 0, 0, 14, 0],
        ...     [0, 0, 9, 0, 0, 20],
        ...     [0, 0, 0, 7, 0, 4],
        ...     [0, 0, 0, 0, 0, 0]
        ... ]
        >>> isap = ISAP(graph, 0, 5)
        >>> isap.max_flow()
        23

        >>> graph_2 = [
        ...     [0, 3, 2, 0],
        ...     [0, 0, 1, 1],
        ...     [0, 0, 0, 4],
        ...     [0, 0, 0, 0]
        ... ]
        >>> isap_2 = ISAP(graph_2, 0, 3)
        >>> isap_2.max_flow()
        4
        """
        self._bfs_init()
        max_flow_value = 0

        # Run until the source's distance label implies it's unreachable
        # (Technically if height[s] >= num_nodes)
        while self.height[self.source] < self.num_nodes:
            max_flow_value += self._dfs(self.source, 10**18)

        return max_flow_value


if __name__ == "__main__":
    import doctest

    doctest.testmod()
