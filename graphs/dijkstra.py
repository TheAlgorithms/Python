"""
pseudo-code

DIJKSTRA(graph G, start vertex s, destination vertex d):

// all nodes initially unexplored

1 -  let H = min heap data structure, initialized with (0, s)
     // 0 is the distance from start vertex s
2 -  let costs = dictionary to store minimum costs to reach each node,
     initialized with {s: 0}
3 -  while H is non-empty:
4 -    remove the first node and cost from H, call them U and cost
5 -    if U has been previously explored:
6 -      continue // skip further processing and go back to while loop, line 3
7 -    mark U as explored
8 -    if U is d:
9 -      return cost // total cost from start to destination vertex
10 -   for each neighbor V and edge cost c of U in G:
11 -     if V has been previously explored:
12 -       continue to next neighbor V in line 10
13 -     total_cost = cost + c
14 -     if total_cost is less than costs.get(V, ∞):
15 -       update costs[V] to total_cost
16 -       add (total_cost, V) to H

// At the end, if destination d is not reachable, return -1

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


def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str, end: str) -> int:
    """Return the cost of the shortest path between vertices start and end.

    >>> dijkstra(G, "E", "C")
    6
    >>> dijkstra(G2, "E", "F")
    3
    >>> dijkstra(G3, "E", "F")
    3
    """
    heap: list[tuple[int, str]] = [(0, start)]  # (cost, node)
    visited: set[str] = set()
    costs: dict[str, int] = {start: 0}  # Store minimum costs to reach each node

    while heap:
        cost, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost

        for v, c in graph[u]:
            if v in visited:
                continue
            next_cost = cost + c
            # Only push to heap if a cheaper path is found
            if next_cost < costs.get(v, float("inf")):
                costs[v] = next_cost
                heapq.heappush(heap, (next_cost, v))

    return -1


G = {
    "A": [("B", 2), ("C", 5)],
    "B": [("A", 2), ("D", 3), ("E", 1), ("F", 1)],
    "C": [("A", 5), ("F", 3)],
    "D": [("B", 3)],
    "E": [("B", 4), ("F", 3)],
    "F": [("C", 3), ("E", 3)],
}

r"""
Layout of G2:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    ----------------- 3 --------------------
"""
G2 = {
    "B": [("C", 1)],
    "C": [("D", 1)],
    "D": [("F", 1)],
    "E": [("B", 1), ("F", 3)],
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
    "B": [("C", 1)],
    "C": [("D", 1)],
    "D": [("F", 1)],
    "E": [("B", 1), ("G", 2)],
    "F": [],
    "G": [("F", 1)],
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
