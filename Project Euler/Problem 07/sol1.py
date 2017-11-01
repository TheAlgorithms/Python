'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the Nth prime number?
'''
from math import sqrt
def isprime(n):
    if (n==2):
        return True
    elif (n%2==0):
        return False
    else:
        sq = int(sqrt(n))+1
        for i in range(3,sq,2):
            if(n%i==0):
                return False
    return True
n = int(input())
i=0
j=1
while(i!=n and j<3):
    j+=1
    if (isprime(j)):
        i+=1
while(i!=n):
    j+=2
    if(isprime(j)):
        i+=1
print j