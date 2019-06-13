# https://projecteuler.net/problem=81
from collections import defaultdict

class graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        
    def add_node(self,value):
        self.nodes.add(value)

    def add_edge(self,from_node, to_node ):
        self.edges[from_node].append(to_node)
        
        

def dijkstra(initial,graph):
    visited=[]
    valid=[initial]
    path={initial:initial}
    while len(valid)>0:
        current = min(valid,key=lambda x: path[x])
        visited.append(current)
        valid.remove(current)
        for node in graph.edges[current]:
            if node not in valid and node not in visited:
                valid.append(node)
            else:
                pass
            if node not in path:
                path[node]=path[current]+node
            else:
                if path[node]>(path[current]+node):
                    path[node]=path[current]+node
    return path

with open('input.txt') as in_file:
    matrix = [[int(x) for x in line.split(',')] for line in in_file]
in_file.close()
                                         
#.   d{} which counts repeated node's frequency
#.   matrix1 is used to calculate

d={}                                     
    for node in range(80):
        jup=0
        for k in matrix:
            l=k.count(matrix[_][node])
            jup+=l
        if jup > 1:
            d[matrix[_][node]]=jup

matrix2=[]
f2=open('input.txt','r')
for lin in f2:
    lin=lin.split(',')                #.   matrix2 gets rid of repeated nodes
    lin=list(map(int,lin))
    for p in range(len(lin)):
        if lin[p] in d:
            d[lin[p]]-=1
            lin[p]=lin[p]+ ((d[lin[p]]+1)/10000)
    matrix2.append(lin)
f2.close()

G=graph()

#. Adding edges of of non boundry nodes on matrix2
#. All the edges according to the problem is
for _ in range(0,len(matrix2)-1):
    for node in range(0,len(matrix2[_])-1):
        G.add_node(matrix2[_][node])
        G.add_edge(matrix2[_][node],matrix2[_][node+1])
        G.add_edge(matrix2[_][node],matrix2[_+1][node])

for node in range(0,len(matrix2)-1):
    G.add_node(matrix2[79][node])
    G.add_edge(matrix2[79][node],matrix2[79][node+1])

for node in range(0,len(matrix2)-1):
    G.add_node(matrix2[node][79])
    G.add_edge(matrix2[node][79],matrix2[node+1][79])

a=dijkstra(matrix2[0][0],G)
print(int(a[matrix2[-1][-1]]))
