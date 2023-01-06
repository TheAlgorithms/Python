import gmpy2
from gmpy2 import mpz

# the takahashi fibonacci algorithm is used to compute fibonacci numbers for a large value of n.
# more details on D.Takahashi's paper about his algorithm
# https://www.semanticscholar.org/paper/A-fast-algorithm-for-computing-large-Fibonacci-Takahashi/96529e1fedb0a372b825215c7b471a99088f4515


def fibonacci(n):
    def fib_inner(n):
        if n == 0:
            return mpz(2), mpz(1)
        m = n >> 1
        u, v = fib_inner(m)
        q = (2, -2)[m & 1]
        u = u * u - q
        v = v * v + q
        if n & 1:
            return v - u, v
        return u, v - u

    m = n >> 1
    u, v = fib_inner(m)
    f = (2 * v - u) / 5
    if n & 1:
        q = (n & 2) - 1
        return v * f - q
    return u * f


n = int(input())
print(fibonacci(n))
