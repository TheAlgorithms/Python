import itertools
from collections.abc import Generator, Hashable, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T", bound=int | str | Hashable)


@dataclass(frozen=True)
class TSPEdge(Generic[T]):
    """
    Represents an edge in a graph for the Traveling Salesman Problem (TSP).

    Attributes:
        vertices (frozenset[T]): A pair of vertices representing the edge.
        weight (float): The weight (or cost) of the edge.
    """

    vertices: frozenset[T]
    weight: float

    def __str__(self) -> str:
        """
        Examples:
            >>> tsp_edge = TSPEdge.from_3_tuple(1, 2, 0.5)
            >>> str(tsp_edge)
            '(frozenset({1, 2}), 0.5)'
        """
        return f"({self.vertices}, {self.weight})"

    def __post_init__(self) -> None:
        # Ensures that there is no loop in a vertex
        if len(self.vertices) != 2:
            raise ValueError("frozenset must have exactly 2 elements")

    @classmethod
    def from_3_tuple(cls, vertex_1: T, vertex_2: T, weight: float) -> "TSPEdge":
        """
        Construct TSPEdge from a 3-tuple (x, y, w).
        x & y are vertices and w is the weight.

        Examples:
            >>> tsp_edge = TSPEdge.from_3_tuple(1, 2, 0.5)
            >>> tsp_edge.vertices
            frozenset({1, 2})
            >>> tsp_edge.weight
            0.5
        """
        return cls(frozenset([vertex_1, vertex_2]), weight)

    def __eq__(self, other: object) -> bool:
        """
        Examples:
            >>> tsp_edge_1 = TSPEdge.from_3_tuple(1, 2, 0.5)
            >>> tsp_edge_2 = TSPEdge.from_3_tuple(2, 1, 0.7)
            >>> tsp_edge_1 == tsp_edge_2
            True
        """
        if not isinstance(other, TSPEdge):
            return NotImplemented
        return self.vertices == other.vertices

    def __add__(self, other: "TSPEdge") -> float:
        """
        Examples:
            >>> tsp_edge_1 = TSPEdge.from_3_tuple(1, 2, 1.0)
            >>> tsp_edge_2 = TSPEdge.from_3_tuple(2, 1, 2.5)
            >>> tsp_edge_1 + tsp_edge_2
            3.5
        """
        return self.weight + other.weight


class TSPGraph(Generic[T]):
    """
    Represents a graph for the Traveling Salesman Problem (TSP).
    The graph is:
    - Simple (no loops or multiple edges between vertices).
    - Undirected.
    - Connected.
    """

    def __init__(self, edges: frozenset[TSPEdge] | None = None):
        self._edges = edges or frozenset()

    def __str__(self) -> str:
        return f"{[str(edge) for edge in self._edges]}"

    @classmethod
    def from_3_tuples(cls, *edges) -> "TSPGraph":
        return cls(frozenset(TSPEdge.from_3_tuple(x, y, w) for x, y, w in edges))

    @classmethod
    def from_weights(cls, weights: list) -> "TSPGraph":
        """
        Create TSPGraph from Weights (List of Lists) where the vertices
        are labeled with integers.
        """
        triples = [
            (x, y, weights[x][y])
            for x, y in itertools.product(range(len(weights)), range(len(weights[0])))
            if x != y  # Filter out self-loops
        ]
        # return cls.from_3_tuples(*cast(list[tuple[T, T, float]], triples))
        return cls.from_3_tuples(*triples)

    @property
    def vertices(self) -> frozenset[T]:
        return frozenset(vertex for edge in self._edges for vertex in edge.vertices)

    @property
    def edges(self) -> frozenset[TSPEdge]:
        return self._edges

    @property
    def weight(self) -> float:
        """Total Weight of TSPGraph."""
        return sum(edge.weight for edge in self._edges)

    def __contains__(self, obj: T | TSPEdge) -> bool:
        if isinstance(obj, TSPEdge):
            return any(obj == edge_ for edge_ in self._edges)
        else:
            return obj in self.vertices

    def is_edge_in_graph(self, x: T, y: T) -> bool:
        return frozenset([x, y]) in self.get_edges()

    def add_edge(self, x: T, y: T, w: float) -> "TSPGraph":
        # Validator to check if either x or y is in the vertex set to ensure
        # that the graph would be connected
        # Only use this validator if there exist at least 1 edge in the edge set.
        if self._edges and x not in self and y not in self:
            error_message = f"Adding the edge ({x}, {y}) may form a disconnected graph."
            raise ValueError(error_message)

        new_edge = TSPEdge.from_3_tuple(
            x, y, w
        )  # This would raise Vertex Loop error if x == y

        # Raise error if Multi-Edges
        if new_edge in self:
            error_message = f"({x}, {y}, {w}) is invalid."
            raise ValueError(error_message)

        return TSPGraph(
            edges=frozenset(self._edges | frozenset([TSPEdge.from_3_tuple(x, y, w)]))
        )

    def get_edges(self) -> list[frozenset[T]]:
        return [edge.vertices for edge in self.edges]

    def get_edge_weight(self, x: T, y: T) -> float:
        if (x not in self) or (y not in self):
            error_message = f"{x} or {y} does not belong to the graph vertices."
            raise ValueError(error_message)

        # Find the edge with vertices (x, y)
        edge = next(
            (edge for edge in self.edges if frozenset([x, y]) == edge.vertices), None
        )

        if edge is None:
            error_message = f"No edge exists between {x} and {y}."
            raise ValueError(error_message)

        return edge.weight

    def get_vertex_neighbors(self, x: T) -> frozenset[T]:
        if x not in self.vertices:
            error_message = f"{x} does not belong to the graph vertex set."
            raise ValueError(error_message)
        return frozenset(
            next(iter(edge.vertices - frozenset([x])))
            for edge in self.edges
            if x in edge.vertices
        )

    def get_vertex_degree(self, x: T) -> int:
        if x not in self.vertices:
            error_message = f"{x} does not belong to the graph vertices."
            raise ValueError(error_message)
        return sum(1 for edge in self.edges if x in edge.vertices)

    def get_vertex_argmin(self, x: T) -> T:
        """Returns the Neighbor of a Vertex with the Minimum Weight."""
        return min(
            [(y, self.get_edge_weight(x, y)) for y in self.get_vertex_neighbors(x)],
            key=lambda tup: tup[1],
        )[0]

    def get_vertex_argmax(self, x: T) -> T:
        """Returns the Neighbor of a Vertex with the Maximum Weight."""
        return max(
            [(y, self.get_edge_weight(x, y)) for y in self.get_vertex_neighbors(x)],
            key=lambda tup: tup[1],
        )[0]

    def get_vertex_neighbor_weights(self, x: T) -> Sequence[tuple[T, float]]:
        # Sort by Smallest to Largest
        return sorted(
            [(y, self.get_edge_weight(x, y)) for y in self.get_vertex_neighbors(x)],
            key=lambda tup: tup[1],  # pair[1] is the weight (float)
        )


def adjacent_tuples(path: list[T]) -> zip:
    """
    Generates adjacent pairs of elements from a path.

    Args:
        path (list[T]): A list of vertices representing a path.

    Returns:
        zip: A zip object containing tuples of adjacent vertices.

    Examples:
        >>> list(adjacent_tuples([1, 2, 3, 4, 5]))
        [(1, 2), (2, 3), (3, 4), (4, 5)]

        >>> list(adjacent_tuples(["A", "B", "C", "D", "E"]))
        [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
    """
    iter1, iter2 = itertools.tee(path)
    next(iter2, None)
    return zip(iter1, iter2)


def path_weight(path: list[T], tsp_graph: TSPGraph) -> float:
    """
    Calculates the total weight of a given path in the graph.

    Args:
        path (list[T]): A list of vertices representing a path.
        tsp_graph (TSPGraph): The graph containing the edges and weights.

    Returns:
        float: The total weight of the path.

    Examples:
        >>> graph = TSPGraph.from_3_tuples((1, 2, 2), (2, 3, 4), (3, 4, 2), (4, 5, 1))
        >>> path_weight([1, 2, 3], graph)
        6
        >>> path_weight([1, 2, 3, 4], graph)
        8
        >>> path_weight([1, 2, 3, 4, 5], graph)
        9
    """
    return sum(tsp_graph.get_edge_weight(x, y) for x, y in adjacent_tuples(path))


def generate_paths(start: T, end: T, tsp_graph: TSPGraph) -> Generator[list[T]]:
    """
    Generates all possible paths between two vertices in a
    TSPGraph using Depth-First Search (DFS).

    Args:
        start (T): The starting vertex.
        end (T): The target vertex.
        tsp_graph (TSPGraph): The graph to traverse.

    Yields:
        Generator[list[T]]: A generator yielding paths as lists of vertices.

    Raises:
        AssertionError: If start or end is not in the graph, or if they are the same.

    Examples:
        >>> graph = TSPGraph.from_3_tuples((1, 2, 2), (2, 3, 4), (3, 1, 2))
        >>> graph_generator = generate_paths(1, 3, graph)
        >>> next(graph_generator)
        [1, 2, 3]
        >>> next(graph_generator)
        [1, 3]
    """

    assert start in tsp_graph.vertices
    assert end in tsp_graph.vertices
    assert start != end

    def dfs(
        current: T, target: T, visited: set[T], path: list[T]
    ) -> Generator[list[T]]:
        visited.add(current)
        path.append(current)

        # If we reach the target, yield the current path
        if current == target:
            yield list(path)
        else:
            # Recur for all unvisited neighbors
            for neighbor in tsp_graph.get_vertex_neighbors(current):
                if neighbor not in visited:
                    yield from dfs(neighbor, target, visited, path)

        # Backtrack
        path.pop()
        visited.remove(current)

    # Initialize DFS
    yield from dfs(start, end, set(), [])


def nearest_neighborhood(
    tsp_graph: TSPGraph, current_vertex: T, visited_: list[T] | None = None
) -> list[T] | None:
    """
    Approximates a solution to the Traveling Salesman Problem
    using the Nearest Neighbor heuristic.

    Args:
        tsp_graph (TSPGraph): The graph to traverse.
        v (T): The starting vertex.
        visited_ (list[T] | None): A list of already visited vertices.

    Returns:
        list[T] | None: A complete Hamiltonian cycle if possible, otherwise None.

    Examples:
        >>> edges = [
        ...     ("A", "B", 7), ("A", "D", 1), ("A", "E", 1),
        ...     ("B", "C", 3), ("B", "E", 8), ("C", "E", 2),
        ...     ("C", "D", 6), ("D", "E", 7)
        ... ]
        >>> graph = TSPGraph.from_3_tuples(*edges)
        >>> import random
        >>> init_v = random.choice(list(graph.vertices))
        >>> result = nearest_neighborhood(graph, init_v)
        >>> assert result in [
        ...     ['A', 'D', 'C', 'E', 'B', 'A'],
        ...     ['E', 'A', 'D', 'C', 'B', 'E'],
        ...     None
        ... ]
        >>> path_1 = ['A', 'D', 'C', 'E', 'B', 'A']
        >>> path_2 = ['E', 'A', 'D', 'C', 'B', 'E']
        >>> assert path_weight(path_1, graph) == 24 if result == path_1 else 19 or None
        >>> assert path_weight(path_2, graph) == 19 if result == path_2 else 24 or None
    """
    # Initialize visited list on first call
    visited = visited_ or [current_vertex]

    # Base case: if all vertices are visited
    if len(visited) == len(tsp_graph.vertices):
        # Check if there is an edge to return to the starting point
        if tsp_graph.is_edge_in_graph(visited[-1], visited[0]):
            return [*visited, visited[0]]
        else:
            return None

    # Get unvisited neighbors
    filtered_neighbors = [
        tup
        for tup in tsp_graph.get_vertex_neighbor_weights(current_vertex)
        if tup[0] not in visited
    ]

    # If there are unvisited neighbors, continue to the nearest one
    if filtered_neighbors:
        next_v = min(filtered_neighbors, key=lambda tup: tup[1])[0]
        return nearest_neighborhood(
            tsp_graph, current_vertex=next_v, visited_=[*visited, next_v]
        )
    else:
        # No more neighbors, return None (cannot form a complete tour)
        return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
