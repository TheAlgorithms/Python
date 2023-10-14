""" 
Author: OMKAR PATHAK 

Class representing a directed graph.
"""

class Graph:
    def __init__(self):
        """
        Initialize a graph.
        """
        self.vertex = {}

    def print_graph(self) -> None:
        """
        Print the graph vertices.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> g.print_graph()
        0  ->  1 -> 2
        1  ->  2
        2  ->  0 -> 3
        3  ->  3
        """

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        Add an edge between two vertices.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.vertex
        {0: [1]}

        >>> g.add_edge(0, 2)
        >>> g.vertex
        {0: [1, 2]}
        """

    def dfs(self) -> None:
        """
        Perform Depth-First Search on the graph.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> g.dfs()
        0 1 2 3 
        """

    def dfs_recursive(self, start_vertex: int, visited: list) -> None:
        """
        Perform Depth-First Search recursively from a given vertex.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> visited = [False] * len(g.vertex)
        >>> g.dfs_recursive(0, visited)
        0 1 2 3 
        """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
