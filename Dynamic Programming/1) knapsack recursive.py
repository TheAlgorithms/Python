def knapsackRecursive(wt,val,W,n):
    #base condition
    if n==0 or W ==0:
        return 0
    #recursive condition
    if wt[n-1]<=W:
        return max(val[n-1]+knapsackRecursive(wt,val,W-wt[n-1],n-1), knapsackRecursive(wt,val,W,n-1))
    if wt[n-1]>W:
        return knapsackRecursive(wt,val,W,n-1)
    
wt=[1,2,3]
val=[2,4,8]
W=3
n=3

print("Weight Array:",wt)
print("Value Array:",val)
print("Knapsack Weight:",W)
print("Number of Items:",n)
ans = knapsackRecursive(wt,val,W,n)
print("Max Profit:",ans)
