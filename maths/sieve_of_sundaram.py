def sieve_sundaram(n):
    ''' 
    Sieve of Sundaram
    
    https://en.wikipedia.org/wiki/Sieve_of_Sundaram
    '''

    ub = (n-1)//2 + 1
    sieve = bytearray(ub)
    start = 0
    for i in range(1, ub):
        start += 4*i
        if start >= ub:
            break
        for j in range(start, ub, 2*i+1):
            sieve[j] = 1
    return [2] + [2*i+1 for i in range(1, ub) if sieve[i] == 0]

print(sieve_sundaram(1000))
