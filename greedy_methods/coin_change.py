def findMinCoins(amount,denominations):

    coins = 0

    while amount>0:
        for i in range(len(denominations)-1,-1,-1):
            if denominations[i]<=amount:
                coins+=1
                amount-=denominations[i]
    return coins

amount = 93
denominations = (1,5,10,20,50,100,500,1000)
print(findMinCoins(amount,denominations))