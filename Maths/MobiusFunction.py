def is_square_free(factors):
    '''
    This functions takes a list of prime factors as input.
    returns True if the factors are square free.
    '''
    for i in factors:
        if factors.count(i) > 1:
            return False
    return True
    

def prime_factors(n):
    '''
    Returns prime factors of n as a list.
    '''
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def mobius_function(n):
    '''
    Mobius function
    '''
    factors = prime_factors(n)
    if is_square_free(factors):
        if len(factors)%2 == 0:
            return 1
        elif len(factors)%2 != 0:
            return -1
    else:
        return 0
