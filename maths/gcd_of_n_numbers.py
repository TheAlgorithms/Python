"""
GCD of N Numbers

This module calculates the Greatest Common Divisor (GCD)
of multiple positive integers using prime factorization.

Reference:
https://en.wikipedia.org/wiki/Greatest_common_divisor
"""

from collections import Counter
from math import isqrt


def get_factors(
    number: int, prime_factors: Counter | None = None, divisor: int = 2
) -> Counter:
    """
    Recursively computes the PRIME FACTORIZATION of a positive integer.

    The result is returned as a Counter where:
    - key   → prime factor
    - value → power of that prime factor

    Examples:
    >>> get_factors(45)
    Counter({3: 2, 5: 1})
    >>> get_factors(2520)
    Counter({2: 3, 3: 2, 5: 1, 7: 1})
    >>> get_factors(23)
    Counter({23: 1})
    >>> get_factors(1)
    Counter()
    """

    # -----------------------------
    # Input Validation
    # -----------------------------
    # The function should only accept positive integers.
    # Any other input is invalid.
    if not isinstance(number, int) or number <= 0:
        raise TypeError("number must be an integer greater than zero")

    # -----------------------------
    # Base Case: number == 1
    # -----------------------------
    # 1 has NO prime factors.
    # Returning an empty Counter is mathematically correct.
    if number == 1:
        return Counter()

    # -----------------------------
    # Initialize Counter
    # -----------------------------
    # If this is the first call, create a new Counter.
    # Otherwise, reuse the existing one (recursive calls).
    prime_factors = prime_factors or Counter()

    # -----------------------------
    # Optimization (IMPORTANT)
    # -----------------------------
    # If divisor is greater than sqrt(number),
    # then the remaining number itself must be prime.
    #
    # Example:
    # If number = 23, no divisor <= sqrt(23) divides it,
    # so 23 is prime.
    if divisor > isqrt(number):
        prime_factors[number] += 1
        return prime_factors

    # -----------------------------
    # If divisor divides the number
    # -----------------------------
    if number % divisor == 0:
        # divisor is a prime factor
        prime_factors[divisor] += 1

        # Continue factoring the reduced number
        return get_factors(number // divisor, prime_factors, divisor)

    # -----------------------------
    # If divisor does NOT divide the number
    # -----------------------------
    # Try the next possible divisor
    return get_factors(number, prime_factors, divisor + 1)


def get_greatest_common_divisor(*numbers: int) -> int:
    """
    Computes the Greatest Common Divisor (GCD)
    of one or more positive integers.

    The approach:
    1. Compute prime factors of each number
    2. Find common factors using Counter intersection
    3. Multiply common factors to get GCD

    Examples:
    >>> get_greatest_common_divisor(18, 45)
    9
    >>> get_greatest_common_divisor(23, 37)
    1
    >>> get_greatest_common_divisor(2520, 8350)
    10
    """

    # -----------------------------
    # Factorize all numbers
    # -----------------------------
    # map(get_factors, numbers) converts:
    # (18, 45) → [Counter({2:1,3:2}), Counter({3:2,5:1})]
    try:
        common_factors, *other_factors = map(get_factors, numbers)
    except TypeError as exc:
        # Raised if any input is invalid
        raise ValueError("numbers must be integers greater than zero") from exc

    # -----------------------------
    # Find common prime factors
    # -----------------------------
    # Counter '&' operator keeps:
    # - only common keys
    # - minimum power for each key
    #
    # Example:
    # Counter({2:1, 3:2}) & Counter({3:2, 5:1})
    # → Counter({3:2})
    for factors in other_factors:
        common_factors &= factors

    # -----------------------------
    # Multiply common factors
    # -----------------------------
    # Convert factorization back into a number.
    # Example:
    # Counter({2:2, 3:1}) → 2² * 3¹ = 12
    gcd_value = 1
    for factor, power in common_factors.items():
        gcd_value *= factor**power

    return gcd_value


# -----------------------------
# Manual Test
# -----------------------------
if __name__ == "__main__":
    print(get_greatest_common_divisor(18, 45))  # Expected output: 9
