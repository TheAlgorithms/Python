import sys
from collections import defaultdict

class MinHeap:
    
    def __init__(self, n):
        self.distance       = [sys.maxsize] * n 
        self.positionToNode = [int(x) for x in range(n)]
        self.nodeToPosition = [int(x) for x in range(n)]
    
    def getPosition(self, vertex):
        return self.nodeToPosition[vertex]
    
    def setPosition(self, vertex, pos):
        self.nodeToPosition[vertex] = pos
    
    def getMinimum(self):
        return self.positionToNode[0]
    
    def bottomToTop(self, index):
        temp = self.positionToNode[index]
        val  = self.distance[index]
        
        while(index != 0):
            if index % 2 == 0:
                parent = int( (index-2) / 2 )
            else:
                parent = int( (index-1) / 2 )
            
            if val < self.distance[parent]:
                self.distance[index] = self.distance[parent]
                self.positionToNode[index] = self.positionToNode[parent]
                self.setPosition(self.positionToNode[parent], index)
            else:
                self.distance[index] = val
                self.positionToNode[index] = temp
                self.setPosition(temp, index)
                break 
            index = parent
        else:
            self.distance[0] = val
            self.positionToNode[0] = temp
            self.setPosition(temp, 0)
            
    def topToBottom(self, start):
        size = len(self.distance)
        if start > size // 2 - 1:
            return
        else:
            if 2 * start + 2 >= size:
                m = 2 * start + 1
            else:
                if self.distance[2 * start + 1] < self.distance[2 * start + 2]:
                    m = 2 * start + 1
                else:
                    m = 2 * start + 2
            if self.distance[m] < self.distance[start]:
                temp, temp1 = self.distance[m], self.positionToNode[m]
                self.distance[m], self.positionToNode[m] = self.distance[start], self.positionToNode[start]
                self.distance[start], self.positionToNode[start] = temp, temp1
                
                temp = self.getPosition(self.positionToNode[m])
                self.setPosition(self.positionToNode[m], self.getPosition(self.positionToNode[start]))
                self.setPosition(self.positionToNode[start], temp)
        
                self.topToBottom(m)
    
    def set(self, value, node):
        pos = self.nodeToPosition[node]
        prevVal = self.distance[pos]
        if prevVal < value:
            self.distance[pos] = value
            self.topToBottom(pos)
        elif prevVal > value:
            self.distance[pos] = value
            self.bottomToTop(pos)
    
    def get(self, node):
        return self.distance[self.nodeToPosition[node]]
        
    def heapify(self):
        start = len(self.distance) // 2 - 1        
        for i in range(start, -1, -1):
            self.topToBottom(i)
    
    def deleteMinimum(self):
        temp = self.positionToNode[0]
        self.set(sys.maxsize, temp)
        return temp
    
# Dijkstra's Algorithm - Single Source Shortest Path:
def SingleSourceSP(l, source):
    visited  = [False] * len(l)
    distance = MinHeap(len(l))
    n        = len(visited)
    ans      = [0] * n
    
    distance.set(0, source)
    
    for i in range(n):
        dist          = distance.get(distance.positionToNode[0])
        node          = distance.deleteMinimum()
        ans[node] = dist
        visited[node] = True
        for nbr in l[node]:
            if visited[nbr[0]] == False and distance.get(nbr[0]) > dist + nbr[1]:
                distance.set(dist + nbr[1], nbr[0])
    
    return ans

# Bellmann Ford Algorithm
def fn(edges, source, n):
    Distance = [int(sys.maxsize) for x in range(n)]
    Predecessor = [-1 for x in range(n)]
    Distance[source] = 0
    
    for i in range(n):
        for x in edges:
            if Distance[x[1]] > Distance[x[0]] + x[2]:
                Distance[x[1]] = Distance[x[0]] + x[2]
                Predecessor[x[1]] = x[0]
    
    
    # Checking whether a graph has negative cycle or not
    for x in edges:
        if Distance[x[1]] > Distance[x[0]] + x[2]:
                print("Graph has negative cycle")
                return
    
    # Printing path for shortest path
    print(Predecessor)
        

# Directed Graph
# n = int(input("Enter number of vertices: "))
# e = int(input("Enter number of edges: "))
# edges = []
# for x in range(e):
#     edges.append([int(x) for x in input().split()])
# fn(edges, 0, n)

# Undirected Graph  
# n = int(input("Enter number of vertices: "))
# e = int(input("Enter number of edges: "))
# adjlist = defaultdict(list)
# for x in range(e):
#     l = [int(x) for x in input().split()]
#     adjlist[l[0]].append([ l[1], l[2] ])
#     adjlist[l[1]].append([ l[0], l[2] ])
#     
# ans = SingleSourceSP(adjlist, 0)
# print("Distance from source 0 to all the nodes in graph: ")
# print(ans)
    

            
            
    
    
    
    
    