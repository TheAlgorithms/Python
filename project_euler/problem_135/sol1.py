"""
Project Euler Problem [135]: [https://projecteuler.net/problem=135]

... [Given the positive integers, x, y, and z,
are consecutive terms of an arithmetic progression,
the least value of the positive integer, n,
for which the equation,
x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value
which has exactly ten solutions.

How many values of n less than one million
have exactly ten distinct solutions?] ...


... [Taking x,y,z of the form a+d,a,a-d respectively,
    the given equation reduces to a*(4d-a)=n.
    Calculating no of solutions for every n till 1 million by fixing a
    ,and n must be multiple of a.
    Total no of steps=n*(1/1+1/2+1/3+1/4..+1/n)
    ,so roughly O(nlogn) time complexity.]...

"""


def solution() -> int:
    """
    returns the values of n less than one million
    have exactly ten distinct solutions
    >>> solution()
    4989
    """
    LIMIT = int(1e6) + 1
    freq = [0] * LIMIT
    for a in range(1, LIMIT):
        for n in range(a, LIMIT, a):
            d = a + n / a
            if d % 4:  # d must be divisble by 4
                continue
            else:
                d /= 4
                if a > d and a < 4 * d:  # since x,y,z are positive integers
                    freq[n] += 1  # so z>0 and a>d ,also 4d<a
    count = 0
    for n in range(1, LIMIT):
        if freq[n] == 10:
            count += 1

    return count
