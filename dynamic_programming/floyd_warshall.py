import math


class Graph:
    def __init__(self, n=0):  # a graph with Node 0,1,...,N-1
        self.n = n
        self.w = [
            [math.inf for j in range(n)] for i in range(n)
        ]  # adjacency matrix for weight
        self.dp = [
            [math.inf for j in range(n)] for i in range(n)
        ]  # dp[i][j] stores minimum distance from i to j

    def add_edge(self, u, v, w):
        """
        Adds a directed edge from node u
        to node v with weight w.

        >>> g = Graph(3)
        >>> g.add_edge(0, 1, 5)
        >>> g.dp[0][1]
        5
        """
        self.dp[u][v] = w

    def floyd_warshall(self):
        """
        Computes the shortest paths between all pairs of
        nodes using the Floyd-Warshall algorithm.

        >>> g = Graph(3)
        >>> g.add_edge(0, 1, 1)
        >>> g.add_edge(1, 2, 2)
        >>> g.floyd_warshall()
        >>> g.show_min(0, 2)
        3
        >>> g.show_min(2, 0)
        inf
        """
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.dp[i][j] = min(self.dp[i][j], self.dp[i][k] + self.dp[k][j])

    def show_min(self, u, v):
        """
        Returns the minimum distance from node u to node v.

        >>> g = Graph(3)
        >>> g.add_edge(0, 1, 3)
        >>> g.add_edge(1, 2, 4)
        >>> g.floyd_warshall()
        >>> g.show_min(0, 2)
        7
        >>> g.show_min(1, 0)
        inf
        """
        return self.dp[u][v]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    graph = Graph(5)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 4, 10)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 7)
    graph.add_edge(3, 0, 10)
    graph.add_edge(3, 1, 2)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 1, 3)
    graph.add_edge(4, 2, 4)
    graph.add_edge(4, 3, 9)
    graph.floyd_warshall()
    print(
        graph.show_min(1, 4)
    )  # Should output the minimum distance from node 1 to node 4
    print(
        graph.show_min(0, 3)
    )  # Should output the minimum distance from node 0 to node 3
