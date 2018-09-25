import math

def primeFactors(n):
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
        
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
    
    if n > 2:
        pf.append(n)
    
    return pf

print(primeFactors(100))
