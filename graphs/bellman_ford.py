class Graph:
  def __init__(self,vertices):
    self.v=vertices
    self.graph=[]
  def addEdge(self,u,v,w):
    self.graph.append([u,v,w])
  def BellmanFord(self,source):
    dic=[float("Inf")]*self.v
    dic[source]=0

    for i in range(self.v-1):
      for u,v,w in self.graph:
        if dic[u]!=float("Inf") and dic[u]+w<dic[v]:
          dic[v]=dic[u]+w
    
    for u,v,w in self.graph:
      if dic[u]!=float("Inf") and dic[u]+w<dic[v]:
        print("Negative cycle found")
        return
    
    self.printPath(dic)
  def printPath(self,dic):
    print("Vertex Distance from source")
    for i in range(len(dic)):
      print("%d \t\t %d" %(i,dic[i]))

g = Graph(7) 
g.addEdge(0,1, 6) 
g.addEdge(0,2, 5) 
g.addEdge(0,3, 5) 
g.addEdge(1,4, -1) 
g.addEdge(3,2, -2) 
g.addEdge(2,1, -2) 
g.addEdge(4,6, 3) 
g.addEdge(5,6, 3) 
g.addEdge(3,5, -1) 
g.addEdge(2,4, 1) 


g.BellmanFord(0) 
