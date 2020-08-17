from collections import defaultdict
 class Graph:
  def __init__(self):
    self.graph=defaultdict(list)
  def add_edge(self,node1,node2):  # undirected graph
    self.graph[node1].append(node2)
    self.graph[node2].append(node1)
  def print(self):
    print(self.graph)

  def breadth_first_search(self,starting_node):
    visited=[False]*len(self.graph)
    queue=[]
    queue.append(starting_node)
    visited[starting_node]=True
    while queue:
      first_inserted_element_in_queue=queue.pop(0)
      print(first_inserted_element_in_queue)
      for i in self.graph[first_inserted_element_in_queue]:
        if visited[i]!=True:
          queue.append(i)
          visited[i]=True
        
  def _depth_fitst_search(self,visited,node):
    visited[node]=True
    print(node)
    for i in self.graph[node]:
      if visited[i]!=True:
        self._depth_first_search(visited,i)
  def depth_first_search(self,node):
    visited=[False]*len(self.graph)
    self._depth_first_search(visited,node)

graph=Graph()
grap.add_edge(0,3)
graph.add_edge(0,1)
graph.add_edge(3,1)
graph.add_edge(2,1)
graph.add_edge(6,1)
graph.add_edge(3,2)
graph.add_edge(2,4)
graph.add_edge(1,5)
graph.add_edge(2,5)
