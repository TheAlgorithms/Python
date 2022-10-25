"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return node
        visited=[node]
        graph=dict()
        graph[node.val]=Node(node.val,[])

        while len(visited)>0:
            cur=visited.pop(0)
            curCloned=graph[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in graph:
                    graph[ngbr.val]=Node(ngbr.val,[])
                    visited.append(ngbr)
                curCloned.neighbors.append(graph[ngbr.val])
        return graph[node.val]

