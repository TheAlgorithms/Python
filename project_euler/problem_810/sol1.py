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

from array import array


def xor_multiply(op_a: int, op_b: int) -> int:
    """
    Perform XOR multiplication of two integers, equivalent to polynomial
    multiplication in GF(2).

    >>> xor_multiply(3, 5)  # (011) ⊗ (101)
    15
    """
    res = 0
    while op_b:
        if op_b & 1:
            res ^= op_a
        op_a <<= 1
        op_b >>= 1
    return res


def divisors(num: int) -> set[int]:
    """
    Return all divisors of `num` (excluding 0).

    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}
    """
    s = {1}
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            s.add(i)
            s.add(num // i)
    s.add(num)
    return s


def mobius_table(num: int) -> list[int]:
    """
    Generate a variant of Möbius function values from 1 to num.

    >>> mobius_table(10)[:6]
    [0, 1, -1, -1, 0, -1]
    """
    mob = [1] * (num + 1)
    is_prime = [True] * (num + 1)
    mob[0] = 0

    for p in range(2, num + 1):
        if is_prime[p]:
            mob[p] = -1
            for j in range(2 * p, num + 1, p):
                is_prime[j] = False
                mob[j] *= -1
            p2 = p * p
            if p2 <= num:
                for j in range(p2, num + 1, p2):
                    mob[j] = 0
    return mob


def count_irreducibles(deg: int) -> int:
    """
    Count the number of irreducible polynomials of degree `deg` over GF(2)
    using the variant of Möbius function.

    >>> count_irreducibles(3)
    2
    """
    mob = mobius_table(deg)
    total = 0
    for div in divisors(deg) | {deg}:
        total += mob[div] * (1 << (deg // div))
    return total // deg


def find_xor_prime(rank: int) -> int:
    """
    Find the Nth XOR prime using a bitarray-based sieve.

    >>> find_xor_prime(10)
    41
    """
    total, degree = 0, 1
    while total + count_irreducibles(degree) < rank:
        total += count_irreducibles(degree)
        degree += 1

    limit = 1 << (degree + 1)

    sieve = array("B", [1]) * limit
    sieve[0] = sieve[1] = 0

    current = 0
    for i in range(2, limit):
        if sieve[i]:
            current += 1
            if current == rank:
                return i

            j = i
            while True:
                prod = xor_multiply(i, j)
                if prod >= limit:
                    break
                sieve[prod] = 0
                j += 1

    raise ValueError("Failed to locate the requested XOR-prime")


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
