"""
Push-relabel (Goldberg-Tarjan) algorithm for the maximum-flow problem.

The push-relabel method takes a very different approach from the augmenting-path
algorithms in this directory (``ford_fulkerson.py`` builds up a valid flow one
path at a time).  Instead it works with a *preflow*, in which a vertex may
temporarily receive more flow than it sends out.  Each active vertex either
*pushes* its excess towards a neighbour that is one level lower, or is *relabeled*
to a higher level so that a push becomes possible.  When no vertex other than the
source and sink has excess, the preflow has become a maximum flow.

Using the highest-label selection rule (always discharge an active vertex whose
label is largest) this implementation runs in O(V^2 * sqrt(E)) time, which beats
the augmenting-path methods on dense graphs.

Reference: https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm
"""


class PushRelabel:
    """
    Maximum flow in a directed graph with non-negative integer capacities.

    Add edges with :meth:`add_edge`, then call :meth:`max_flow`.

    >>> g = PushRelabel(6)
    >>> capacities = {
    ...     (0, 1): 16, (0, 2): 13, (1, 2): 10, (1, 3): 12,
    ...     (2, 1): 4, (2, 4): 14, (3, 2): 9, (3, 5): 20,
    ...     (4, 3): 7, (4, 5): 4,
    ... }
    >>> for (u, v), cap in capacities.items():
    ...     g.add_edge(u, v, cap)
    >>> g.max_flow(0, 5)
    23

    It agrees with the classic four-vertex example:

    >>> h = PushRelabel(4)
    >>> for (u, v), cap in {(0, 1): 3, (0, 2): 2, (1, 2): 5,
    ...                     (1, 3): 2, (2, 3): 3}.items():
    ...     h.add_edge(u, v, cap)
    >>> h.max_flow(0, 3)
    5

    Parallel edges add up, and a disconnected sink gives zero flow:

    >>> p = PushRelabel(2)
    >>> p.add_edge(0, 1, 3)
    >>> p.add_edge(0, 1, 5)
    >>> p.max_flow(0, 1)
    8
    >>> PushRelabel(3).max_flow(0, 2)
    0
    """

    def __init__(self, vertices: int) -> None:
        if vertices <= 0:
            raise ValueError("number of vertices must be positive")
        self.size = vertices
        self.graph: list[list[int]] = [[] for _ in range(vertices)]
        # Each edge is stored as [destination, residual_capacity].
        self.edges: list[list[int]] = []

    def add_edge(self, source: int, destination: int, capacity: int) -> None:
        """
        Add a directed edge ``source -> destination`` with the given capacity.

        >>> g = PushRelabel(2)
        >>> g.add_edge(0, 1, -1)
        Traceback (most recent call last):
            ...
        ValueError: capacity must be non-negative
        >>> g.add_edge(2, 0, 1)
        Traceback (most recent call last):
            ...
        ValueError: vertex out of range
        """
        if capacity < 0:
            raise ValueError("capacity must be non-negative")
        if not (0 <= source < self.size and 0 <= destination < self.size):
            raise ValueError("vertex out of range")
        self.graph[source].append(len(self.edges))
        self.edges.append([destination, capacity])
        self.graph[destination].append(len(self.edges))
        self.edges.append([source, 0])  # reverse edge starts saturated

    def max_flow(self, source: int, sink: int) -> int:
        """
        Return the maximum flow from ``source`` to ``sink``.

        >>> PushRelabel(2).max_flow(0, 0)
        Traceback (most recent call last):
            ...
        ValueError: source and sink must be different
        """
        if not (0 <= source < self.size and 0 <= sink < self.size):
            raise ValueError("vertex out of range")
        if source == sink:
            raise ValueError("source and sink must be different")

        height = [0] * self.size
        excess = [0] * self.size
        height[source] = self.size

        # Saturate every edge leaving the source to create the initial preflow.
        for edge_index in self.graph[source]:
            destination, residual = self.edges[edge_index]
            if residual > 0:
                self.edges[edge_index][1] -= residual
                self.edges[edge_index ^ 1][1] += residual
                excess[destination] += residual
                excess[source] -= residual

        active = [
            v for v in range(self.size) if v not in (source, sink) and excess[v] > 0
        ]

        while active:
            u = max(active, key=lambda v: height[v])
            if not self._discharge(u, height):
                # Relabel: lift u just above its lowest usable neighbour.
                min_height = min(
                    height[self.edges[i][0]]
                    for i in self.graph[u]
                    if self.edges[i][1] > 0
                )
                height[u] = min_height + 1
            self._apply_pushes(u, height, excess)
            active = [
                v for v in range(self.size) if v not in (source, sink) and excess[v] > 0
            ]

        return excess[sink]

    def _discharge(self, u: int, height: list[int]) -> bool:
        """Return ``True`` if ``u`` has at least one admissible outgoing edge."""
        return any(
            self.edges[i][1] > 0 and height[self.edges[i][0]] == height[u] - 1
            for i in self.graph[u]
        )

    def _apply_pushes(self, u: int, height: list[int], excess: list[int]) -> None:
        """Push as much excess as possible from ``u`` along admissible edges."""
        for edge_index in self.graph[u]:
            if excess[u] == 0:
                break
            destination, residual = self.edges[edge_index]
            if residual > 0 and height[u] == height[destination] + 1:
                delta = min(excess[u], residual)
                self.edges[edge_index][1] -= delta
                self.edges[edge_index ^ 1][1] += delta
                excess[u] -= delta
                excess[destination] += delta


if __name__ == "__main__":
    from doctest import testmod

    testmod()
