#0/1 BFS
#if graph contain edge weight like 0/1 then 0/1 BFS can be used t find the shortest distance
#Dequeue data structure
#if distance is less as compared to already present in queue, append at front i.e left and if distance is more as compared to alredy present distancw in queue append at back i.e right
from collections import deque
from collections import defaultdict
import sys


class Graph:
 
    def __init__(self,vertices):
    
        # No. of vertices
        self.V= vertices #No. of vertices
        
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        

 
    # Function to add an edge to graph
    def addEdge(self,v,w,d):
      
        #Add w to v_s list
        self.graph[v].append([w,d])
        
         #Add v to w_s list
        self.graph[w].append([v,d])
 
    def print1(self):
        print(self.graph)

    def bfs01(self,source) :
        dq = deque()
        dist=[10000]*(self.V)
        dist[source]=0
        l=[source,0]
        dq.append(l)
        while len(dq)!=0:
            print(dq)
            node=dq[0][0]
            source=dq[0][1]
            dq.popleft()
            for i in self.graph[node]:
                n=i[0]
                d=i[1]
                if (d+dist[node])<dist[n]:
                    dist[n]=d+dist[node]
                    if d==1:
                        dq.append([n,dist[n]])
                    else:
                        dq.appendleft([n,dist[n]])
        for k in range(0,len(dist)):
            print(dist[k])
g = Graph(6)
g.addEdge(0, 1 ,0)
g.addEdge(0, 2, 1)
g.addEdge(1, 2, 1)
g.addEdge(1, 4, 1)
g.addEdge(2, 3,1)
g.addEdge(4,3,1)
g.addEdge(4,5,0)
g.addEdge(3,5,1)
g.print1()
g.bfs01(0)
 