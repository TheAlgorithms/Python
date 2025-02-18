class dijkstra_2:
    """
    Test Case One with 4 Vertices and 4 Edges all with Weights of Zero
    >>> testOne = dijkstra_2(4,4, True)
    >>> testOne.add_edge(0,1,0)
    >>> testOne.add_edge(1,2,0)
    >>> testOne.add_edge(2,3,0)
    >>> testOne.add_edge(3,0,0)
    >>> testOne.dijkstra(testOne.get_graph(),4,0) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Vertex Distance
    0    0
    1    0
    2    0
    >>> testTwo = dijkstra_2(8,10,True)
    >>> testTwo.add_edge(0,2,8)
    >>> testTwo.add_edge(2,1,3)
    >>> testTwo.add_edge(2,4,5)
    >>> testTwo.add_edge(2,5,6)
    >>> testTwo.add_edge(1,6,2)
    >>> testTwo.add_edge(4,6,7)
    >>> testTwo.add_edge(4,7,6)
    >>> testTwo.add_edge(5,7,6)
    >>> testTwo.add_edge(6,7,8)
    >>> testTwo.add_edge(7,3,4)
    >>> testTwo.dijkstra(testTwo.get_graph(),8,0) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Vertex Distance
    0    0
    1    11
    2    8
    3    23
    4    13
    5    14
    6    13
    >>> testThree = dijkstra_2(8,5,True)
    >>> testThree.add_edge(0,1,8)
    >>> testThree.add_edge(3,5,3)
    >>> testThree.add_edge(5,2,2)
    >>> testThree.add_edge(2,6,3)
    >>> testThree.add_edge(6,7,7)
    >>> testThree.add_edge(4,4,0)
    >>> testThree.dijkstra(testThree.get_graph(),8,0) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Vertex Distance
    0    0
    1    8
    2    INF
    3    INF
    4    INF
    5    INF
    6    INF
    >>> testFour = dijkstra_2(18,24,True)
    >>> testFour.add_edge(0,7,8)
    >>> testFour.add_edge(0,4,4)
    >>> testFour.add_edge(1,4,2)
    >>> testFour.add_edge(4,5,6)
    >>> testFour.add_edge(4,7,4)
    >>> testFour.add_edge(4,8,9)
    >>> testFour.add_edge(7,11,6)
    >>> testFour.add_edge(11,15,3)
    >>> testFour.add_edge(5,8,6)
    >>> testFour.add_edge(8,9,1)
    >>> testFour.add_edge(8,12,8)
    >>> testFour.add_edge(9,12,2)
    >>> testFour.add_edge(9,6,3)
    >>> testFour.add_edge(6,3,9)
    >>> testFour.add_edge(3,2,6)
    >>> testFour.add_edge(6,10,8)
    >>> testFour.add_edge(9,10,2)
    >>> testFour.add_edge(3,17,5)
    >>> testFour.add_edge(10,17,6)
    >>> testFour.add_edge(17,13,3)
    >>> testFour.add_edge(17,16,2)
    >>> testFour.add_edge(13,16,3)
    >>> testFour.add_edge(16,12,6)
    >>> testFour.add_edge(16,15,4)
    >>> testFour.add_edge(12,15,1)
    >>> testFour.add_edge(15,14,4)
    >>> testFour.dijkstra(testFour.get_graph(),18,0) #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Vertex Distance
    0    0
    1    6
    2    32
    3    26
    4    4
    5    10
    6    17
    7    8
    8    13
    9    14
    10   16
    11   14
    12   16
    13   24
    14   21
    15   17
    16   21
    >>> testFive = dijkstra_2(8,8,True)
    >>> testFive.add_edge(1.5,1,8)
    Source must be an integer
    >>> testFive.add_edge(1,1.5,8)
    Destination must be an integer
    >>> testFive.add_edge (1, 1, -1)
    Weight must be positive
    """

    def __init__(self, V, E, testing):
        self.graph = [[float("inf") for i in range(V)] for j in range(V)]
        for i in range(V):
            self.graph[i][i] = 0.0
        if not testing:
            index = 0
            while index < E:
                print("\nEdge ", index + 1)
                src = input("Enter source:").strip()
                if not src.isdigit() or int(src) < 0 or int(src) >= V:
                    print(
                        "\nSource must be an positive integer within the bounds of the (# of vertices - 1) (Try again)\n"
                    )
                    continue
                dst = input("Enter destination:").strip()
                if not dst.isdigit() or int(dst) < 0 or int(dst) >= V:
                    print(
                        "\nDestination must be a positive integer within the bounds of the (# of vertices - 1) (Try again)\n"
                    )
                    continue
                weight = input("Enter weight:").strip()
                if not weight.isdigit() or float(weight) < 0:
                    print("\nWeight must be positive integer (Try Again)\n")
                    continue
                self.add_edge(int(src), int(dst), float(weight))
                index += 1
            gsrc = int(input("\nEnter shortest path source:").strip())
            self.dijkstra(self.graph, V, gsrc)

    def get_graph(self):
        return self.graph

    def add_edge(self, src, dst, weight):
        if weight < 0:
            print("Weight must be positive")
            return
        if not src.is_integer():
            print("Source must be an integer")
            return
        if not dst.is_integer():
            print("Destination must be an integer")
            return
        self.graph[src][dst] = weight
        self.graph[dst][src] = weight

    def print_dist(self, dist, v):
        print("\nVertex Distance")
        for i in range(v):
            if dist[i] != float("inf"):
                print(i, "\t", int(dist[i]), end="\t")
            else:
                print(i, "\t", "INF", end="\t")
            print()

    def min_dist(self, mdist, vset, v):
        min_val = float("inf")
        min_ind = -1
        for i in range(v):
            if (not vset[i]) and mdist[i] < min_val:
                min_ind = i
                min_val = mdist[i]
        return min_ind

    def dijkstra(self, graph, v, src):
        mdist = [float("inf") for _ in range(v)]
        vset = [False for _ in range(v)]
        mdist[src] = 0.0

        for _ in range(v - 1):
            u = self.min_dist(mdist, vset, v)
            vset[u] = True

            for i in range(v):
                if (
                    (not vset[i])
                    and graph[u][i] != float("inf")
                    and mdist[u] + graph[u][i] < mdist[i]
                ):
                    mdist[i] = mdist[u] + graph[u][i]

        self.print_dist(mdist, i)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())
    calculateShortest = dijkstra_2(V, E, False)
