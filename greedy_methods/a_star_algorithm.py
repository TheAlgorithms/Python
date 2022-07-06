"""
URL reference to A* algorithm: https://en.wikipedia.org/wiki/A*_search_algorithm
"""


def a_star(start_vertex, vertex_target):
    """
    STEP 1: Firstly, add the beginning node to the open list
    STEP 2: Then repeat the following step
        – In the open list, find the square with the lowest F cost – and this denotes the current square.
        – Now we move to the closed square.
        – Consider 8 squares adjacent to the current square and :
            + Ignore it if it is on the closed list, or if it is not workable. Do the following if it is workable
            + Check if it is on the open list; if not, add it. You need to make the current square as this square’s a parent. You will now record the different costs of the square like the F, G and H costs.
            + If it is on the open list, use G cost to measure the better path. Lower the G cost, the better the path. If this path is better, make the current square as the parent square. Now you need to recalculate the other scores – the G and F scores of this square.
        – You’ll stop:
            + If you find the path, you need to check the closed list and add the target square to it.
            + There is no path if the open list is empty and you could not find the target square.
    STEP 3: Now you can save the path and work backwards starting from the target square, going to the parent square from each square you go, till it takes you to the starting square. You’ve found your path now.
    """
    open_set = set(start_vertex)
    closed_set = set()
    dist_from_startnode = {}
    parents = {}

    dist_from_startnode[start_vertex] = 0
    parents[start_vertex] = start_vertex

    while len(open_set) > 0:
        x = None
        for v in open_set:
            if x is None or dist_from_startnode[v] + heuristic(v) < dist_from_startnode[
                x
            ] + heuristic(x):
                x = v

        if x == vertex_target or Nodes[x] is None:
            pass
        else:
            for (y, weight) in get_neighbors(x):
                if y not in open_set and y not in closed_set:
                    open_set.add(y)
                    parents[y] = x
                    dist_from_startnode[y] = dist_from_startnode[x] + weight
                else:
                    if dist_from_startnode[y] > dist_from_startnode[x] + weight:
                        dist_from_startnode[y] = dist_from_startnode[x] + weight
                        parents[y] = x
                        if y in closed_set:
                            closed_set.remove(y)
                            open_set.add(y)

        if x is None:
            print("Path does not exist!")
            return None

        # if the current node is the vertex_target
        # then we begin reconstruct in the path from it to the start_vertex
        if x == vertex_target:
            path = []

            while parents[x] != x:
                path.append(x)
                x = parents[x]

            path.append(start_vertex)

            path.reverse()

            print(f"Path found: {path}")
            return path
        open_set.remove(x)
        closed_set.add(x)

    print("Path does not exist!")
    return None


def get_neighbors(v):
    if v in Nodes:
        return Nodes[v]
    else:
        return None


def heuristic(n):
    h_distance = {
        "A": 11,
        "B": 6,
        "C": 99,
        "D": 1,
        "E": 7,
        "G": 0,
    }
    return h_distance[n]


Nodes = {
    "A": [("B", 2), ("E", 3)],
    "B": [("C", 1), ("G", 9)],
    "C": None,
    "E": [("D", 6)],
    "D": [("G", 1)],
}

if __name__ == "__main__":
    a_star("A", "G")
