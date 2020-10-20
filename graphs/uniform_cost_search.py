'''
n - Number of nodes in the graph
m - Number of goals
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : Indexing starts from 1 so 0th column and row of the matrix are 0

Return : A list containing the Uniform Cost Search traversal from a start node to the cheapest path to a goal node from the list of goal nodes
'''
def UCS_Traversal(cost,start,goals):
    l = []
    node=start	
    frontier=[]
    explored=[]
    frontier.append([cost[start][start],start])
	
    while 1:
        frontier.sort()
        if not frontier:
            return l
		
        node=frontier.pop(0)
		
        if(node[-1] in goals):
            node.pop(0)
            l=node.copy()
            return l
		
        explored.append(node[-1])
        for i in range(1,len(cost)):
            if cost[node[-1]][i] > 0 and i not in explored:
                tmp=node.copy()
                tmp.append(i)
                tmp[0]=tmp[0]+cost[node[-1]][i]
                if tmp not in frontier:
                    frontier.append(tmp)
                else:
                    for k in range(0,len(frontier)):
                        if frontier[k][-1]==i and tmp[0]<frontier[k][0]:
                            frontier[k]=tmp
if __name__=="__main__":
    cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
            [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1], 
            [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
            [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
            [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
            [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
            [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
            [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
    print(UCS_Traversal(cost, 1, [6, 7, 10]))#[1, 5, 4, 7]
    print(UCS_Traversal(cost, 3, [6, 7, 10])) #[3, 4, 7]
    print(UCS_Traversal(cost, 8, [8]))#[8]
    print(UCS_Traversal(cost, 9, [6]))#[]
    print(UCS_Traversal(cost, 8, [10]))# [8, 10]
    print(UCS_Traversal(cost, 4, [6, 7, 10]))#[4,7]