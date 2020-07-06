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
from typing import Dict, Set

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: Dict, start: str) -> Set[str]:
    """
    >>> ''.join(sorted(breadth_first_search(G, 'A')))
    'ABCDEF'
    """
    explored = {start}
    queue = [start]
    while queue:
        v = queue.pop(0)  # queue.popleft()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.append(w)
    return explored


if __name__ == "__main__":
    print(breadth_first_search(G, "A"))
