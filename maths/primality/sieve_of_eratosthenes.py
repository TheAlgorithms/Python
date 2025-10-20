# Sieve of Eratosthenes: an efficient algorithm to compute all prime numbers up to n.
# It repeatedly marks multiples of each prime as non-prime, starting from 2.
# This method is suitable for n up to about 10**7 on typical hardware.

def sieve_of_erastosthenes(n):
    """
Compute all prime numbers up to and including n using the Sieve of Eratosthenes.
Parameters
----------
n : int
    Upper bound (inclusive) of the range in which to find prime numbers.
    Expected to be a non-negative integer. If n < 2 the function returns an empty list.
Returns
-------
list[int]
    A list of primes in ascending order that are <= n.
    """

   
    #Boolean list to track prime status of numbers
    prime = [True] * (n + 1)
    p = 2

    # Main Algorithm
    while p * p <= n:
        if prime[p]:
            
            # All multiples of p will be non-prime hence delcare them False.

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Store all primes.
    result = []
    for p in range(2, n + 1):
        if prime[p]:
            result.append(p)
    
    return result

if __name__ == "__main__":
    n = 35
    result = sieve_of_erastosthenes(n)
    for num in result:
        print(num, end=' ')