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
   vertices within the same partition (U intersect V = empty set).

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
     distance_map[matched_left] == distance_map[left_vertex] + 1.
   - Symmetric Difference: Matching edges along each augmenting path are flipped
     (unmatched becomes matched, matched becomes unmatched).

Complexity:
    Time Complexity:  O(|E| * sqrt(|V|))
    Space Complexity: O(|V| + |E|)
"""

from __future__ import annotations

import math
from collections import deque


def hopcroft_karp[T](graph: dict[T, list[T]]) -> dict[T, T]:
    """Find a maximum cardinality matching in a bipartite graph using Hopcroft-Karp.

    Parameters:
        graph: An adjacency list mapping each vertex in the left partition (U) to
            a list of adjacent vertices in the right partition (V). The two
            partitions must be disjoint.

    Returns:
        A dictionary representing the matching, mapping each matched vertex in
        the left partition to its matched partner in the right partition.

    Raises:
        ValueError: If any vertex appears in both the left and right partitions,
            violating the disjoint bipartite partition condition.

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
    """
    left_vertices = list(graph.keys())
    right_vertices = sorted(
        {right_vertex for neighbors in graph.values() for right_vertex in neighbors},
        key=repr,
    )

    # Condition Check: Partitions U and V must be disjoint
    overlap = set(left_vertices) & set(right_vertices)
    if overlap:
        msg = (
            f"Partitions must be disjoint: found vertices in both sets: "
            f"{sorted(overlap, key=repr)}"
        )
        raise ValueError(msg)

    # pair_left[u] stores the vertex in V matched to u in U (or None if free)
    pair_left: dict[T, T | None] = dict.fromkeys(left_vertices)
    # pair_right[v] stores the vertex in U matched to v in V (or None if free)
    pair_right: dict[T, T | None] = dict.fromkeys(right_vertices)
    # distance_map stores the BFS level/distance from free vertices in U
    distance_map: dict[T | None, float] = {}

    def breadth_first_search() -> bool:
        """BFS Phase: Layer the graph and find shortest augmenting path length.

        Returns:
            True if at least one augmenting path to a free vertex in V exists,
            False otherwise (termination condition).
        """
        queue: deque[T] = deque()

        # Initialize BFS from all free vertices in the left partition U
        for left_vertex in left_vertices:
            if pair_left[left_vertex] is None:
                distance_map[left_vertex] = 0.0
                queue.append(left_vertex)
            else:
                distance_map[left_vertex] = math.inf

        # distance_map[None] represents distance to a free vertex in right partition V
        distance_map[None] = math.inf

        while queue:
            left_vertex = queue.popleft()

            # Only explore while distance is strictly less than shortest augmenting path
            if distance_map[left_vertex] < distance_map[None]:
                for right_vertex in graph[left_vertex]:
                    matched_left = pair_right[right_vertex]

                    # If matched_left has not been visited in this BFS phase
                    if distance_map.get(matched_left, math.inf) == math.inf:
                        distance_map[matched_left] = distance_map[left_vertex] + 1.0
                        if matched_left is not None:
                            queue.append(matched_left)

        # Termination condition: True if an augmenting path was found, False otherwise
        return distance_map[None] != math.inf

    def depth_first_search(left_vertex: T | None) -> bool:
        """DFS Phase: Find vertex-disjoint augmenting paths along shortest layers.

        Returns:
            True if an augmenting path was successfully found and augmented,
            False otherwise.
        """
        if left_vertex is not None:
            for right_vertex in graph[left_vertex]:
                matched_left = pair_right[right_vertex]

                # Augmentation Condition: Only step forward along the layered DAG
                if distance_map.get(matched_left, math.inf) == distance_map[
                    left_vertex
                ] + 1.0 and depth_first_search(matched_left):
                    # Augment the path by flipping matched/unmatched edges
                    pair_right[right_vertex] = left_vertex
                    pair_left[left_vertex] = right_vertex
                    return True

            # If no augmenting path can proceed through left_vertex, prune it
            distance_map[left_vertex] = math.inf
            return False

        # Base case: reached a free vertex in V (represented by None)
        return True

    # Main Loop: Alternate BFS layering and DFS augmentations
    while breadth_first_search():
        for left_vertex in left_vertices:
            if pair_left[left_vertex] is None:
                depth_first_search(left_vertex)

    # Return only the matched pairs from left partition U -> right partition V
    return {
        left_vertex: matched_right
        for left_vertex, matched_right in pair_left.items()
        if matched_right is not None
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
