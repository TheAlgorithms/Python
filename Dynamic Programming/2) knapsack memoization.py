wt=[1,3,2]
val=[2,10,9]
W=3
n=3

print("Weight Array:",wt)
print("Value Array:",val)
print("Knapsack Weight:",W)
print("Number of Items:",n)



t=[[-1 for i in range(W+1)] for j in range(n+1)]
def knapsackMemoization(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]

    if wt[n-1]<=W:
        t[n][W]=max(val[n-1]+knapsackMemoization(wt,val,W-wt[n-1],n-1),knapsackMemoization(wt,val,W,n-1))
        return t[n][W]
    elif wt[n-1]>W:
        t[n][W]=knapsackMemoization(wt,val,W,n-1)
        return t[n][W]

ans = knapsackMemoization(wt,val,W,n)
print("Max Profit:",ans)
