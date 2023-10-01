# The problem is to find the shortest distance between all pairs of vertices in a weighted directed graph that can have negative edge weights.
# For the problem to be well-defined, there should be no cycles in the graph with a negative total weight.

from typing import Dict, Union
# Link to reference - https://en.wikipedia.org/wiki/Johnson%27s_algorithm
class Graph:
    def __init__(self) -> None:
        self.vertices: Dict[Union[int, str], Vertex] = {}

    def add_vertex(self, key: Union[int, str]) -> None:
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key: Union[int, str]) -> Vertex:
        """Return vertex object with the corresponding key."""
        return self.vertices[key]

    def __contains__(self, key: Union[int, str]) -> bool:
        return key in self.vertices

    def add_edge(self, src_key: Union[int, str], dest_key: Union[int, str], weight: int = 1) -> None:
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key: Union[int, str], dest_key: Union[int, str]) -> bool:
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __len__(self) -> int:
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key: Union[int, str]) -> None:
        self.key: Union[int, str] = key
        self.points_to: Dict[Vertex, int] = {}

    def get_key(self) -> Union[int, str]:
        """Return key corresponding to this vertex object."""
        return self.key

    def add_neighbour(self, dest: 'Vertex', weight: int) -> None:
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight

    def get_neighbours(self) -> Dict[Vertex, int]:
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()

    def get_weight(self, dest: 'Vertex') -> int:
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]

    def set_weight(self, dest: 'Vertex', weight: int) -> None:
        """Set weight of edge from this vertex to dest."""
        self.points_to[dest] = weight

    def does_it_point_to(self, dest: 'Vertex') -> bool:
        """Return True if this vertex points to dest."""
        return dest in self.points_to

def johnson(g: Graph) -> Dict[Vertex, Dict[Vertex, int]]:
    """Return distance where distance[u][v] is the min distance from u to v.

    distance[u][v] is the shortest distance from vertex u to v.

    g is a Graph object which can have negative edge weights.
    """
    # add new vertex q
    g.add_vertex("q")
    # let q point to all other vertices in g with zero-weight edges
    for v in g:
        g.add_edge("q", v.get_key(), 0)

    # compute shortest distance from vertex q to all other vertices
    bell_dist = bellman_ford(g, g.get_vertex("q"))

    # set weight(u, v) = weight(u, v) + bell_dist(u) - bell_dist(v) for each
    # edge (u, v)
    for v in g:
        for n in v.get_neighbours():
            w = v.get_weight(n)
            v.set_weight(n, w + bell_dist[v] - bell_dist[n])

    # remove vertex q
    # This implementation of the graph stores edge (u, v) in Vertex object u
    # Since no other vertex points back to q, we do not need to worry about
    # removing edges pointing to q from other vertices.
    del g.vertices["q"]

    distance = {v: dijkstra(g, v) for v in g}
    # correct distances
    for v in g:
        for w in g:
            distance[v][w] += bell_dist[w] - bell_dist[v]

    # correct weights in original graph
    for v in g:
        for n in v.get_neighbours():
            w = v.get_weight(n)
            v.set_weight(n, w + bell_dist[n] - bell_dist[v])

    return distance


def bellman_ford(g: Graph, source: Vertex) -> Dict[Vertex, int]:
    """Return distance where distance[v] is min distance from source to v.

    This will return a dictionary distance.

    g is a Graph object which can have negative edge weights.
    source is a Vertex object in g.
    """
    distance = dict.fromkeys(g, float("inf"))
    distance[source] = 0

    for _ in range(len(g) - 1):
        for v in g:
            for n in v.get_neighbours():
                distance[n] = min(distance[n], distance[v] + v.get_weight(n))

    return distance


def dijkstra(g: Graph, source: Vertex) -> Dict[Vertex, int]:
    """Return distance where distance[v] is min distance from source to v.

    This will return a dictionary distance.

    g is a Graph object.
    source is a Vertex object in g.
    """
    unvisited = set(g)
    distance = dict.fromkeys(g, float("inf"))
    distance[source] = 0

    while unvisited != set():
        # find vertex with minimum distance
        closest = min(unvisited, key=lambda v: distance[v])

        # mark as visited
        unvisited.remove(closest)

        # update distances
        for neighbour in closest.get_neighbours():
            if neighbour in unvisited:
                new_distance = distance[closest] + closest.get_weight(neighbour)
                distance[neighbour] = min(distance[neighbour], new_distance)
    return distance


g = Graph()

# Add vertices
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
# Add edges
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 5)
g.add_edge(3, 1, 2)

# Run Johnson's algorithm
distance = johnson(g)

# Print the result
print("Shortest distances:")
for start in g:
    for end in g:
        print(f"{start.get_key()} to {end.get_key()}", end=" ")
        print(f"distance {distance[start][end]}")

# Display vertices and edges
print("Vertices: ", end="")
for v in g:
    print(v.get_key(), end=" ")
print()

print("Edges: ")
for v in g:
    for dest in v.get_neighbours():
        w = v.get_weight(dest)
        print(f"(src={v.get_key()}, dest={dest.get_key()}, weight={w}) ")

# Output
# Shortest distances:
# 1 to 1 distance 0
# 1 to 2 distance 3
# 1 to 3 distance 8
# 2 to 1 distance 7
# 2 to 2 distance 0
# 2 to 3 distance 5
# 3 to 1 distance 2
# 3 to 2 distance 5
# 3 to 3 distance 0
# Vertices: 1 2 3
# Edges:
# (src=1, dest=2, weight=3)
# (src=2, dest=3, weight=5)
# (src=3, dest=1, weight=2)
