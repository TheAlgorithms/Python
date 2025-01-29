import math
import random

def gcd(a, b):
    """Computes the greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def modular_exponentiation(base, exp, mod):
    """Computes (base^exp) % mod using fast modular exponentiation."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def find_order(a, N):
    """Finds the smallest r such that a^r ≡ 1 (mod N)"""
    r = 1
    while modular_exponentiation(a, r, N) != 1:
        r += 1
        if r > N:  # Prevent infinite loops
            return None
    return r

def shor_algorithm(N):
    """Simulates Shor’s Algorithm classically to factorize N."""
    if N % 2 == 0:
        return 2, N // 2  # Trivial case if N is even

    while True:
        a = random.randint(2, N - 1)
        factor = gcd(a, N)
        if factor > 1:
            return factor, N // factor  # Lucky case: a and N are not coprime

        r = find_order(a, N)
        if r is None or r % 2 == 1:
            continue  # Retry if order is not even

        factor1 = gcd(modular_exponentiation(a, r // 2, N) - 1, N)
        factor2 = gcd(modular_exponentiation(a, r // 2, N) + 1, N)

        if 1 < factor1 < N:
            return factor1, N // factor1
        if 1 < factor2 < N:
            return factor2, N // factor2

# Example usage
if __name__ == "__main__":
    N = 15  # You can test with 21, 35, 55, etc.
    factors = shor_algorithm(N)
    print(f"Factors of {N}: {factors}")
