import math

#Function to calculate minimum of two values
def min(a,b):
    if(a>b):
        return b
    else:
        return a

#Function to generate final matrix obtained after applying Floyd Warshall algorithm and print it
def print_fw(a,n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a[j][k]=min(a[j][k],a[j][i]+a[i][k])
    
    for i in range(n):
        for j in range(n):
            if(a[i][j]==math.inf):
                print("INF")
            else:
                print(a[i][j])

#Function to take input
def inp(n):
    a = [[ 0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            z=input()
            if(z!="INF"):
                a[i][j]=int(z)
            else:
                a[i][j]=math.inf
    return a


n=int(input())
a = inp(n)
print_fw(a,n)



