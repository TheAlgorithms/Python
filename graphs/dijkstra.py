"""
pseudo-code

DIJKSTRA(graph G, start vertex s, destination vertex d):

//all nodes initially unexplored

1 -  let H = min heap data structure, initialized with 0 and s [here 0 indicates
     the distance from start vertex s]
2 -  while H is non-empty:
3 -    remove the first node and cost of H, call it U and cost
4 -    if U has been previously explored:
5 -      go to the while loop, line 2 //Once a node is explored there is no need
         to make it again
6 -    mark U as explored
7 -    if U is d:
8 -      return cost // total cost from start to destination vertex
9 -    for each edge(U, V): c=cost of edge(U,V) // for V in graph[U]
10 -     if V explored:
11 -       go to next V in line 9
12 -     total_cost = cost + c
13 -     add (total_cost,V) to H

You can think at cost as a distance where Dijkstra finds the shortest distance
between vertices s and v in a graph G. The use of a min heap as H guarantees
that if a vertex has already been explored there will be no other path with
shortest distance, that happens because heapq.heappop will always return the
next vertex with the shortest distance, considering that the heap stores not
only the distance between previous vertex and current vertex but the entire
distance between each vertex that makes up the path from start vertex to target
vertex.
"""

import heapq


def dijkstra(graph, start, end):
    """Return the cost of the shortest path between vertices start and end.

    >>> dijkstra(G, "E", "C")
    6
    >>> dijkstra(G2, "E", "F")
    3
    >>> dijkstra(G3, "E", "F")
    3
    """

    heap = [(0, start)]  # cost from start node,end node
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            next_item = cost + c
            heapq.heappush(heap, (next_item, v))
    return -1


G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}

r"""
Layout of G2:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    ----------------- 3 --------------------
"""
G2 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["F", 3]],
    "F": [],
}

r"""
Layout of G3:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    -------- 2 ---------> G ------- 1 ------
"""
G3 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}

short_distance = dijkstra(G, "E", "C")
print(short_distance)  # E -- 3 --> F -- 3 --> C == 6

short_distance = dijkstra(G2, "E", "F")
print(short_distance)  # E -- 3 --> F == 3

short_distance = dijkstra(G3, "E", "F")
print(short_distance)  # E -- 2 --> G -- 1 --> F == 3

if __name__ == "__main__":
    import doctest

    doctest.testmod()
