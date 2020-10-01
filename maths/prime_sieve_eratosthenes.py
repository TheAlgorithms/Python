# flake8: noqa

"""
Sieve of Eratosthenes

Input : n =10
Output: 2 3 5 7

Input : n = 20
Output: 2 3 5 7 11 13 17 19

you can read in detail about this at
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def sieve(n):
    m=(n-1)//2
    b=[True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    print(*ps)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    num = int(input())

    seive(num)
