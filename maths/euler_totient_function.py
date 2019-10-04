"""Program to find euler totient function of a natural number"""
# Euler’s Totient function phi(n) for an input n is the count of 
# numbers in {1, 2, 3, …, n} that are relatively prime to n, i.e., 
# the numbers whose GCD (Greatest Common Divisor) with n is 1.

# phi(n) = n*(1 - 1/a)*(1 - 1/b)*(1 - 1/c)...
# where a, b, c, ... are the prime factors of n

def phi(n): 
      
    # Initialize result as n 
    result = n;  
  
    # Consider all prime factors 
    # of n and subtract their 
    # multiples from result 
    p = 2  
    while(p * p <= n): 
          
        # Check if p is a  
        # prime factor. 
        if (n % p == 0):  
              
            # If yes, then  
            # update n and result 
            while (n % p == 0): 
                n = int(n / p) 
            result -= int(result / p)
        p += 1
  
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most  
    # one such prime factor) 
    if (n > 1): 
        result -= int(result / n); 
    return result