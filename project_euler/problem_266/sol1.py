"""
Pseudo Square Root
Show HTML problem content 
Problem 266

The divisors of 12 are: 1,2,3,4,6 and 12.
The largest divisor of 12 that does not exceed the square root of 12 is 3.
We shall call the largest divisor of an integer n that does not exceed the square root of n the pseudo square root (PSR) of n.
It can be seen that PSR(3102)=47.

Let p be the product of the primes below 190.
Find PSR(p) mod 10**16.
"""

"""
p>>>5397346292805549782720214077673687806275517530364350655459511599582614290
ans 4272890769165047
this algo uses roots multiplication to get the number
"""
import math as m


def prod(a):
    if len(a) == 1:
        return a[0]
    return a[-1] * prod(a[:-1])


def isprime(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, a // 2 + 1, 2):
        if a % i == 0:
            return False
    return True


roots = []
p = 1
for i in range(2, 190):
    if isprime(i):
        roots.append(i)
        p *= i

lim = m.sqrt(p)

for i in range(2, len(roots)):
    if prod(roots[-i:]) < lim and prod(roots[-i - 1 :]) > lim:
        print(prod(roots[-i:]) % 10 ** 16)
        break
