from collections import defaultdict

class Graph:

  def __init__(self,no_of_vertices,list_of_v):
    self.no_of_vertices = no_of_vertices
    self.graph = defaultdict(list)
    for v in list_of_v:
      self.graph[v] = []

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def isSink(self):
    keys = list(self.graph.keys())

    for i in keys:
      if(self.graph[i]==[]):
        flag = 0
        for j in keys:
          if(i!=j):
            if(not (i in self.graph[j])):
              flag = 1
              break
        if(flag==0):
          return True
        else:
          return False
    return False

g = Graph(4,["A","B","C","D"])

g.addEdge("A","B")
g.addEdge("B","C")
g.addEdge("A","D")
g.addEdge("B","D")
g.addEdge("C","D")
g.addEdge("C","A")

print(g.isSink())