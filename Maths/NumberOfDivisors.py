import math

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

print(numberOfDivisors(100))
