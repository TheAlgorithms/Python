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

Find the 5,000,000 th XOR-prime.

References:
http://en.wikipedia.org/wiki/M%C3%B6bius_function

"""

import math


def get_divisors(num: int) -> set[int]:
    """
    Return all positive divisors of num.
    >>> get_divisors(12)
    {1, 2, 3, 4, 6, 12}
    """
    divisors = {1}
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    divisors.add(num)
    return divisors


def xor_multiply(op_a: int, op_b: int) -> int:
    """
    Perform XOR-based multiplication (polynomial multiplication mod 2).
    >>> xor_multiply(3, 5)
    15
    """
    result = 0
    while op_b:
        if op_b & 1:
            result ^= op_a
        op_a <<= 1
        op_b >>= 1
    return result


def mobius_table(lim: int, k: int = 2) -> list[int]:
    """
    Compute a modified Mobius function table up to `lim`.
    >>> mobius_table(10)[:6]
    [0, 1, -1, -1, 0, -1]
    """
    mob = [0] + [1] * lim
    is_prime = [True] * (lim + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, lim + 1):
        if is_prime[p]:
            mob[p] *= -1
            for mul in range(2 * p, lim + 1, p):
                is_prime[mul] = False
                mob[mul] *= -1

            p_pow = p**k
            if p_pow <= lim:
                for mul in range(p_pow, lim + 1, p_pow):
                    mob[mul] = 0
    return mob


def cnt_irred_pol(num: int) -> int:
    """
    Return the number of monic irreducible polynomials of degree num over GF(2).
    >>> cnt_irred_pol(3)
    2
    """
    mob = mobius_table(num)
    total = sum(mob[d] * (2 ** (num // d)) for d in get_divisors(num))
    return total // num


def xor_prime_func(tgt_idx: int) -> int:
    """
    Find the N-th XOR-prime (irreducible polynomial) index approximation.
    >>> xor_prime_func(10)
    41
    """
    total, degree = 0, 1

    while True:
        cnt = cnt_irred_pol(degree)
        if total + cnt > tgt_idx:
            break
        total += cnt
        degree += 1

    lim = 1 << (degree + 1)
    is_prime = [True] * lim
    is_prime[0] = is_prime[1] = False

    for even in range(4, lim, 2):
        is_prime[even] = False

    cnt = 1
    for num in range(3, lim, 2):
        if not is_prime[num]:
            continue

        cnt += 1
        if cnt == tgt_idx:
            return num

        mul = num
        while True:
            prod = xor_multiply(mul, num)
            if prod >= lim:
                break
            is_prime[prod] = False
            mul += 2

    raise ValueError("Could not compute the XOR-prime.")


def solution(nth: int = 5000000) -> int:
    """
    Compute the Nth XOR prime and print timing.
    >>> solution(10)
    41
    """
    result = xor_prime_func(nth)
    return result


if __name__ == "__main__":
    print(f"{solution() = }")
