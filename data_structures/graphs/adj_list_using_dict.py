"""
Dictionary in python is the most suitable builtin data structure for graph implementaion similar to map in c++.
Keys of the dictionary represent the nodes of the graph.
"""


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  #values for keys , i.e.,node are a list of dest

    def add_edge(self,u,v):
        (self.graph)[u].append(v)
    
    def remove_edge(self,u,v):
        if len(self.graph[u])>1 :
            self.graph[u].remove(v)
        else:
            del self.graph[u]

    def all_edges(self):
        edges=[]
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node,neighbour))
        print(edges)

    def display(self):
        for key,value in (self.graph).items():
            print(f"{key}:",end=" ")
            print(*value,sep=" ")

def test_graph():
   """
    >>> graph= Graph()
    >>> for i in range(5):
    ...     graph.add_edge(i,i+1)
    >>> graph.all_edges()
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    >>> graph.remove_edge(3,4)
    >>> graph.display()
    0: 1
    1: 2
    2: 3
    4: 5
    """

if __name__== "__main__":
    from collections import defaultdict
    import doctest
    doctest.testmod()
