arr = []
B = int(input())    #maximum distance traversed in 1 full tank
L = int(input())    #destination
n=int(input())
arr = list(map(int, input().split()))

arr.insert(0,int(0))
arr.append(B)

def MinRefills(x,n,L):
    numrefills = 0
    currentrefills = 0
    while currentrefills<=n:
        lastrefill = currentrefills
        while currentrefills<=n and x[currentrefills+1]-x[lastrefill]<=L:
            currentrefills = currentrefills+1
        if currentrefills == lastrefill:
            return -1
        if currentrefills<=n:
            numrefills=numrefills+1
    return numrefills

ans = MinRefills(arr,n,L)

print(ans)
