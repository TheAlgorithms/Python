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


    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)




def union(parentA,d,e):
    x_=parent(parentA,d)
    y_=parent(parentA,e)
    parentA[x_]=y_

def parent(parentA,k):
    if parentA[k]==-1:
        return k
    return parent(parentA,parentA[k])


def isCyclic(graph,n):
  
    visit={i:False for i in range(n)}# dictionary for trace a node is visited or not by true or false
    parentA=[-1]*n
    
    for i in graph:
        for j in graph[i]:
            if visit[j]==False:
                
                x=parent(parentA,i)  #who is parent of vertex i.
                y=parent(parentA,j)  #who is parent of vertex j.
                #print(i,x,j,y)
                if x==y:  #checking above both vertices are belonging from same parent or not.
                    
                    return 1    #if both vertices have same parent then return 1 ,thats mean cycle is exist in graph.



                union(parentA,i,j)
        visit[i]=True
            
    
    return 0        #return 0 if not cycle
    


if __name__ == '__main__':
    
        V,E = map(int,input().strip().split())      #N=5,E=4(pair of u,v)

        graph = Graph(V)# make an object of Graph Class
        edges = list(map(int,input().strip().split()))
        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            graph.addEdge(u,v) # add an undirected edge from u to v
            graph.addEdge(v,u)# add an undirected edge from v to u
        print(isCyclic(graph.graph,V))
        """
        >>> 5 4
        >>> 0 1 2 3 3 4 4 2
        >>> graph = Graph(5)
        >>> graph.addEdge(0, 1)
        >>> graph.addEdge(2, 3)
        >>> graph.addEdge(3, 4)
        >>> graph.addEdge(4, 2)
        >>> isCyclic(graph.graph, 5)
        
        """


    
   
