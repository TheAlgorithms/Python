"""
Project Euler Problem 810: https://projecteuler.net/problem=810

We use x ⊕ y for the bitwise XOR of x and y.
Define the XOR-product of x and y, denoted by x ⊗ y,
similar to a long multiplication in base 2,
except the intermediate results are XORed instead of usual integer addition.

For example, 7 ⊗ 3 = 9, or in base 2, 111_2 ⊗ 11_2 = 1001_2:
        111
    ⊗   11
    -------
        111
       111
    -------
       1001
An XOR-Prime is an integer n greater than 1 that is not an
XOR-product of two integers greater than 1.
The above example shows that 9 is not an XOR-prime.
Similarly, 5 = 3 ⊗ 3 is not an XOR-prime.
The first few XOR-primes are 2, 3, 7, 11, 13, ... and the 10th XOR-prime is 41.

Find the 5,000,000.th XOR-prime.

References:
http://en.wikipedia.org/wiki/M%C3%B6bius_function

"""


def xor_multiply(a: int, b: int) -> int:
    """
    Perform XOR multiplication of two integers, equivalent to polynomial
    multiplication in GF(2).

    >>> xor_multiply(3, 5)  # (011) ⊗ (101)
    15
    """
    res = 0
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        b >>= 1
    return res


def divisors(n: int) -> set[int]:
    """
    Return all divisors of n (excluding 0).

    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}
    """
    s = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    s.add(n)
    return s


def mobius_table(n: int) -> list[int]:
    """
    Generate Möbius function values from 1 to n.

    >>> mobius_table(10)[:6]
    [0, 1, -1, -1, 0, -1]
    """
    mob = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    mob[0] = 0

    for p in range(2, n + 1):
        if is_prime[p]:
            mob[p] = -1
            for j in range(2 * p, n + 1, p):
                is_prime[j] = False
                mob[j] *= -1
            p2 = p * p
            if p2 <= n:
                for j in range(p2, n + 1, p2):
                    mob[j] = 0
    return mob


def count_irreducibles(d: int) -> int:
    """
    Count the number of irreducible polynomials of degree d over GF(2)
    using the Möbius function.

    >>> count_irreducibles(3)
    2
    """
    mob = mobius_table(d)
    total = 0
    for div in divisors(d) | {d}:
        total += mob[div] * (1 << (d // div))
    return total // d


def find_xor_prime(rank: int) -> int:
    """
    Find the Nth XOR prime using a bitarray-based sieve.

    >>> find_xor_prime(10)
    41
    """
    total, degree = 0, 1
    while True:
        count = count_irreducibles(degree)
        if total + count > rank:
            break
        total += count
        degree += 1

    limit = 1 << (degree + 1)

    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for even in range(4, limit, 2):
        sieve[even] = False

    current = 1
    for i in range(3, limit, 2):
        if sieve[i]:
            current += 1
            if current == rank:
                return i

            j = i
            while True:
                prod = xor_multiply(i, j)
                if prod >= limit:
                    break
                sieve[prod] = False
                j += 2

    raise ValueError(
        "Failed to locate the requested XOR-prime within the computed limit"
    )


def solution(limit: int = 5000001) -> int:
    """
    Wrapper for Project Euler-style solution function.

    >>> solution(10)
    41
    """
    result = find_xor_prime(limit)
    return result


if __name__ == "__main__":
    print(f"{solution(5000000) = }")
