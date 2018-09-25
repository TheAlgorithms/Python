def eulerPhi(n):
    l = primeFactors(n)
    l = set(l)
    s = n
    for x in l:
        s *= (x - 1)/x 
    return s  

print(eulerPhi(100))
