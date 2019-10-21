#Contributed by : Ghulam Mohiyuddin
"""
what is this: Here I am going to detect cycle in graph,return 1 if any otherwise 0.

Data Structure Used:
        DisJoint Set (Union, parent)
        Dictionary
        List


link:https://en.wikipedia.org/wiki/Disjoint-set_data_structure


Input style:
    The First line of each testcase contains two integers 'N' and 'M' which denotes the no of vertices and no of edges respectively.
    The Second line of each test case contains 'M'  space separated pairs u and v denoting that there is a bidirectional  edge from u to v
    
    eg-1:
    5 4                 #--------->No. of nodes is5, and edges is 4.
    0 1 2 3 3 4 4 2     #--------->edges are (0<-->1),(2<-->3),(3<-->4) and (4<-->2).
    Output: 1           #----> 1 means cycle exist.


    eg 2:
    4 3                 #--------->No. of nodes is 4, and edges is 3.
    0 1 1 2 2 3         #--------->edges are (0<-->1),(1<-->2) and (2<-->3).
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


def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph

    >>> graph = Graph([0, 1, 2, 3, 4])
    >>> graph.addEdge(0, 1)
    >>> graph.addEdge(1, 2)
    >>> graph.addEdge(2, 3)
    >>> is_cyclic(graph.graph, 5)
    0
    >>> graph.addEdge(4, 2)
    >>> is_cyclic(graph.graph, 5)
    1
    >>> is_cyclic(graph.graph, 6)
    1
    '''
    # code here
    visit={i:False for i in range(n)}# dictionary for trace a node is visited or not by true or false
    parentA=[-1]*n
    
    for i in g:
        for j in g[i]:
            if visit[j]==False:
                
                x=parent(parentA,i)
                y=parent(parentA,j)
                #print(i,x,j,y)
                if x==y:
                    #return 1 if any
                    
                    return 1
                union(parentA,i,j)
        visit[i]=True
            
    #return 0 if not cycle
    return 0
    





if __name__ == '__main__':
    #test_cases = int(input())
    #for cases in range(test_cases) :
        N,E = map(int,input().strip().split())      #N=5,E=4(pair of u,v)

        g = Graph(N)# make an object of Graph Class
        edges = list(map(int,input().strip().split()))
        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)# add an undirected edge from v to u
        print(isCyclic(g.graph,N))


    
   
