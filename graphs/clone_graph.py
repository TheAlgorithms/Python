# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: list) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors else []


# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]


def clone_graph(node: Node) -> Node:
    if node == None:
        return node
    visited = [node]
    graph = dict()
    graph[node.val] = Node(node.val, [])

    while len(visited) > 0:
        cur = visited.pop(0)
        cur_cloned = graph[cur.val]

        for ngbr in cur.neighbors:
            if ngbr.val not in graph:
                graph[ngbr.val] = Node(ngbr.val, [])
                visited.append(ngbr)
            cur_cloned.neighbors.append(graph[ngbr.val])
    return graph[node.val]
