def __gcd(a,b): 
    return a if(b==0) else __gcd(b, a % b) 

def digitGCD(n): 

    gcd = 0
    while (n > 0): 

        gcd = __gcd(n % 10, gcd) 

        # If at point GCD becomes 1, 
        # return it 
        if (gcd == 1): 
           return 1

        n = n // 10

    return gcd 

#Driver code 
n = 2448
print(digitGCD(n)) 
