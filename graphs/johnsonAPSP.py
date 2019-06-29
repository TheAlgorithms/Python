#The issue with dijkstra's algorithm is that it won't work for negative edge weights but the johnson's algorithm aims to bypass the issue by reweighting the edges such that all edges become non negative and so we can apply dijkstra's. How this works is that we take a new vertex and connect it to all existing vertices and weigh the edges connecting them to 0. Then we run Bellman-Ford which from the new vertex. Then we reweigh the weight such that new weight = old weight + minDist(u)-minDist(v) where edge is from u to v. After reweighing we get all edge weights as non negative. Now we can run Dijkstra's taking each vertex as a source.

import math

def fillEdges():	
    for edge in range(numEdge):
	print('input 3 numbers:starting vertex, ending vertex, weight')
	    u, v, w=input().split()
	    edges.append((int(u), int(v), int(w)))

def fillGraph():
    for edge in newEdges:
	u=edge[0]
	v=edge[1]
	w=edge[2]
	if len(str(adjList[int(u)]))>0:
	    adjList[int(u)].append((int(v), int(w)))
	else:
	    adjList[int(u)]=(int(v), int(w))

def bellFord(source):
    minDist[source]=0
    for outer in range(numVert):
	for edge in edges:
	    if minDist[int(edge[1])]>minDist[int(edge[0])]+int(edge[2]):
		minDist[int(edge[1])]=minDist[int(edge[0])]+int(edge[2])

def reWeigh():
    for edge in edges:
	newEdges.append((edge[0], edge[1], edge[2]+minDist[edge[0]]-minDist[edge[1]]))

def dijk(src):
    ans=[math.inf]*(numVert+1)
    ans[src]=0
    pq=[]
    pq.append((0, src))
    while len(pq)>0:
	pq.sort()
	u=pq[0][1]
	del pq[0]
	for tup in adjList[u]:
	    if ans[tup[0]]>ans[u]+tup[1]:
		ans[tup[0]]=ans[u]+tup[1]
		pq.append((ans[tup[0]], tup[0]))
    print('This is the shortest path of all vertices from {}:{}'.format(src, ans[1:]))

numVert=5
numEdge=10
adjList = {new_list: [] for new_list in range(1,numVert+2)} 
print('initialised graph')
edges=[]
fillEdges()
print('filled edges')
minDist=[math.inf]*(numVert+2)
for i in range(1, numVert+1):
    edges.append((int(numVert+1), i, 0))
bellFord(numVert+1)
newEdges=[]
del edges[numEdge:len(edges)]
reWeigh()
print('reweighing done')
fillGraph()
print('filled graph')
minDist=[math.inf]*(numVert+2)
for src in range(1, numVert+1):
    dijk(src)
