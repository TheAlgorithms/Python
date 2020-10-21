graph={

    0: [1],
    1: [0,2],
    2: [1],
    3: [4],
    4:[3]

}

visited=[0 for i in range(len(graph))]

queue=[]

path=[]

def BFS(start):
    queue.append(start)
    visited[start]=1

    while len(queue)!=0:
        c=queue.pop(0)
        path.append(c)
        for i in graph[c]:
            if visited[i]!=1:
                visited[i]=1
                queue.append(i)

def conn_comp():

	count=0
	
	for i in range(len(visited)):
	    if visited[i]!=1:
		BFS(i)
		path.clear()
		count+=1
	return count



conn_comp()
