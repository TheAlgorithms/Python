trgNum = int(input("enter target number"))
firstSum=0

def getDigSqSum(num):
    res = 0
    while num>0:
        a = int(num%10)
        res = res + (a*a
        num = num - a
        num = num/10
        
    return res

firstSum = getDigSqSum(trgNum)
print (firstSum)

n = firstSum
lastSum=0

while lastSum != firstSum :
        
    lastSum = 0 
    
    lastSum = getDigSqSum(n) 
        
    print(lastSum)    
    n = lastSum
        
#focxtrot12
