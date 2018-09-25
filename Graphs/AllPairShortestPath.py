import sys

# Can be used only if V <= 400
# This algorithm can also be used to check whether a negative cycle exists or not
# If any diagonal element becomes negative, a negative cycle gets detected

# Warshall's Algorithm
# It was first introduced to find the transitive closure. It means to check whether a path
# exists from i to j or not. Or and & operation is used to store 0 or 1 in below 
# algorithm instead of maintaining the edge values and storing in matrix.

# Floyd's Warshall Algorithm
def AllPairShortestPath(cost):
    
    infy = sys.maxsize
    n = len(cost)
    
    # Minimum cost matrix
    A = []
    
    # Path matrix
    P = []
    
    for i in range(n):
        temp = []
        temp1 = []
        for j in range(n):
            if i != j:
                temp.append(cost[i][j])
            else:
                temp.append(0)
        A.append(temp)
        
        for j in range(n):
            if i == j:
                temp1.append(0)
            elif A[i][j] == infy:
                temp1.append(infy)
            else:
                temp1.append(i)
        P.append(temp1)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    if A[i][j] > A[i][k] + A[k][j]:
                        A[i][j] = A[i][k] + A[k][j]
                        P[i][j] = k
                    
    return A, P

infy = sys.maxsize
n = int(input("Enter number of vertices: "))
cost = [ [infy for x in range(n)] for x in range(n) ]
e = int(input("Enter number of edges: "))
for x in range(e):
    x, y, z = [int(x) for x in input().split()]
    cost[x][y] = z
    
A, P = AllPairShortestPath(cost)

print(A)
print(P)

            


    