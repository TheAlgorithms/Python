"""pseudo-code"""

"""
DFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
for every edge (s, v):
    if v unexplored:
        DFS(G, v)
"""


def dfs(graph, start):
    """The DFS function simply calls itself recursively for every unvisited child of its argument. We can emulate that
     behaviour precisely using a stack of iterators. Instead of recursively calling with a node, we'll push an iterator
      to the node's children onto the iterator stack. When the iterator at the top of the stack terminates, we'll pop
       it off the stack."""
    explored, stack = set(), [start]
    explored.add(start)
    while stack:
        v = stack.pop()  # one difference from BFS is to pop last element here instead of first one
        
        if v in explored:
            continue

        explored.add(v)

        for w in graph[v]:
            if w not in explored:
                stack.append(w)
    return explored


G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

print(dfs(G, 'A'))
