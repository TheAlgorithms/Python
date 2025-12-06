"""
Shor's Algorithm - Classical Simulation

Shor's algorithm is a quantum algorithm for integer factorization that runs in
polynomial time. It was developed by Peter Shor in 1994. This implementation
provides a classical simulation to demonstrate the algorithm's logic without
requiring quantum hardware or libraries like Qiskit or Cirq.

The algorithm can factor large integers exponentially faster than the best-known
classical algorithms, which has significant implications for breaking RSA
cryptography.

References:
    - https://en.wikipedia.org/wiki/Shor%27s_algorithm
    - https://arxiv.org/abs/quant-ph/9508027 (Original Paper)

Time Complexity: O((log N)^3) for quantum part, O((log N)^2) for classical simulation
Space Complexity: O(log N)
"""

from __future__ import annotations

import math
import random
from fractions import Fraction


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
        >>> gcd(100, 25)
        25
    """
    while b:
        a, b = b, a % b
    return a


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using trial division.

    Args:
        n: Integer to check for primality

    Returns:
        True if n is prime, False otherwise

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(15)
        False
        >>> is_prime(1)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_perfect_power(n: int) -> tuple[int, int] | None:
    """
    Check if n is a perfect power (n = a^b for some integers a, b > 1).

    Args:
        n: Integer to check

    Returns:
        Tuple (base, exponent) if n is a perfect power, None otherwise

    Examples:
        >>> is_perfect_power(8)
        (2, 3)
        >>> is_perfect_power(27)
        (3, 3)
        >>> is_perfect_power(15)
        >>> is_perfect_power(16)
        (4, 2)
    """
    if n <= 1:
        return None

    for b in range(2, int(math.log2(n)) + 1):
        a = round(n ** (1 / b))
        # Check nearby values due to floating point errors
        for candidate in [a - 1, a, a + 1]:
            if candidate > 1 and candidate**b == n:
                return (candidate, b)
    return None


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    Compute (base^exponent) mod modulus efficiently using binary exponentiation.

    Args:
        base: Base of the exponentiation
        exponent: Exponent value
        modulus: Modulus for the operation

    Returns:
        (base^exponent) mod modulus

    Examples:
        >>> modular_exponentiation(2, 10, 1000)
        24
        >>> modular_exponentiation(3, 5, 13)
        9
        >>> modular_exponentiation(7, 256, 13)
        9
    """
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def find_order(a: int, n: int) -> int | None:
    """
    Find the multiplicative order of a modulo n.

    The order r is the smallest positive integer such that a^r ≡ 1 (mod n).
    This is the classical simulation of the quantum period-finding subroutine.

    In a real quantum computer, this would use Quantum Fourier Transform
    to find the period in polynomial time. Here we simulate it classically.

    Args:
        a: Base integer (must be coprime to n)
        n: Modulus

    Returns:
        The order r if found, None otherwise

    Examples:
        >>> find_order(2, 15)
        4
        >>> find_order(7, 15)
        4
        >>> find_order(11, 15)
        2
    """
    if gcd(a, n) != 1:
        return None

    r = 1
    current = a % n

    # In practice, order is bounded by Euler's totient function φ(n)
    # For simulation, we check up to n
    max_iterations = n

    while r < max_iterations:
        if current == 1:
            return r
        current = (current * a) % n
        r += 1

    return None


def quantum_period_finding_simulation(a: int, n: int) -> int | None:
    """
    Simulate the quantum period-finding algorithm.

    In a real quantum implementation, this would:
    1. Create a superposition of all states |x⟩
    2. Compute |x⟩|a^x mod N⟩
    3. Apply Quantum Fourier Transform
    4. Measure to get a value related to the period

    This classical simulation directly computes the period.

    Args:
        a: Base for modular exponentiation
        n: Number to factor

    Returns:
        The period r such that a^r ≡ 1 (mod n), or None if not found

    Examples:
        >>> quantum_period_finding_simulation(7, 15)
        4
        >>> quantum_period_finding_simulation(11, 21)
        6
    """
    return find_order(a, n)


def continued_fraction_expansion(numerator: int, denominator: int) -> list[int]:
    """
    Compute the continued fraction expansion of a rational number.

    Args:
        numerator: Numerator of the fraction
        denominator: Denominator of the fraction

    Returns:
        List of coefficients in the continued fraction expansion

    Examples:
        >>> continued_fraction_expansion(7, 15)
        [0, 2, 7]
        >>> continued_fraction_expansion(3, 8)
        [0, 2, 1, 2]
    """
    coefficients = []
    while denominator != 0:
        coefficients.append(numerator // denominator)
        numerator, denominator = denominator, numerator % denominator
    return coefficients


def convergents_from_continued_fraction(coefficients: list[int]) -> list[Fraction]:
    """
    Compute the convergents from a continued fraction expansion.

    Args:
        coefficients: Continued fraction coefficients

    Returns:
        List of convergent fractions

    Examples:
        >>> convergents = convergents_from_continued_fraction([0, 2, 7])
        >>> [(f.numerator, f.denominator) for f in convergents]
        [(0, 1), (1, 2), (7, 15)]
    """
    convergents = []
    for i in range(len(coefficients)):
        # Compute the i-th convergent
        fraction = Fraction(coefficients[i])
        for j in range(i - 1, -1, -1):
            fraction = coefficients[j] + Fraction(1, fraction)
        convergents.append(Fraction(fraction))
    return convergents


def shors_algorithm(n: int, max_attempts: int = 10) -> tuple[int, int] | None:
    """
    Shor's algorithm for integer factorization.

    This algorithm finds a non-trivial factor of a composite integer N.
    It combines classical pre/post-processing with a quantum period-finding
    subroutine (simulated classically here).

    Algorithm steps:
    1. Check if N is even, prime, or a perfect power (classical)
    2. Choose a random integer a where 1 < a < N
    3. Compute gcd(a, N) - if > 1, we found a factor
    4. Find the period r of f(x) = a^x mod N (quantum part)
    5. If r is odd, retry with different a
    6. Compute gcd(a^(r/2) ± 1, N) to find factors

    Args:
        n: The integer to factor (must be > 1, composite, and odd)
        max_attempts: Maximum number of random attempts

    Returns:
        A tuple (p, q) of non-trivial factors if found, None otherwise

    Raises:
        ValueError: If n is less than 2, even, or prime

    Examples:
        >>> result = shors_algorithm(15)
        >>> result is not None and result[0] * result[1] == 15
        True
        >>> result = shors_algorithm(21)
        >>> result is not None and result[0] * result[1] == 21
        True
        >>> result = shors_algorithm(35)
        >>> result is not None and result[0] * result[1] == 35
        True
        >>> shors_algorithm(2)
        Traceback (most recent call last):
            ...
        ValueError: n must be odd and greater than 2
        >>> shors_algorithm(17)
        Traceback (most recent call last):
            ...
        ValueError: n is prime and cannot be factored
    """
    # Input validation
    if n < 3 or n % 2 == 0:
        raise ValueError("n must be odd and greater than 2")

    if is_prime(n):
        raise ValueError("n is prime and cannot be factored")

    # Check if n is a perfect power
    if (perfect_power := is_perfect_power(n)) is not None:
        base, _ = perfect_power
        return (base, n // base)

    # Main factorization loop
    for _ in range(max_attempts):
        # Step 1: Choose random a where 1 < a < n
        a = random.randint(2, n - 1)

        # Step 2: Check if a shares a factor with n
        common_factor = gcd(a, n)
        if common_factor > 1:
            return (common_factor, n // common_factor)

        # Step 3: Find the period r (quantum subroutine)
        r = quantum_period_finding_simulation(a, n)

        if r is None:
            continue

        # Step 4: r must be even for the algorithm to work
        if r % 2 != 0:
            continue

        # Step 5: Compute a^(r/2) mod n
        x = modular_exponentiation(a, r // 2, n)

        # Step 6: Check that a^(r/2) ≢ -1 (mod n)
        if x == n - 1:
            continue

        # Step 7: Compute factors using gcd
        factor1 = gcd(x - 1, n)
        factor2 = gcd(x + 1, n)

        # Check for non-trivial factors
        if 1 < factor1 < n:
            return (factor1, n // factor1)
        if 1 < factor2 < n:
            return (factor2, n // factor2)

    return None


def demonstrate_rsa_vulnerability(p: int, q: int) -> dict:
    """
    Demonstrate how Shor's algorithm breaks RSA encryption.

    This function shows the vulnerability of RSA to quantum attacks by:
    1. Generating RSA public key from primes p and q
    2. Using Shor's algorithm to factor n = p * q
    3. Recovering the private key

    Args:
        p: First prime number
        q: Second prime number

    Returns:
        Dictionary containing RSA parameters and attack results

    Examples:
        >>> result = demonstrate_rsa_vulnerability(3, 5)
        >>> result['n']
        15
        >>> result['factors_found'] == (3, 5) or result['factors_found'] == (5, 3)
        True
        >>> result['attack_successful']
        True
    """
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both p and q must be prime numbers")

    # Generate RSA modulus
    n = p * q

    # Euler's totient
    phi_n = (p - 1) * (q - 1)

    # Common public exponent
    e = 65537
    if gcd(e, phi_n) != 1:
        # Find alternative e
        for e in range(3, phi_n, 2):
            if gcd(e, phi_n) == 1:
                break

    # Attack using Shor's algorithm
    factors = shors_algorithm(n)

    result = {
        "n": n,
        "public_exponent": e,
        "original_primes": (p, q),
        "phi_n": phi_n,
        "factors_found": factors,
        "attack_successful": factors is not None,
    }

    return result


def factor_with_explanation(n: int) -> None:
    """
    Factor a number using Shor's algorithm with step-by-step explanation.

    Args:
        n: The number to factor

    Examples:
        >>> factor_with_explanation(15)  # doctest: +ELLIPSIS
        ===================...
        Shor's Algorithm - Factoring 15
        ===================...
        ...
        Step 1: Preliminary checks
        ...
        Step 2: Quantum period finding (simulated)
        ...
        Step 3: Factor extraction
          - Successfully found factors!
        ...
        RESULT: 15 = ...
        ===================...
    """
    print("=" * 60)
    print(f"Shor's Algorithm - Factoring {n}")
    print("=" * 60)
    print()

    print("Step 1: Preliminary checks")
    print(f"  - {n} is {'odd ✓' if n % 2 == 1 else 'even ✗'}")
    print(f"  - {n} is {'not prime ✓' if not is_prime(n) else 'prime ✗'}")
    pp = is_perfect_power(n)
    print(f"  - {n} is {'not ' if pp is None else ''}a perfect power", end="")
    print(" ✓" if pp is None else f" = {pp[0]}^{pp[1]} ✗")
    print()

    print("Step 2: Quantum period finding (simulated)")
    print("  - Selecting random base a...")

    if factors := shors_algorithm(n):
        print("  - Found suitable parameters")
        print()
        print("Step 3: Factor extraction")
        print("  - Successfully found factors!")
        print()
        print("=" * 60)
        print(f"RESULT: {n} = {factors[0]} × {factors[1]}")
        print("=" * 60)
    else:
        print("  - Failed to find factors")
        print()
        print("=" * 60)
        print("RESULT: Factorization failed")
        print("=" * 60)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    print("\n" + "=" * 60)
    print("SHOR'S ALGORITHM DEMONSTRATION")
    print("=" * 60)

    # Test factorization of various numbers
    test_numbers = [15, 21, 35, 77, 91, 143, 221, 323]

    print("\nFactoring composite numbers:")
    print("-" * 40)
    for num in test_numbers:
        result = shors_algorithm(num)
        if result:
            p, q = result
            print(f"{num:4d} = {p} × {q}")
        else:
            print(f"{num:4d} = Failed to factor")

    # Demonstrate RSA vulnerability
    print("\n" + "=" * 60)
    print("RSA VULNERABILITY DEMONSTRATION")
    print("=" * 60)

    # Using small primes for demonstration
    demo = demonstrate_rsa_vulnerability(11, 13)
    print(f"\nRSA modulus n = {demo['n']}")
    print(f"Original primes: {demo['original_primes']}")
    print(f"Factors found by Shor's algorithm: {demo['factors_found']}")
    print(f"Attack successful: {demo['attack_successful']}")

    # Interactive factorization with explanation
    print("\n")
    factor_with_explanation(91)
