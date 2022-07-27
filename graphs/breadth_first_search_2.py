"""
https://en.wikipedia.org/wiki/Breadth-first_search
pseudo-code:
breadth_first_search(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)
"""
from __future__ import annotations

from queue import Queue

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: dict, start: str) -> set[str]:
    """
    >>> ''.join(sorted(breadth_first_search(G, 'A')))
    'ABCDEF'
    """
    explored = {start}
    queue: Queue = Queue()
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.put(w)
    return explored


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(breadth_first_search(G, "A"))
