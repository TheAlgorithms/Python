"""
Implements a graph in the form of adjacency matrix by using nested lists.
A graph with vertex starting from 1.
"""
class Graph:
    def __init__(self,size):
        self.adj= [[0]*size for i in range(size)]
        self.size=size

    def add_edge(self,orig , dest):
        if orig>self.size or dest>self.size or orig<1 or dest<1:
            print("Invalid Edge")
        else:
            self.adj[orig-1][dest-1]=1
        #Considering we have an undirected graph otherwise dont include this line    self.adj[dest-1][orig-1]=1  

    def remove_edge(self, orig, dest):
        if orig>self.size or dest>self.size or orig<1 or dest<1:
            print("Invalid Edge")
        else:
            self.adj[orig-1][dest-1]=0
        #IF we have an undirected graph otherwise dont include this line "self.adj[dest-1][orig-1]=0"
    
    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print(f'{val} ',end=" ")
        print()

    def all_vertices(self):
        print()
        print(set([i for j in range(1,self.size+1) for i in range(1,self.size+1) if self.adj[i-1][j-1]==1]))
    
    def all_edges(self):
        print()
        print([(i,j) for j in range(1,self.size+1) for i in range(1,self.size+1) if self.adj[i-1][j-1]==1])
    

def test_graph() -> None:
        """
        >>> test_graph()
        """
        adjmatrix = Graph(5)
        try:
            try:
                adjmatrix.add_edge(1,6)
                assert False
            except IndexError:
                assert True
        
            try:
                adjmatrix.add_edge(0,6)
                assert False 
            except IndexError:
                assert True          #Graph starts with index one for user

            try:
                adjmatrix.remove_edge(0,6)
                assert False
            except IndexError:
                assert True


        finally:
            adjmatrix.add_edge(2,3)
            adjmatrix.add_edge(4,1)
            adjmatrix.add_edge(3,3)
            adjmatrix.display()
            adjmatrix.all_vertices()
            adjmatrix.all_edges()



if __name__ == "__main__":
        test_graph()
