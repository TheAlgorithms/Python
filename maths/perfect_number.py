def isPerfect( n ): 
    """
    A number is a perfect number if is equal to sum of its proper divisors, 
    that is, sum of its positive divisors excluding the number itself.
    # return True/False is the given Number is Perfect Number or Not.
    
    >>> isPerfect(10)
    False
    >>> isPerfect(1)
    False
    >>> isPerfect(16)
    False
    >>> isPerfect(28)
    True
    >>> isPerfect(6)
    True
    """
    sum = 1
    i = 2
    while i * i <= n: 
        if n % i == 0: 
            sum = sum + i + n/i 
        i += 1
    return (True if sum == n and n!=1 else False) 

if __name__ == "__main__":
    n = 64
    print(isPerfect (n))
    
