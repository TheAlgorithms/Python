from collections import defaultdict
# n = int(input("Enter number of vertices: "))
# print("Enter adjacency list: ")
# l = []
# for x in range(n):
#     l.append([int(x) for x in input().split()])

# Depth first search
def DFS(l, start, visited):
    visited[start] = 1          # This runs for all vertices (V)
    for x in l[start]:          # This for loop runs for all the edges twice (2E)
        if visited[x] == 0:
            DFS(l, x, visited)
# Time complexity = O(V + 2E) = O(V + E)

# DETECT CYCLE for Undirected Graph
def DetectCycleUDG(l, start, visited, parent):
    visited[start] = 1
    for x in l[start]:
        if visited[x] == 0:
            parent[x] = start
            if DetectCycleUDG(l, x, visited, parent) == True:
                return True
        elif parent[start] != x:
            # There exist a cycle
            return True
    return False
# Time complexity = O(V + 2E) = O(V + E)
# DESCRIPTION:
# For every visited vertex v, if there is an adjacent u such that u is already visited 
# and u is not parent of v, then there is a cycle in graph. If we dont find such an adjacent 
# for any vertex, we say that there is no cycle. The assumption of this approach is that there 
# are no parallel edges between any two vertices.

# DETECT CYCLE for Directed Graph
def DetectCycleDG(l, start, visited, recStack):
    visited[start] = 1
    for x in l[start]:
        if visited[x] == False:
            recStack[start] = True
            if DetectCycleDG(l, x, visited, recStack) == True:
                recStack[start] = False
                return True
        elif recStack[x] == True:
            return True
    return False
# Time complexity = O(V + E)
# DESCRIPTION: To detect a back edge, we can keep track of vertices currently in recursion stack
# of function for DFS traversal. If we reach a vertex that is already in the recursion stack, 
# then there is a cycle in the tree. The edge that connects current vertex to the vertex in the 
# recursion stack is a back edge. We have used recStack[] array to keep track of vertices in the 
# recursion stack.

# Find Strongly Connected Components: Kosaraju's Algorithm
def DFSTraversal_SCC(l, start, visited, stack):
    visited[start] = True
    for x in l[start]:
        if visited[x] == False:
            DFSTraversal_SCC(l, x, visited, stack)
    stack.append(start)
    
    
def SCC(l, start, n):
    visited = [False] * n
    stack = []
    DFSTraversal_SCC(l, 0, visited, stack)
    
    # l1 = Reverse of graph l
    l1 = defaultdict(list)
    for key, values in l.items():
        for x in values:
            l1[x].append(key)
    
    # Popping from stack and applying DFS in reversed graph from popped vertex
    scc = []
    visited = [False] * n
    while(len(stack) > 0):
        t = []
        DFSTraversal_SCC(l1, stack.pop(), visited, t)
        while(len(stack) > 0):
            if visited[stack[-1]] == False:
                break
            else:
                stack.pop()
        scc.append(t)
    return scc
# Time Complexity = O(k(V+E))
# DESCRIPTION: Push the vertices in stack with minimum post number first. At the end the top of
# stack will have vertex with highest post number. Reverse the graph. After reversing the source SCC
# becomes sink SCC with minimum post number. Pop the top of stack and apply DFS in reversed graph
# from that vertex. As soon as the post at that vertex ends you get your first SCC and go on popping
# from the stack.

# While Taking input take care of 3:[] -> vertex which has no outgoing edges
# l = {0:[1], 1:[2,3,4], 2:[5], 3:[], 4:[1,5,6], 5:[2,7], 6:[7,9], 7:[10], 8:[6], 9:[8], 10:[11], 11:[9]}
# print(SCC(l, 0, 12))

# <------ TARJAN'S ALGORITHM ------->

# Finding Bridges in Undirected Graph
def computeBridges(l):
    id = 0
    n = len(l) # No of vertices in graph
    low = [0] * n
    visited = [False] * n
    
    def dfs(at, parent, bridges, id):
        visited[at] = True
        low[at] = id
        id += 1
        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                dfs(to, at, bridges, id)
                low[at] = min(low[at], low[to])
                if at < low[to]:
                    bridges.append([at, to])
            else:
                # This edge is a back edge and cannot be a bridge
                low[at] = min(low[at], to)
    
    bridges = []
    for i in range(n):
        if (not visited[i]):
            dfs(i, -1, bridges, id)
    print(bridges)
            
# l = {0:[1,2], 1:[0,2], 2:[0,1,3,5], 3:[2,4], 4:[3], 5:[2,6,8], 6:[5,7], 7:[6,8], 8:[5,7]}
# computeBridges(l)

# Finding Articulation Points in Undirected Graph
def computeAP(l):
    n = len(l)
    outEdgeCount = 0
    low = [0] * n
    visited = [False] * n
    isArt = [False] * n
    
    def dfs(root, at, parent, outEdgeCount):
        if parent == root:
            outEdgeCount += 1
        visited[at] = True
        low[at] = at
        
        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                outEdgeCount = dfs(root, to, at, outEdgeCount)
                low[at] = min(low[at], low[to])
    
                # AP found via bridge
                if at < low[to]:
                    isArt[at] = True
                # AP found via cycle
                if at == low[to]:
                    isArt[at] = True
            else:
                low[at] = min(low[at], to)
        return outEdgeCount

    for i in range(n):
        if not visited[i]:
            outEdgeCount = 0
            outEdgeCount = dfs(i, i, -1, outEdgeCount)
            isArt[i] = (outEdgeCount > 1)
    
    for x in range(len(isArt)):
        if isArt[x] == True:
            print(x, end=" ")
            
# l = {0:[1,2], 1:[0,2], 2:[0,1,3,5], 3:[2,4], 4:[3], 5:[2,6,8], 6:[5,7], 7:[6,8], 8:[5,7]}
# computeAP(l)
    
# Finding topological ordering of Directed Acyclic Graph using DFS
def TopologicalSort(l):
    stack = []
    visited = [False] * len(l)
    
    def dfs(start):
        visited[start] = True
        for x in l[start]:
            if not visited[x]:
                dfs(x)
        stack.append(start)
        
    
    for i in range(len(l)):
        if not visited[i]:
            dfs(i)
    
    stack.reverse()
    print(stack)
    
# l = {0:[1,2], 1:[3], 2:[3], 3:[4,5], 4:[], 5:[]}
# TopologicalSort(l)


    
    
    
    
    
    
    
    

        
    
    
        