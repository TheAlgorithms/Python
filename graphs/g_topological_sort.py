def topological_sort(jobs, deps):
    g = Graph(jobs, deps)
    visited = {}
    finished = []
    for s in jobs:          
        if s not in visited:
            parent_nodes = [False for el in range(len(jobs) + 1)]
            visited, finished = DFS_rec(s, g, visited, finished, parent_nodes)
            if visited == None and finished == None:        # there's a cycle
                return []
    return list(reversed(finished))

def DFS_rec(s, g, visited, finished, parent_nodes):
    parent_nodes[s] = True
    visited[s] = True
    if s in g.adj:
        for v in g.adj[s]:
            if parent_nodes[v]:
                return None, None
            if v not in visited:
                visited, finished = DFS_rec(v, g, visited, finished, parent_nodes)
            if visited == None and finished == None:        # there's a cycle
                return None, None            
    finished.append(s)
    parent_nodes[s] = False
    return visited, finished

class Graph:
    def __init__(self, jobs, deps):
        self.adj = {}
        for edge in deps:
            v, u = edge[0], edge[1]
            if v not in self.adj:
                self.adj[v] = [u]
            else:
                self.adj[v].append(u)
                
if __name__ == '__main__':
    jobs = [1, 2, 3, 4, 5, 6, 7, 8]
    deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]
    print(topological_sort(jobs, deps))
