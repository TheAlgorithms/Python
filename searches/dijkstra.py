from queue import PriorityQueue


class Graph:

    def __init__(self, num_of_vertices: int) -> None:
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, node_a: int, node_b: int, weight: int) -> None:
        """
        >>> g = Graph(9)
        >>> g.add_edge(0, 1, 4)
        >>> assert g.edges[0][1] == 4
        >>> assert g.edges[1][0] == 4
        """
        self.edges[node_a][node_b] = weight
        self.edges[node_b][node_a] = weight

    def dijkstra(self, start_vertex: int) -> dict:
        """
        >>> g = Graph(9)
        >>> g.add_edge(0, 1, 4)
        >>> g.add_edge(0, 6, 7)
        >>> g.add_edge(1, 6, 11)
        >>> g.add_edge(1, 7, 20)
        >>> g.add_edge(1, 2, 9)
        >>> g.add_edge(2, 3, 6)
        >>> g.add_edge(2, 4, 2)
        >>> g.add_edge(3, 4, 10)
        >>> g.add_edge(3, 5, 5)
        >>> g.add_edge(4, 5, 15)
        >>> g.add_edge(4, 7, 1)
        >>> g.add_edge(4, 8, 5)
        >>> g.add_edge(5, 8, 12)
        >>> g.add_edge(6, 7, 1)
        >>> g.add_edge(7, 8, 3)
        >>> distance = g.dijkstra(0)
        >>> [for dis in distance)]
        [0, 4, 11, 17, 9, 22, 7, 8, 11]
        """
        distance = {v: float('inf') for v in range(self.v)}
        distance[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = distance[neighbor]
                        new_cost = distance[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            distance[neighbor] = new_cost
        return distance


def main() -> None:
    """
    >>> g = Graph(9)
    >>> g.add_edge(0, 1, 4)
    >>> g.add_edge(0, 6, 7)
    >>> g.add_edge(1, 6, 11)
    >>> g.add_edge(1, 7, 20)
    >>> g.add_edge(1, 2, 9)
    >>> g.add_edge(2, 3, 6)
    >>> g.add_edge(2, 4, 2)
    >>> g.add_edge(3, 4, 10)
    >>> g.add_edge(3, 5, 5)
    >>> g.add_edge(4, 5, 15)
    >>> g.add_edge(4, 7, 1)
    >>> g.add_edge(4, 8, 5)
    >>> g.add_edge(5, 8, 12)
    >>> g.add_edge(6, 7, 1)
    >>> g.add_edge(7, 8, 3)
    >>> distance = g.dijkstra(0)
    >>> [for dis in distance)]
    [0, 4, 11, 17, 9, 22, 7, 8, 11]
    """
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)
    distance = g.dijkstra(0)

    for vertex in range(len(distance)):
        print("Distance from vertex 0 to vertex", vertex, "is", distance[vertex])


if __name__ == "__main__":
    main()
