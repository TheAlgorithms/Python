#Contributed by : Ghulam Mohiyuddin
"""
what is this: Here I am going to detect cycle in graph,return 1 if any otherwise 0.

Data Structure Used:
        DisJoint Set (Union, parent)
        Dictionary
        List


link:https://en.wikipedia.org/wiki/Disjoint-set_data_structure


Input style:
    The First line contains two integers 'V' and 'E' which denotes the no of vertices and no of edges respectively.
    The Second line of each test case contains 'E'  space separated pairs u and v denoting that there is a bidirectional  edge from u to v
    
    eg-1:
    >>> 5 4                 #--------->No. of nodes is5, and edges is 4.
    >>> 0 1 2 3 3 4 4 2     #--------->edges are (0<-->1),(2<-->3),(3<-->4) and (4<-->2).
    Output: 1           #----> 1 means cycle exist.


    eg 2:
    >>> 4 3                 #--------->No. of nodes is 4, and edges is 3.
    >>> 0 1 1 2 2 3         #--------->edges are (0<-->1),(1<-->2) and (2<-->3).
    Output: 0           #----->0 means not exist.



"""


from collections import defaultdict

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)# Initialize

        self.V = vertices # Initialize no. of vertices


    def add_edge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)




def union(parentA,d,e):
    x_=parent(parentA,d)
    y_=parent(parentA,e)
    parentA[x_]=y_

def parent(parentA,k):
    if parentA[k]==-1:
        return k
    return parent(parentA,parentA[k])


def is_cyclic(graph,n):
  
    visit={i:False for i in range(n)}# dictionary for trace a node is visited or not by true or false
    parentA=[-1]*n
    
    for i in graph:
        for j in graph[i]:
            if visit[j]==False:
                
                x=parent(parentA,i)  #who is parent of vertex i.
                y=parent(parentA,j)  #who is parent of vertex j.
                #print(i,x,j,y)
                if x==y:  #checking above both vertices are belonging from same parent or not.
                    
                    return True    #if both vertices have same parent then return true ,thats mean cycle is exist in graph.



                union(parentA,i,j)
        visit[i]=True
            
    
    return False        #return false if not cycle
    


if __name__ == '__main__':
    
        V,E = map(int,input().strip().split())      #N=5,E=4(pair of u,v)

        graph = Graph(V)# make an object of Graph Class
        edges = list(map(int,input().split()))      #[map(int,input().split())]
        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            graph.add_edge(u,v) # add an undirected edge from u to v
            graph.add_edge(v,u)# add an undirected edge from v to u
        print(is_cyclic(graph.graph,V))
        """
        >>> 5 4
        >>> 0 1 2 3 3 4 4 2
        >>> graph = Graph(5)
        >>> graph.addEdge(0, 1)
        >>> graph.addEdge(2, 3)
        >>> graph.addEdge(3, 4)
        >>> graph.addEdge(4, 2)
        >>> is_cyclic(graph.graph, 5)
        
        """


    
   
