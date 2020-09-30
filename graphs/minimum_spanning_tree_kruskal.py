# Kruskal's algorithm for Minimum Spanning Tree in Python

from dataclasses import dataclass, field

@dataclass
class Edge :
   src : int
   dst : int
   weight : int

@dataclass
class Graph :

    num_nodes : int
    edgelist : list
    parent : list = field(default_factory = list)
    rank : list = field(default_factory = list)

    # mst stores edges of the minimum spanning tree
    mst : list = field(default_factory = list)

    def FindParent(self, node) :

        if self.parent[node] == node :
           return node
        return self.FindParent(self.parent[node])

    def KruskalMST(self) :

        # Sort objects of an Edge class based on attribute (weight)
        self.edgelist.sort(key=lambda Edge : Edge.weight)

        self.parent = [None] * self.num_nodes
        self.rank   = [None] * self.num_nodes

        for n in range(self.num_nodes) :
            self.parent[n] = n # Every node is the parent of itself at the beginning
            self.rank[n] = 0   # Rank of every node is 0 at the beginning

        for edge in self.edgelist :
            root1 = self.FindParent(edge.src)
            root2 = self.FindParent(edge.dst)

            # Parents of the source and destination nodes are not in the same subset
            # Add the edge to the spanning tree
            if root1 != root2 :
               self.mst.append(edge)
               if self.rank[root1] < self.rank[root2] :
                  self.parent[root1] = root2
                  self.rank[root2] += 1
               else :
                  self.parent[root2] = root1
                  self.rank[root1] += 1

        print("Edges of minimum spanning tree are in Graph 1 :", end=' ')
        cost = 0
        for edge in self.mst :
            print("[" + str(edge.src) + "-" + str(edge.dst) + "](" + str(edge.weight) + ")", end = ' ')
            cost += edge.weight
        print("\nCost of minimum spanning tree : " +str(cost))

def main() :

    # Edge(source, destination, weight)
    num_nodes = int(input("Enter the number of nodes : "))
    edges=[]
    for i in range(num_nodes):
        s=int(input("Enter the source: "))
        d=int(input("Enter the destination: "))
        w=int(input("Enter the weight: "))
        edges.append(Edge(s,d,w))

    g = Graph(num_nodes, edges)
    g.KruskalMST()


if __name__ == "__main__" :
    main()



""" Sample Output : Edges of minimum spanning tree are in Graph 1 : [0-2](1) [3-4](1) [1-3](2) [2-3](2) [1-5](3) 
    Cost of minimum spanning tree : 9 """
