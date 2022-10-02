wt=[1,2,3]
val=[2,7,8]
W=3
n=3
print("Weight Array:",wt)
print("Value Array:",val)
print("Knapasack Weight:",W)
print("Number of items:",n)
def knapsackTopDown(wt,val,W,n):
    t=[[None for j in range(W+1)] for i in range(n+1)]
    #Step1: Initialization
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j]=0
    #Step2: Actual Process
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print("Max Profit:",t[n][W])
knapsackTopDown(wt,val,W,n)
