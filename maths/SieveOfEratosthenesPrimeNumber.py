'''
Sieve of Eratosthenes

Input : n =10
Output : 2 3 5 7 

Input : n = 20 
Output: 2 3 5 7 11 13 17 19
'''

def primeNumbers(num):
    
    primes = [True for i in range(num + 1)]
    p = 2
    
    while p * p <= num:
        if primes[p] == True:
            for i in range(p*p, num+1, p):
                primes[i] = False
        p+=1

    for prime in range(2, num+1):
        if primes[prime]:
            print(prime, end=" ")

if __name__ == "__main__":
    num = int(input())
    
    primeNumbers(num)