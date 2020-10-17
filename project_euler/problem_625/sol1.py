"""
https://projecteuler.net/problem=625

G(N) = Sum of j=1 to N(Sum of i=1 to j 0f GCD(i, j)).
You are given: G(10) = 122.

Find G(10**11). Give your answer modulo 998244353
"""

def gcd(a,b):
    """Find GCD"""
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def solution():
    num = 10**11 #INPUT
    total = 0 #Total
    for j in range(1, num+1):
        for i in range(1, j+1):
            total += gcd(i, j)
    return total

if __name__ == "__main__":
    print(solution())
