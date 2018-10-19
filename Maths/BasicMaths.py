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

def numberOfDivisors(n):
    div = 1
    
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    div = div * (temp) 
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        div = div * (temp)
    
    return div

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

def eulerPhi(n):
    l = primeFactors(n)
    l = set(l)
    s = n
    for x in l:
        s *= (x - 1)/x 
    return s   

def main():
    print(primeFactors(100))
    print(numberOfDivisors(100))
    print(sumOfDivisors(100))
    print(eulerPhi(100))
    
if __name__ == '__main__':
    main()
    
    