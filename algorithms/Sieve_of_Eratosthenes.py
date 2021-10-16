#Sieve of Eratosthenes is used to get all 
#prime number in a given range and is a 
#very efficient algorithm.

from math import sqrt

def eratosthenes_primes(num):
    prime_arr = [1]*(num+1)
    prime_arr[0] = 0
    prime_arr[1] = 0
    for k in range(2,int(sqrt(num))+1):
        if(prime_arr[k]==1):
            i=2
            while(k*i<num+1):
                prime_arr[i*k]=0
                i=i+1
    return prime_arr

print(eratosthenes_primes(10))
#In this the range is from 0-10 and we get output in the form
#of 0's and 1's . The 0's in the array indicate that the number is not 
#prime and the 1's represent that the number is prime in the defined range.so the output is
#[0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0] in this
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# as 2 is prime so we get 1 and 3 is prime so again we get 1






