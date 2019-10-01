def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u3 = 1, a
    v1, v3 = 0, m
    while v3 != 0:
        q = u3 // v3
        v1, v3, u1, u3 = (u1 - q * v1), (u3 - q *v3), v1, v3
    return u1 % m     
