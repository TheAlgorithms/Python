"""
Sieve of Sundaram - Alternative prime number algorithm.
Discovered by S. P. Sundaram in 1934.
"""

from typing import List


def sieve_of_sundaram(limit: int) -> List[int]:
    """
    Find all prime numbers up to limit using Sieve of Sundaram.
    
    >>> sieve_of_sundaram(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> sieve_of_sundaram(10)
    [2, 3, 5, 7]
    >>> sieve_of_sundaram(2)
    []
    """
    if limit <= 2:
        return []
    
    n = (limit - 1) // 2
    marked = [False] * (n + 1)
    
    for i in range(1, n + 1):
        j = i
        while i + j + 2 * i * j <= n:
            marked[i + j + 2 * i * j] = True
            j += 1
    
    primes = [2]
    for i in range(1, n + 1):
        if not marked[i]:
            primes.append(2 * i + 1)
    
    return primes



if __name__ == "__main__":
    print("Sieve of Sundaram Demo")
    print("-" * 20)
    
    for limit in [10, 30, 50]:
        primes = sieve_of_sundaram(limit)
        print(f"Primes up to {limit}: {primes}")
        print(f"Found {len(primes)} primes")
