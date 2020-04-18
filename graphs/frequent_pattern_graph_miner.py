'''
FP-GraphMiner - A Fast Frequent Pattern Mining Algorithm for Network Graphs

A novel Frequent Pattern Graph Mining algorithm,
FP-GraphMiner, that compactly represents a set of network graphs as a Frequent Pattern Graph (or FP-Graph).
This graph can be used to efficiently mine frequent subgraphs including maximal frequent subgraphs and maximum common subgraphs.

URL:https://www.researchgate.net/publication/235255851_FP-GraphMiner_-_A_Fast_Frequent_Pattern_Mining_Algorithm_for_Network_Graphs

'''
from typing import List

edge_array=[
    ['ab-e1','ac-e3','ad-e5','bc-e4','bd-e2','be-e6','bh-e12','cd-e2','ce-e4','de-e1','df-e8','dg-e5','dh-e10','ef-e3','eg-e2','fg-e6','gh-e6','hi-e3'],
    ['ab-e1','ac-e3','ad-e5','bc-e4','bd-e2','be-e6','cd-e2','de-e1','df-e8','ef-e3','eg-e2','fg-e6'],
    ['ab-e1','ac-e3','bc-e4','bd-e2','de-e1','df-e8','dg-e5','ef-e3','eg-e2','eh-e12','fg-e6','fh-e10','gh-e6'],
    ['ab-e1','ac-e3','bc-e4','bd-e2','bh-e12','cd-e2','df-e8','dh-e10'],
    ['ab-e1','ac-e3','ad-e5','bc-e4','bd-e2','cd-e2','ce-e4','de-e1','df-e8','dg-e5','ef-e3','eg-e2','fg-e6']
    ]

def get_distinct_edge(edge_array: List[List[str]]) -> List[str]:
    '''
    Return Distinct edges from edge array of multiple graphs
    '''
    distinct_edge=set()

    for i,row in enumerate(edge_array):    
        for j,item in enumerate(row):
            distinct_edge.add(item[0])

    return list(distinct_edge)

def get_bitcode(edge_array,distinct_edge):
    '''
    Return bitcode of distinct_edge
    '''
    bitcode=['0' for i in enumerate(edge_array)]
    
    for i,row in enumerate(edge_array):
        for j,item in enumerate(row):
            if distinct_edge in item[0]:
                bitcode[i]='1'
                break

            
    return bitcode

def get_frequency_table(edge_array):
    '''
    Returns Frequency Table,cluster,nodes,support
    '''
    distinct_edge=get_distinct_edge(edge_array) 
    frequency_table=dict()
    
    for i,item in enumerate(distinct_edge):
        bit=get_bitcode(edge_array,item)
        bt=''.join(bit)
        s=bt.count('1')
        frequency_table[item]=[s,bt]
    # Store [Distinct edge, WT(Bitcode), Bitcode] in Descending order
    sorted_frequency_table=[[k,v[0],v[1]] for k,v in sorted(frequency_table.items(),key=lambda v:v[1][0],reverse=True)]
    # format cluster:{WT(bitcode):nodes with same WT}
    cluster={}
    # format nodes={bitcode:edges that represent the bitcode}
    nodes={}
    support=[]

    for i,item in enumerate(sorted_frequency_table):
        nodes.setdefault(item[2],[]).append(item[0])
        
    for key,value in nodes.items():
        cluster.setdefault(key.count('1'),{})[key]=value
        
    for i in cluster:
        support.append(i*100/len(cluster)) 
        
    return sorted_frequency_table,cluster,nodes,support   

def print_all():
    print("\nNodes\n")
    for key,value in nodes.items():
        print(key,value)
    print("\nSupport\n")
    print(support)
    '''print("\n Edge List\n")
    for i in EL:
        print(i)'''
    print("\n Cluster \n")
    for key,value in sorted(cluster.items(),reverse=True):
        print(key, value)
    print("\n Graph\n")
    for key,value in graph.items():
        print(key, value)
    print("\n Edge List of Frequent subgraphs \n")
    for edge_list in freq_subgraph_edge_list:
        print(edge_list)
       
def create_edge(nodes,graph,cluster,c1):
    '''
    create edge between the nodes 
    '''
    for i in cluster[c1].keys():
        count=0
        c2=c1+1
        while c2 < max(cluster.keys()):
            for j in cluster[c2].keys():
                '''
                creates edge only if the condition satisfies
                '''
                if(int(i,2) & int(j,2) == int(i,2)): 
                   if tuple(nodes[i]) in graph:
                       graph[tuple(nodes[i])].append(nodes[j])
                   else:
                        graph[tuple(nodes[i])]=[nodes[j]]
                   count+=1
            if(count==0):
                c2=c2+1
            else:
                break

def construct_graph(cluster,nodes): 
    X=cluster[max(cluster.keys())]
    cluster[max(cluster.keys())+1]='Header'
    graph={}
    for i in X.keys():
        if tuple(['Header']) in graph:
            graph[tuple(['Header'])].append(X[i])
        else:
            graph[tuple(['Header'])]=[X[i]]
    for i in X.keys():
        graph[tuple(X[i])]=[['Header']]
    i=1
    while i < max(cluster.keys())-1:
        create_edge(nodes,graph,cluster,i) 
        i=i+1
        
    return graph

def myDFS(graph,start,end,path=[]): 
    '''
    find different DFS walk from given node to Header node
    '''
    path=path+[start] 
    if start==end:
        paths.append(path) 
    for node in graph[start]:
        if tuple(node) not in path:
            myDFS(graph,tuple(node),end,path)
            
def find_freq_subgraph_given_support(s,cluster,graph):
    '''
    find edges of multiple frequent subgraphs
    '''
    k=int(s/100*(len(cluster)-1))
    freq_subgraphs=[]
    for i in cluster[k].keys():
        myDFS(graph,tuple(cluster[k][i]),tuple(['Header']))

def freq_subgraphs_edge_list(paths):
    '''
    returns Edge list for frequent subgraphs
    '''
    freq_sub_EL=[]
    for edges in paths:
        EL=[]
        for j in range(len(edges)-1):
            temp=list(edges[j])
            for e in temp:
                edge=(e[0],e[1])
                EL.append(edge)
        freq_sub_EL.append(EL)
        
    return freq_sub_EL 
def preprocess(edge_array: List[List[str]) -> List[List[List[str]]]:
    for i in range(len(edge_array)):
        for j in range(len(edge_array[i])):
            t=edge_array[i][j].split('-')
            edge_array[i][j]=t
                                
if __name__ == "__main__":
                                
    preprocess(edge_array)
    frequency_table,cluster,nodes,support=get_frequency_table(edge_array)
    graph=construct_graph(cluster,nodes)
    paths = []
    find_freq_subgraph_given_support(60,cluster,graph)
    freq_subgraph_edge_list=freq_subgraphs_edge_list(paths)
    
    print_all()
