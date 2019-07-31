"""
https://projecteuler.net/problem=10

Problem Statement:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

using Sieve_of_Eratosthenes : 

The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million
"""

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3

try:
    xrange  # Python 2
except NameError:
    xrange = range  # Python 3


def prime_sum(n):
    """Returns the sum of all the primes below n.
    

        >>> prime_sum(2000000)
        142913828922
        >>> prime_sum(1000)
        76127
        >>> prime_sum(5000)
        1548136
        >>> prime_sum(10000)
        5736396
        >>> prime_sum(7)
        10

    """
    
    list = [0 for i in xrange(n+1)]

    list[0]=1
    list[1]=1

    for i in xrange(2,int(n**0.5)+1):
        if list[i]==0:
            for j in xrange(i * i, n+1, i):
                    list[j]=1
    s=0
    for i in xrange(n):
        if list[i] == 0:
            s+=i
    return(s)

if __name__ == '__main__':
    
    #import doctest
    #doctest.testmod()
    
    print(prime_sum(int(raw_input())))


