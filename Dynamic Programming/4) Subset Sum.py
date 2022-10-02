arr=[1,2,1]
sum=0
n=3
print("Elements Array:",arr)
print("Target Sum:",sum)
print("Number of Elements:",n)
def subsetSum(arr,sum,n):
    t=[[None for i in range(sum+1)] for j in range(n+1)]
    #Step 1: Initialization
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True
    #Step 2: Actual Process
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return(t[n][sum])
ans=subsetSum(arr,sum,n)
print("Is it Possible:",ans)
