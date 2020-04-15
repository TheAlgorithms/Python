'''
FP-GraphMiner - A Fast Frequent Pattern Mining Algorithm for Network Graphs

A novel Frequent Pattern Graph Mining algorithm,
FP-GraphMiner, that compactly represents a set of network graphs as a Frequent Pattern Graph (or FP-Graph).
This graph can be used to efficiently mine frequent subgraphs including maximal frequent subgraphs and maximum common subgraphs.

URL:https://www.researchgate.net/publication/235255851_FP-GraphMiner_-_A_Fast_Frequent_Pattern_Mining_Algorithm_for_Network_Graphs

'''
def get_DE(EA):
    '''
    Return Distinct edges from edge array of multiple graphs
    '''
    DE=set()
    for i in range(len(EA)):
        for j in range(len(EA[i])):
            DE.add(EA[i][j][0])
    return list(DE)  # avoid unneeded parens and avoid creating variables that only last for one line.

def get_bitcode(EA,DE):
    '''
    Return bitcode of DE
    '''
    bitcode=['0' for i in range(len(EA))] 
    #bitcode="0" * len(EA)
    for i in range(len(EA)):
        for j in range(len(EA[i])):
            if DE in EA[i][j][0]:
                bitcode[i]='1'
                break
    return bitcode

def get_FT(EA):
    '''
    Returns FT,cluster,nodes,support
    '''
    DE=get_DE(EA) 
    FT=dict()
    for i in range(len(DE)):
        bit=get_bitcode(EA,DE[i])
        bt=''.join(bit)
        #print(bt)
        s=bt.count('1')
        FT[DE[i]]=[s,bt]
    '''
    Store [Distinct edge, WT(Bitcode), Bitcode] in Descending order
    '''
    Sorted_FT=[[k,v[0],v[1]] for k,v in sorted(FT.items(),key=lambda v:v[1][0],reverse=True)]
    '''
    format cluster:{WT(bitcode):nodes with same WT}
    '''
    cluster={}
    '''
    format nodes={bitcode:edges that represent the bitcode}
    '''
    nodes={}
    support=[]
    for i in range(len(Sorted_FT)): 
        nodes.setdefault(Sorted_FT[i][2],[]).append(Sorted_FT[i][0])
    for i in nodes.keys():
        cluster.setdefault(i.count('1'),{})[i]=nodes[i]
    for i in cluster.keys():
        support.append(i*100/len(cluster.keys())) 
        
    return Sorted_FT,cluster,nodes,support   

def print_all():
    print("\nNodes\n")
    for i in nodes.keys():
        print(i,nodes[i])
    print("\nSupport\n")
    print(support)
    '''print("\n Edge List\n")
    for i in EL:
        print(i)'''
    print("\n Cluster \n")
    for i in sorted(cluster.keys(),reverse=True):
        print(i,cluster[i])
    print("\n Graph\n")
    for i in G.keys():
        print(i,G[i])
    print("\n Edge List of Frequent subgraphs \n")
    for i in freq_sub_EL:
        print(i)
        
def create_edge(nodes,G,cluster,c1):
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
                   if tuple(nodes[i]) in G:
                       G[tuple(nodes[i])].append(nodes[j])
                   else:
                        G[tuple(nodes[i])]=[nodes[j]]
                   count+=1
            if(count==0):
                c2=c2+1
            else:
                break

def construct_graph(cluster,nodes): 
    X=cluster[max(cluster.keys())]
    cluster[max(cluster.keys())+1]='Header'
    G={}
    for i in X.keys():
        if tuple(['Header']) in G:
            G[tuple(['Header'])].append(X[i])
        else:
            G[tuple(['Header'])]=[X[i]]
    for i in X.keys():
        G[tuple(X[i])]=[['Header']]
    i=1
    while i < max(cluster.keys())-1:
        create_edge(nodes,G,cluster,i) 
        i=i+1
        
    return G

def myDFS(graph,start,end,path=[]): 
    '''
    find different DFS walk from given node to Header node
    '''
    path=path+[start] 
    if start==end or ''.join(list(start))== end:
        paths.append(path) 
    for node in graph[start]:
        if tuple(node) not in path:
            myDFS(graph,tuple(node),end,path)
            
def find_freq_subgraph_given_support(s,cluster,G):
    '''
    find edges of multiple frequent subgraphs
    '''
    k=int(s/100*(len(cluster)-1))
    freq_subgraphs=[]
    for i in cluster[k].keys():
        myDFS(G,tuple(cluster[k][i]),tuple(['Header']))

def freq_subgraphs_EL(paths):
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

if __name__ == "__main__":
    EA=[
    ['ab-e1','ac-e3','ad-e5','bc-e4','bd-e2','be-e6','bh-e12','cd-e2','ce-e4','de-e1','df-e8','dg-e5','dh-e10','ef-e3','eg-e2','fg-e6','gh-e6','hi-e3'],
    ['ab-e1','ac-e3','ad-e5','bc-e4','bd-e2','be-e6','cd-e2','de-e1','df-e8','ef-e3','eg-e2','fg-e6'],
    ['ab-e1','ac-e3','bc-e4','bd-e2','de-e1','df-e8','dg-e5','ef-e3','eg-e2','eh-e12','fg-e6','fh-e10','gh-e6'],
    ['ab-e1','ac-e3','bc-e4','bd-e2','bh-e12','cd-e2','df-e8','dh-e10'],
    ['ab-e1','ac-e3','ad-e5','bc-e4','bd-e2','cd-e2','ce-e4','de-e1','df-e8','dg-e5','ef-e3','eg-e2','fg-e6']
    ]
    for i in range(len(EA)):
        for j in range(len(EA[i])):
            t=EA[i][j].split('-')
            EA[i][j]=t
    
    FT,cluster,nodes,support=get_FT(EA)
    G=construct_graph(cluster,nodes)
    paths = []
    find_freq_subgraph_given_support(60,cluster,G)
    freq_sub_EL=freq_subgraphs_EL(paths)
    print_all()
