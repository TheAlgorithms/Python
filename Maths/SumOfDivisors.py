import math

def sumOfDivisors(n):
    s = 1
    
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    if temp > 1:
        s *= (2**temp - 1) / (2 - 1) 
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        if temp > 1:
            s *= (i**temp - 1) / (i - 1)
    
    return s

print(sumOfDivisors(100))
