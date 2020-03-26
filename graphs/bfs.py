"""
BFS.

pseudo-code:

BFS(graph G, start vertex s):
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

G = {
    "A": ["B", "E", "C"],
    "B": ["A", "F", "C"],
    "C": ["A", "B", "E", "I", "H"],
    "D": ["F"],
    "E": ["A", "C"],
    "F": ["G", "D", "B"],
    "G": ["F"],
    "H": ["I", "C"],
    "I": ["H", "C"]
}


def bfs(graph, start):
    """
    >>> ''.join(sorted(bfs(G, 'A')))
    'ABCDEF'
    """
    explored, queue = [start], [start]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in explored:
                explored.append(w)
                queue.append(w)
    return explored


if __name__ == "__main__":
    print(bfs(G, "A"))
