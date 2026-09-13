"""Hopcroft-Karp algorithm for finding maximum cardinality matching in bipartite graphs.

Reference:
    https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm

The Hopcroft-Karp algorithm finds a maximum cardinality matching in an unweighted
bipartite graph in O(|E| * sqrt(|V|)) time.

Key Concepts and Conditions:
1. Bipartite Condition:
   A graph G = (U union V, E) is bipartite if its vertices can be partitioned into
   two disjoint sets U (left partition) and V (right partition) such that every
   edge connects a vertex in U to a vertex in V. No edges may exist between two
   vertices within the same partition (U intersect V = empty set). Vertices cannot
   be None.

2. Matching Condition:
   A matching M is a subset of edges such that no two edges share a common vertex.
   A vertex is 'free' (unmatched) if it is not incident to any edge in M.

3. Alternating and Augmenting Paths:
   - Alternating path: A path whose edges alternate between unmatched edges
     (not in M) and matched edges (in M).
   - Augmenting path: An alternating path that starts and ends at distinct free
     vertices.
   - Berge's Lemma: A matching is of maximum cardinality if and only if no
     augmenting paths exist.

4. Hopcroft-Karp Layering and Augmentation Conditions:
   Instead of searching for augmenting paths one-by-one (O(|V| * |E|)), Hopcroft-Karp
   operates in phases:
   - BFS Phase (Layering): Simultaneously searches from all free vertices in U to
     find the length of the shortest augmenting paths. It builds a layered DAG of
     alternating levels. If no free vertex in V is reachable, the algorithm terminates.
   - DFS Phase (Augmentation): Discovers a maximal set of vertex-disjoint augmenting
     paths of the shortest length found by BFS. It only traverses edges satisfying:
     distance_map[matched_left] == distance_map[curr_left] + 1.
   - Symmetric Difference: Matching edges along each augmenting path are flipped
     (unmatched becomes matched, matched becomes unmatched).
   - Iterative DFS: The DFS phase is implemented iteratively using an explicit stack
     to prevent RecursionError on graphs with large alternating path diameters.

Complexity:
    Time Complexity:  O(|E| * sqrt(|V|))
    Space Complexity: O(|V| + |E|)
"""

from __future__ import annotations

import math
from collections import deque

_NIL = object()


class HopcroftKarp[T]:
    """Class implementing the Hopcroft-Karp maximum bipartite matching algorithm.

    >>> hk = HopcroftKarp({"u1": ["v1", "v2"], "u2": ["v1"], "u3": ["v2", "v3"]})
    >>> hk.maximum_matching()
    {'u1': 'v2', 'u2': 'v1', 'u3': 'v3'}
    """

    def __init__(self, graph: dict[T, list[T]]) -> None:
        """Initialize bipartite partitions and match pairing dictionaries.

        Raises:
            ValueError: If partitions overlap or if any vertex is None.

        >>> hk = HopcroftKarp({"u1": ["v1"]})
        >>> hk.left_vertices
        ['u1']
        >>> hk.right_vertices
        ['v1']
        >>> HopcroftKarp({"A": ["A"]})
        Traceback (most recent call last):
            ...
        ValueError: Partitions must be disjoint: found vertices in both sets: ['A']
        >>> HopcroftKarp({"u1": [None]})
        Traceback (most recent call last):
            ...
        ValueError: Vertices cannot be None
        """
        self.graph = graph
        self.left_vertices = list(graph.keys())
        self.right_vertices = sorted(
            {
                right_vertex
                for neighbors in graph.values()
                for right_vertex in neighbors
            },
            key=repr,
        )

        if any(vertex is None for vertex in self.left_vertices) or any(
            vertex is None for vertex in self.right_vertices
        ):
            msg = "Vertices cannot be None"
            raise ValueError(msg)

        overlap = set(self.left_vertices) & set(self.right_vertices)
        if overlap:
            msg = (
                f"Partitions must be disjoint: found vertices in both sets: "
                f"{sorted(overlap, key=repr)}"
            )
            raise ValueError(msg)

        # pair_left[u] stores matched vertex in V for u in U (or _NIL if free)
        self.pair_left: dict[T, T | object] = dict.fromkeys(self.left_vertices, _NIL)
        # pair_right[v] stores matched vertex in U for v in V (or _NIL if free)
        self.pair_right: dict[T, T | object] = dict.fromkeys(self.right_vertices, _NIL)
        # distance_map stores the BFS level from free vertices in U
        self.distance_map: dict[T | object, float] = {}

    def breadth_first_search(self) -> bool:
        """BFS Phase: Layer the graph and find shortest augmenting path length.

        Returns:
            True if at least one augmenting path to a free vertex in V exists,
            False otherwise (termination condition).

        >>> hk = HopcroftKarp({"u1": ["v1"]})
        >>> hk.breadth_first_search()
        True
        >>> hk.pair_left["u1"] = "v1"
        >>> hk.pair_right["v1"] = "u1"
        >>> hk.breadth_first_search()
        False
        """
        queue: deque[T] = deque()

        # Enqueue all free vertices in the left partition at level 0
        for left_vertex in self.left_vertices:
            if self.pair_left[left_vertex] is _NIL:
                self.distance_map[left_vertex] = 0.0
                queue.append(left_vertex)
            else:
                self.distance_map[left_vertex] = math.inf

        # distance_map[_NIL] represents distance to a free vertex in right partition
        self.distance_map[_NIL] = math.inf

        while queue:
            left_vertex = queue.popleft()
            if self.distance_map[left_vertex] < self.distance_map[_NIL]:
                for right_vertex in self.graph[left_vertex]:
                    matched_left = self.pair_right[right_vertex]
                    if self.distance_map.get(matched_left, math.inf) == math.inf:
                        self.distance_map[matched_left] = (
                            self.distance_map[left_vertex] + 1.0
                        )
                        if matched_left is not _NIL:
                            queue.append(matched_left)  # type: ignore[arg-type]

        return self.distance_map[_NIL] != math.inf

    def depth_first_search(self, start_left: T) -> bool:
        """DFS Phase: Find and augment along shortest augmenting paths iteratively.

        Implemented iteratively with an explicit stack to prevent RecursionError
        on graphs with deep alternating paths (diameter > 1000).

        Parameters:
            start_left: The free vertex in the left partition to start the search from.

        Returns:
            True if an augmenting path was found and augmented, False otherwise.

        >>> hk = HopcroftKarp({"u1": ["v1"]})
        >>> _ = hk.breadth_first_search()
        >>> hk.depth_first_search("u1")
        True
        >>> hk.pair_left["u1"]
        'v1'
        >>> hk.depth_first_search("u1")
        False
        """
        stack: list[T] = [start_left]
        neighbor_indices: list[int] = [0]
        path: list[tuple[T, T]] = []

        while stack:
            curr_left = stack[-1]
            curr_index = neighbor_indices[-1]
            neighbors = self.graph[curr_left]

            found_next = False
            for idx in range(curr_index, len(neighbors)):
                right_vertex = neighbors[idx]
                matched_left = self.pair_right[right_vertex]

                # Augmentation Condition: Only step along shortest layer paths
                if (
                    self.distance_map.get(matched_left, math.inf)
                    == self.distance_map[curr_left] + 1.0
                ):
                    neighbor_indices[-1] = idx + 1
                    path.append((curr_left, right_vertex))

                    if matched_left is _NIL:
                        # Reached a free right vertex: augment matching along path
                        for path_left, path_right in path:
                            self.pair_right[path_right] = path_left
                            self.pair_left[path_left] = path_right
                        return True

                    stack.append(matched_left)  # type: ignore[arg-type]
                    neighbor_indices.append(0)
                    found_next = True
                    break

            if not found_next:
                # Dead end: prune curr_left from this phase
                self.distance_map[curr_left] = math.inf
                stack.pop()
                neighbor_indices.pop()
                if path:
                    path.pop()

        return False

    def maximum_matching(self) -> dict[T, T]:
        """Compute and return the maximum cardinality matching.

        >>> hk = HopcroftKarp({"u1": ["v1"], "u2": ["v1"]})
        >>> hk.maximum_matching()
        {'u1': 'v1'}
        """
        while self.breadth_first_search():
            for left_vertex in self.left_vertices:
                if self.pair_left[left_vertex] is _NIL:
                    self.depth_first_search(left_vertex)

        return {
            left_vertex: matched_right  # type: ignore[misc]
            for left_vertex, matched_right in self.pair_left.items()
            if matched_right is not _NIL
        }


def hopcroft_karp[T](graph: dict[T, list[T]]) -> dict[T, T]:
    """Find a maximum cardinality matching in a bipartite graph using Hopcroft-Karp.

    Parameters:
        graph: An adjacency list mapping each vertex in the left partition (U) to
            a list of adjacent vertices in the right partition (V). The two
            partitions must be disjoint, and vertices cannot be None.

    Returns:
        A dictionary representing the matching, mapping each matched vertex in
        the left partition to its matched partner in the right partition.

    Raises:
        ValueError: If any vertex appears in both partitions or if any vertex is None.

    Examples:
        >>> # Standard bipartite matching
        >>> graph = {"u1": ["v1", "v2"], "u2": ["v1"], "u3": ["v2", "v3"]}
        >>> hopcroft_karp(graph)
        {'u1': 'v2', 'u2': 'v1', 'u3': 'v3'}

        >>> # Empty graph condition
        >>> hopcroft_karp({})
        {}

        >>> # Isolated vertices (no incident edges)
        >>> hopcroft_karp({"u1": []})
        {}

        >>> # Competing vertices (more left vertices than right vertices)
        >>> hopcroft_karp({"u1": ["v1"], "u2": ["v1"]})
        {'u1': 'v1'}

        >>> # Bipartite cycle (6 vertices)
        >>> cycle_graph = {
        ...     "u1": ["v1", "v2"],
        ...     "u2": ["v2", "v3"],
        ...     "u3": ["v3", "v1"],
        ... }
        >>> hopcroft_karp(cycle_graph)
        {'u1': 'v1', 'u2': 'v2', 'u3': 'v3'}

        >>> # Error condition: Overlapping partitions (not a valid bipartite graph)
        >>> hopcroft_karp({"A": ["A"]})
        Traceback (most recent call last):
            ...
        ValueError: Partitions must be disjoint: found vertices in both sets: ['A']

        >>> # Error condition: None vertex
        >>> hopcroft_karp({"u": [None]})
        Traceback (most recent call last):
            ...
        ValueError: Vertices cannot be None
    """
    return HopcroftKarp(graph).maximum_matching()


def test_hopcroft_karp() -> None:
    """Pytest test function to verify maximum bipartite matching functionality.

    >>> test_hopcroft_karp()
    """
    assert hopcroft_karp({"u1": ["v1", "v2"], "u2": ["v1"], "u3": ["v2", "v3"]}) == {
        "u1": "v2",
        "u2": "v1",
        "u3": "v3",
    }
    assert hopcroft_karp({}) == {}
    assert hopcroft_karp({"u1": []}) == {}
    assert hopcroft_karp({"u1": ["v1"], "u2": ["v1"]}) == {"u1": "v1"}
    assert hopcroft_karp(
        {"u1": ["v1", "v2"], "u2": ["v2", "v3"], "u3": ["v3", "v1"]}
    ) == {"u1": "v1", "u2": "v2", "u3": "v3"}

    # Test deep alternating path to ensure no RecursionError occurs
    chain_length = 1500
    chain_graph = {f"u{i}": [f"v{i}", f"v{i + 1}"] for i in range(chain_length)}
    assert len(hopcroft_karp(chain_graph)) == chain_length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
