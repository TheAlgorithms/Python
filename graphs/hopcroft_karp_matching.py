"""
Author: Gowrawaram Karthik Koundinya (https://github.com/G26karthik)
Description: Implementation of Hopcroft-Karp algorithm for finding maximum
             cardinality matching in bipartite graphs. Uses layered graph
             approach with BFS and DFS phases for O(E*sqrt(V)) complexity.

References:
- https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm
- Hopcroft, John E.; Karp, Richard M. (1973), "An n^5/2 algorithm for maximum
  matchings in bipartite graphs"
"""

from __future__ import annotations

from collections import deque

UNMATCHED = 0
INF = float("inf")


class BipartiteGraph:
    """
    Bipartite graph for computing maximum cardinality matching
    using the Hopcroft-Karp algorithm.

    The graph has two disjoint sets U and V with edges only between U and V nodes.
    """

    def __init__(
        self, n_u: int, n_v: int, adjacency_list: dict[int, list[int]]
    ) -> None:
        """
        Initialize the bipartite graph.

        Args:
            n_u: Number of nodes in set U (1-indexed)
            n_v: Number of nodes in set V (1-indexed)
            adjacency_list: Maps U-nodes to their connected V-nodes

        >>> graph = BipartiteGraph(3, 3, {1: [1], 2: [2], 3: [3]})
        >>> graph.n_u
        3
        >>> graph.n_v
        3
        """
        self.n_u = n_u
        self.n_v = n_v
        self.adjacency_list = adjacency_list

        # pair_u[u] = v means U-node u is matched to V-node v (0 if unmatched)
        self.pair_u = [UNMATCHED] * (n_u + 1)

        # pair_v[v] = u means V-node v is matched to U-node u (0 if unmatched)
        self.pair_v = [UNMATCHED] * (n_v + 1)

        # distance_layer[u] stores the BFS layer distance for U-node u
        self.distance_layer = [INF] * (n_u + 1)

    def _breadth_first_search_phase(self) -> bool:
        """
        Build layered graph using BFS to find shortest augmenting paths.

        Returns:
            True if an augmenting path exists, False otherwise

        >>> graph = BipartiteGraph(2, 2, {1: [1], 2: [2]})
        >>> graph._breadth_first_search_phase()
        True
        """
        queue: deque[int] = deque()

        # Initialize BFS: add all unmatched U-nodes to the queue with distance 0
        for u in range(1, self.n_u + 1):
            if self.pair_u[u] == UNMATCHED:
                self.distance_layer[u] = 0
                queue.append(u)
            else:
                self.distance_layer[u] = INF

        # Distance to dummy unmatched node (used as sentinel)
        self.distance_layer[UNMATCHED] = INF

        # BFS to build layered graph
        while queue:
            u = queue.popleft()

            # Only continue if this U-node can lead to a shorter path
            if self.distance_layer[u] < self.distance_layer[UNMATCHED]:
                # Explore all V-neighbors of this U-node
                for v in self.adjacency_list.get(u, []):
                    # Check the U-node that V is currently matched to
                    u_matched_to_v = self.pair_v[v]

                    # If we haven't visited this matched U-node yet, add it to queue
                    if self.distance_layer[u_matched_to_v] == INF:
                        self.distance_layer[u_matched_to_v] = self.distance_layer[u] + 1
                        queue.append(u_matched_to_v)

        # Return True if we found at least one augmenting path
        # (i.e., an unmatched V-node is reachable)
        return self.distance_layer[UNMATCHED] != INF

    def _depth_first_search_phase(self, node_u: int) -> bool:
        """
        Find and augment along a shortest augmenting path using DFS.

        Args:
            node_u: Current U-node in the DFS traversal

        Returns:
            True if an augmenting path was found, False otherwise

        >>> graph = BipartiteGraph(2, 2, {1: [1], 2: [2]})
        >>> graph._breadth_first_search_phase()
        True
        >>> graph._depth_first_search_phase(1)
        True
        """
        # Base case: we've reached an unmatched node (augmenting path found)
        if node_u == UNMATCHED:
            return True

        # Try all V-neighbors of this U-node
        for v in self.adjacency_list.get(node_u, []):
            u_matched_to_v = self.pair_v[v]

            # Only follow edges that go to the next layer in the BFS tree
            if self.distance_layer[u_matched_to_v] == self.distance_layer[
                node_u
            ] + 1 and self._depth_first_search_phase(u_matched_to_v):
                # Augment the matching: update both pair arrays
                self.pair_v[v] = node_u
                self.pair_u[node_u] = v
                return True

        # No augmenting path found from this node; mark it as unreachable
        self.distance_layer[node_u] = INF
        return False

    def max_cardinality_matching(self) -> int:
        """
        Find maximum cardinality matching using Hopcroft-Karp algorithm.

        Returns:
            Size of the maximum matching (number of matched edges)

        >>> # Test Case: U={1,2,3}, V={1,2,3}. Edges: (1, 2), (2, 1),
        >>> # (2, 3), (3, 3). Max matching is 3.
        >>> adj_input = {1: [2], 2: [1, 3], 3: [3]}
        >>> graph_instance = BipartiteGraph(n_u=3, n_v=3, adjacency_list=adj_input)
        >>> graph_instance.max_cardinality_matching()
        3

        >>> # Test Case: Complete bipartite graph K_{3,3}
        >>> adj_complete = {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]}
        >>> graph_complete = BipartiteGraph(n_u=3, n_v=3, adjacency_list=adj_complete)
        >>> graph_complete.max_cardinality_matching()
        3

        >>> # Test Case: No edges
        >>> adj_empty = {}
        >>> graph_empty = BipartiteGraph(n_u=3, n_v=3, adjacency_list=adj_empty)
        >>> graph_empty.max_cardinality_matching()
        0

        >>> # Test Case: Single edge
        >>> adj_single = {1: [1]}
        >>> graph_single = BipartiteGraph(n_u=2, n_v=2, adjacency_list=adj_single)
        >>> graph_single.max_cardinality_matching()
        1

        >>> # Test Case: Unbalanced graph
        >>> adj_unbalanced = {1: [1], 2: [1], 3: [2]}
        >>> graph_unbalanced = BipartiteGraph(
        ...     n_u=3, n_v=2, adjacency_list=adj_unbalanced
        ... )
        >>> graph_unbalanced.max_cardinality_matching()
        2
        """
        matching_size = 0

        # Main loop: keep finding augmenting paths until none exist
        while self._breadth_first_search_phase():
            # Try to find augmenting paths from all unmatched U-nodes
            for u in range(1, self.n_u + 1):
                if self.pair_u[u] == UNMATCHED and self._depth_first_search_phase(u):
                    # If DFS finds an augmenting path, increment the matching size
                    matching_size += 1

        return matching_size


if __name__ == "__main__":
    import doctest

    doctest.testmod()
