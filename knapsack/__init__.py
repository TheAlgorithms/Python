def knapsack(weights, values, n, maxWeight,i) :
    if i == len(weights):
        return 0
    ans1 = 0
    ans2 = 0
    ans1 = knapsack(weights,values,n,maxWeight,i+1)
    if weights[i] <= maxWeight:
        ans2 = values[i] + knapsack(weights,values,n,maxWeight-weights[i],i+1)
    return max(ans1,ans2)

def takeInput() :
    n = int(input())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, input().split(" ")))
    values = list(map(int, input().split(" ")))
    maxWeight = int(input())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, n, maxWeight,0))
