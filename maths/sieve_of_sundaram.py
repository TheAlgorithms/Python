"""
Sieve of Sundaram Algorithm

The Sieve of Sundaram is an algorithm for finding prime numbers up to a specified integer.
It was discovered by Indian mathematician S. P. Sundaram in 1934.

Wikipedia: https://en.wikipedia.org/wiki/Sieve_of_Sundaram
"""

from typing import List


def sieve_of_sundaram(limit: int) -> List[int]:
    """
    Generate all prime numbers up to the given limit using Sieve of Sundaram.
    
    The algorithm works by creating a list of integers and marking composite numbers,
    then extracting the remaining unmarked numbers which represent primes.
    
    Args:
        limit: Upper bound (exclusive) for finding primes
        
    Returns:
        List of all prime numbers less than the limit
        
    Raises:
        ValueError: If limit is negative
        
    Examples:
        >>> sieve_of_sundaram(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        >>> sieve_of_sundaram(10)
        [2, 3, 5, 7]
        >>> sieve_of_sundaram(2)
        []
        >>> sieve_of_sundaram(4)
        [2, 3]
        >>> sieve_of_sundaram(1)
        []
        >>> sieve_of_sundaram(0)
        []
        >>> sieve_of_sundaram(-5)
        Traceback (most recent call last):
        ...
        ValueError: limit must be non-negative
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")
    
    if limit <= 2:
        return []
    
    # Calculate the range for Sundaram sieve
    # We need to find primes up to 'limit', so we work with (limit-1)//2
    n = (limit - 1) // 2
    
    # Create a boolean array and initialize all entries as not marked (False)
    # marked[i] represents whether (2*i + 1) is composite
    marked = [False] * (n + 1)
    
    # Mark numbers using Sundaram's formula: i + j + 2*i*j
    # where i <= j and i + j + 2*i*j <= n
    for i in range(1, n + 1):
        j = i
        while i + j + 2 * i * j <= n:
            marked[i + j + 2 * i * j] = True
            j += 1
    
    # Collect unmarked numbers and transform them to get primes
    primes = [2]  # 2 is the only even prime
    
    for i in range(1, n + 1):
        if not marked[i]:
            primes.append(2 * i + 1)
    
    return primes


if __name__ == "__main__":
    print("Sieve of Sundaram Demo")
    print("-" * 20)
    
    test_limits = [10, 30, 50, 100]
    
    for limit in test_limits:
        primes = sieve_of_sundaram(limit)
        print(f"Primes up to {limit}: {primes}")
        print(f"Count: {len(primes)}")
        print()
