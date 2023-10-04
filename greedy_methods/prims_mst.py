class Graph:

    def __init__(self,V):
        self.V = V
        self.graph = [[0 for i in range(self.V)] for j in range(self.V)]
    

    def minIdx(self,key,mstSet):
        min = float('inf')
        for v in range(self.V):
            if key[v]<min and v not in mstSet:
                min = key[v]
                idx=v
        return idx
    
    def printMST(self,parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
    
    def MST(self):
        maxval = float('inf')
        mstSet = set()
        parent = [None]*self.V
        keys = [maxval]*self.V
        keys[0] = 0
        for v in range(self.V):

            u = self.minIdx(keys,mstSet)
            mstSet.add(u)

            for neighbor in range(self.V):

                if self.graph[u][neighbor]>0 and neighbor not in mstSet and keys[neighbor]>self.graph[u][neighbor]:
                    keys[neighbor] = self.graph[u][neighbor]
                    parent[neighbor] = u
        self.printMST(parent)
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

g.MST()