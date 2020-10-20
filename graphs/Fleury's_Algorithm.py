from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        '''
        Initiating number of vertices
        '''
        self.graph = defaultdict(list)
        '''
        Default dictionary for graph
        '''
        self.Time = 0

    def addEdge(self, u, v):
        """
        Function to add edges to the graph
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def rmvEdge(self, u, v):
        """
        Remove u-v edge from the graph
        """
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def DFSCount(self, v, visited):
        """
        A DFS based function to count reachable vertices from v
        """
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count = count + self.DFSCount(i, visited)
        return count

    def isValidNextEdge(self, u, v):
        """
        The function to check if edge u-v can be considered as next edge in
         Euler Tour
        """

        if len(self.graph[u]) == 1:
            return True
        else:
            visited = [False] * self.V
            count1 = self.DFSCount(u, visited)

            self.rmvEdge(u, v)
            visited = [False] * self.V
            count2 = self.DFSCount(u, visited)

            self.addEdge(u, v)

            return False if count1 > count2 else True

    def printEulerUtil(self, u):
        """
        To print the elular tour
        """
        for v in self.graph[u]:
            if self.isValidNextEdge(u, v):
                print("%d-%d " % (u, v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)

    def printEulerTour(self):
        """
        The main function that print Eulerian Trail. It first finds an odd
        degree vertex (if there is any) and then calls printEulerUtil()
        to print the path
        """
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        print("\n")
        self.printEulerUtil(u)


if __name__ == "__main__":
    '''
    Driver code
    '''
    g1 = Graph(4)
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)
    g1.printEulerTour()

    g2 = Graph(3)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 0)
    g2.printEulerTour()

    g3 = Graph(5)
    g3.addEdge(1, 0)
    g3.addEdge(0, 2)
    g3.addEdge(2, 1)
    g3.addEdge(0, 3)
    g3.addEdge(3, 4)
    g3.addEdge(3, 2)
    g3.addEdge(3, 1)
    g3.addEdge(2, 4)
    g3.printEulerTour()
