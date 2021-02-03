"""
Project Euler Problem 87: https://projecteuler.net/problem=87

The smallest number expressible as the sum of a prime square, prime cube, and prime
fourth power is 28. In fact, there are exactly four numbers below fifty that can be
expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?
"""


def solution(limit: int = 50000000) -> int:
    """
    Return the number of integers less than limit which can be expressed as the sum
    of a prime square, prime cube, and prime fourth power.
    >>> solution(50)
    4
    """
    ret = set()
    prime_square_limit = int((limit - 24) ** (1 / 2))

    primes = set(range(3, prime_square_limit + 1, 2))
    primes.add(2)
    for p in range(3, prime_square_limit + 1, 2):
        if p not in primes:
            continue
        primes.difference_update(set(range(p * p, prime_square_limit + 1, p)))

    for prime1 in primes:
        square = prime1 * prime1
        for prime2 in primes:
            cube = prime2 * prime2 * prime2
            if square + cube >= limit - 16:
                break
            for prime3 in primes:
                tetr = prime3 * prime3 * prime3 * prime3
                total = square + cube + tetr
                if total >= limit:
                    break
                ret.add(total)

    return len(ret)


if __name__ == "__main__":
    print(f"{solution() = }")
