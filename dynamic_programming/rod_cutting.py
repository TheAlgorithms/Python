### PROBLEM ###
"""
We are given a rod of length n and we are given the array of prices, also of
length n. This array contains the price for selling a rod at a certain length.
For example, prices[5] shows the price we can sell a rod of length 5.
Generalising, prices[x] shows the price a rod of length x can be sold.
We are tasked to find the optimal solution to sell the given rod.
"""

### SOLUTION ###
"""
Profit(n) = max(1<i<n){Price(n),Price(i)+Profit(n-i)}

When we receive a rod, we have two options:
a) Don't cut it and sell it as is (receiving prices[length])
b) Cut it and sell it in two parts. The length we cut it and the rod we are
left with, which we have to try and sell separately in an efficient way.
Choose the maximum price we can get.
"""

def CutRod(n):
    if(n == 1):
        #Cannot cut rod any further
        return prices[1]

    noCut = prices[n] #The price you get when you don't cut the rod
    yesCut = [-1 for x in range(n)] #The prices for the different cutting options

    for i in range(1,n):
        if(solutions[i] == -1):
            #We haven't calulated solution for length i yet.
            #We know we sell the part of length i so we get prices[i].
            #We just need to know how to sell rod of length n-i
            yesCut[i] = prices[i] + CutRod(n-i)
        else:
            #We have calculated solution for length i.
            #We add the two prices.
            yesCut[i] = prices[i] + solutions[n-i]

    #We need to find the highest price in order to sell more efficiently.
    #We have to choose between noCut and the prices in yesCut.
    m = noCut #Initialize max to noCut
    for i in range(n):
        if(yesCut[i] > m):
            m = yesCut[i]

    solutions[n] = m
    return m



### EXAMPLE ###
length = 5
#The first price, 0, is for when we have no rod.
prices = [0, 1, 3, 7, 9, 11, 13, 17, 21, 21, 30]
solutions = [-1 for x in range(length+1)]

print(CutRod(length))
