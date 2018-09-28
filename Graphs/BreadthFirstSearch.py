from collections import defaultdict

# Breadth First Search
def BreadthFirstSearch(l):
    visited = [False] * len(l)
    queue = []
    
    def BFS():
        p = queue.pop(0)
        visited[p] = True
        
        for neighbours in l[p]:
            if not visited[neighbours]:
                queue.append(neighbours)   
    
    for i in range(l):
        if not visited[i]:
            queue.append(i)
            BFS()
        

# Finding Topological ordering of Directed Acyclic Graph using BFS
# Kahn's Algorithm
def topologicalSort(l):
    indegree = [0] * len(l)
    queue = []
    topo = []
    cnt = 0
    
    for key, values in l.items():
        for i in values:
            indegree[i] += 1
        
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            
    while(queue):
        vertex = queue.pop(0)
        cnt += 1
        topo.append(vertex)
        for x in l[vertex]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)
        
    if cnt != len(l):
        print("Cycle exists")
    else:    
        print(topo)
            
# l = {0:[1,2], 1:[3], 2:[3], 3:[4,5], 4:[], 5:[]}
# topologicalSort(l)

# Finding longest distance in DAG using above algorithm
def longestDistance(l):
    indegree = [0] * len(l)
    queue = []
    longDist = [1] * len(l)
    
    for key, values in l.items():
        for i in values:
            indegree[i] += 1
        
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
    
    while(queue):
        vertex = queue.pop(0)
        for x in l[vertex]:
            indegree[x] -= 1
            
            if longDist[vertex] + 1 > longDist[x]:
                longDist[x] =  longDist[vertex] + 1
    
            if indegree[x] == 0:
                queue.append(x)
                
    print(max(longDist))
    
# l = {0:[2,3,4], 1:[2,7], 2:[5], 3:[5,7], 4:[7], 5:[6], 6:[7], 7:[]}
# longestDistance(l)
    
# Check whether Graph is Bipartite or Not using BFS

# A Bipartite Graph is a graph whose vertices can be divided into two independent sets, 
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex 
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, 
# or u belongs to V and v to U. We can also say that there is no edge that connects 
# vertices of same set.
def checkBipartite(l):
    queue = []
    visited = [False] * len(l)
    color = [-1] * len(l)
    
    def bfs():
        while(queue):
            u = queue.pop(0)
            visited[u] = True
            
            for neighbour in l[u]:
                
                if neighbour == u:
                    return False
                
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[u]
                    queue.append(neighbour)
                    
                elif color[neighbour] == color[u]:
                    return False
            
        return True
    
    for i in range(len(l)):
        if not visited[i]:
            queue.append(i)
            color[i] = 0
            if bfs() == False:
                return False
    
    return True

# l = {0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2]}
# print(checkBipartite(l))
    
    
    
    
    
    
    
    


