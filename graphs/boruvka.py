"""Borůvka's algorithm.

    Determines the minimum spanning tree(MST) of a graph using the Borůvka's algorithm.
    Borůvka's algorithm is a greedy algorithm for finding a minimum spanning tree in a
    graph,or a minimum spanning forest in the case of a graph that is not connected.

    The time complexity of this algorithm is O(ELogV), where E represents the number
    of edges, while V represents the number of nodes.

    The space complexity of this algorithm is O(V + E), since we have to keep a couple
    of lists whose sizes are equal to the number of nodes, as well as keep all the
    edges of a graph inside of the data structure itself.

    Borůvka's algorithm gives us pretty much the same result as other MST Algorithms -
    they all find the minimum spanning tree, and the time complexity is approximately
    the same.

    One advantage that Borůvka's algorithm has compared to the alternatives is that it
    doesn't need to presort the edges or maintain a priority queue in order to find the
    minimum spanning tree.
    Even though that doesn't help its complexity, since it still passes the edges logE
    times, it is a bit more simple to code.

    Details: https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
"""


class Graph:
    def __init__(self, num_of_nodes: int) -> None:
        """
        Arguments:
            num_of_nodes - the number of nodes in the graph
        Attributes:
            m_v - the number of nodes in the graph.
            m_edges - the list of edges.
            m_component - the dictionary which stores the index of the component which
            a node belongs to.
        """

        self.m_v = num_of_nodes
        self.m_edges = []
        self.m_component = {}

    def add_edge(self, u_node: int, v_node: int, weight: int) -> None:
        """Adds an edge in the format [first, second, edge weight] to graph."""

        self.m_edges.append([u_node, v_node, weight])

    def find_component(self, u_node: int) -> int:
        """Propagates a new component throughout a given component."""

        if self.m_component[u_node] == u_node:
            return u_node
        return self.find_component(self.m_component[u_node])

    def set_component(self, u_node: int) -> None:
        """Finds the component index of a given node"""

        if self.m_component[u_node] != u_node:
            for k in self.m_component.keys():
                self.m_component[k] = self.find_component(k)

    def union(self, component_size: list, u_node: int, v_node: int) -> None:
        """Union finds the roots of components for two nodes, compares the components
        in terms of size, and attaches the smaller one to the larger one to form
        single component"""

        if component_size[u_node] <= component_size[v_node]:
            self.m_component[u_node] = v_node
            component_size[v_node] += component_size[u_node]
            self.set_component(u_node)

        elif component_size[u_node] >= component_size[v_node]:
            self.m_component[v_node] = self.find_component(u_node)
            component_size[u_node] += component_size[v_node]
            self.set_component(v_node)

    def boruvka(self) -> None:
        """Performs Borůvka's algorithm to find MST."""

        # Initialize additional lists required to algorithm.
        component_size = []
        mst_weight = 0

        minimum_weight_edge = [-1] * self.m_v

        # A list of components (initialized to all of the nodes)
        for node in range(self.m_v):
            self.m_component.update({node: node})
            component_size.append(1)

        num_of_components = self.m_v

        while num_of_components > 1:
            l_edges = len(self.m_edges)
            for i in range(l_edges):

                u = self.m_edges[i][0]
                v = self.m_edges[i][1]
                w = self.m_edges[i][2]

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    """If the current minimum weight edge of component u doesn't
                    exist (is -1), or if it's greater than the edge we're
                    observing right now, we will assign the value of the edge
                    we're observing to it.

                    If the current minimum weight edge of component v doesn't
                    exist (is -1), or if it's greater than the edge we're
                    observing right now, we will assign the value of the edge
                    we're observing to it"""

                    if (
                        minimum_weight_edge[u_component] == -1
                        or minimum_weight_edge[u_component][2] > w
                    ):
                        minimum_weight_edge[u_component] = [u, v, w]
                    if (
                        minimum_weight_edge[v_component] == -1
                        or minimum_weight_edge[v_component][2] > w
                    ):
                        minimum_weight_edge[v_component] = [u, v, w]

            for node in range(self.m_v):
                if minimum_weight_edge[node] != -1:
                    u = minimum_weight_edge[node][0]
                    v = minimum_weight_edge[node][1]
                    w = minimum_weight_edge[node][2]

                    u_component = self.m_component[u]
                    v_component = self.m_component[v]

                    if u_component != v_component:
                        mst_weight += w
                        self.union(component_size, u_component, v_component)
                        print(
                            "Added edge ["
                            + str(u)
                            + " - "
                            + str(v)
                            + "]\n"
                            + "Added weight: "
                            + str(w)
                            + "\n"
                        )
                        num_of_components -= 1

            minimum_weight_edge = [-1] * self.m_v
        print("The total weight of the minimal spanning tree is: " + str(mst_weight))


def test_vector() -> None:
    """
    >>> g=Graph(8)
    >>> g.add_edge(0, 1, 10)
    >>> g.add_edge(0, 2, 6)
    >>> g.add_edge(0, 3, 5)
    >>> g.add_edge(1, 3, 15)
    >>> g.add_edge(2, 3, 4)
    >>> g.add_edge(3, 4, 8)
    >>> g.add_edge(4, 5, 10)
    >>> g.add_edge(4, 6, 6)
    >>> g.add_edge(4, 7, 5)
    >>> g.add_edge(5, 7, 15)
    >>> g.add_edge(6, 7, 4)
    >>> g.boruvka()
    Added edge [0 - 3]
    Added weight: 5
    <BLANKLINE>
    Added edge [0 - 1]
    Added weight: 10
    <BLANKLINE>
    Added edge [2 - 3]
    Added weight: 4
    <BLANKLINE>
    Added edge [4 - 7]
    Added weight: 5
    <BLANKLINE>
    Added edge [4 - 5]
    Added weight: 10
    <BLANKLINE>
    Added edge [6 - 7]
    Added weight: 4
    <BLANKLINE>
    Added edge [3 - 4]
    Added weight: 8
    <BLANKLINE>
    The total weight of the minimal spanning tree is: 46
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
