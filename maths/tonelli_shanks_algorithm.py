import random
import math


def is_prime(num: int) -> bool:
    """
    Checks if number is prime, for simplicity uses "bruteforce"
    Check other algorithms for example Miller-Rabin for better performance
    """
    if num < 2:
        return False

    for n in range(2, math.isqrt(num) + 1):
        if num % n == 0:
            return False

    return True


def legendre_symbol(a: int, p: int) -> int:
    """
    Legendre symbol
    Assumes that the check that p is an odd prime number has already been performed
    See description at https://en.wikipedia.org/wiki/Legendre_symbol
    >>> legendre_symbol(3, 3)
    0

    >>> legendre_symbol(2, 3)
    -1

    >>> legendre_symbol(1, 127)
    1
    """
    if a % p == 0:
        return 0

    # calculating Legendre symbol using Euler's criteria
    # See more at https://en.wikipedia.org/wiki/Euler%27s_criterion
    temp = pow(a, (p - 1) // 2, p)

    # if a is a non-quadratic residue by Euler's criteria we get a^(p-1)/2 = -1 (mod p)
    # since pow() works in such a way that we get -1 (mod p) as p-1
    # we convert this result to match the description
    if temp == p - 1:
        return -1

    return temp


def get_random_non_quadratic_residue(p: int) -> int:
    """
    Generates a random quadratic non-quadratic residue for odd prime number p
    Assumes that the check that p is an odd prime number has already been performed
    """
    while True:
        candidate = random.randint(1, p)
        if legendre_symbol(candidate, p) == -1:
            return candidate


def tonelli_shanks_algorithm(n: int, p: int) -> set[int]:
    """
    Main function for Tonelli-Shanks algorithm.

    Calculates x, such that x^2 = n (mod p)
    Works only with odd prime number p

    See more at https://en.wikipedia.org/wiki/Tonelli–Shanks_algorithm
    >>> tonelli_shanks_algorithm(5, 41)
    {28, 13}

    >>> tonelli_shanks_algorithm(10, 13)
    {6, 7}

    >>> tonelli_shanks_algorithm(17, 41)
    Traceback (most recent call last):
        ...
    ValueError: no integer solutions exist

    >>> tonelli_shanks_algorithm(56, 101)
    {64, 37}

    >>> tonelli_shanks_algorithm(881398088036, 1000000000039)
    {791399408049, 208600591990}

    >>> tonelli_shanks_algorithm(17, 44)
    Traceback (most recent call last):
        ...
    ValueError: p must be prime grater than 2
    """
    if not is_prime(p) or p == 2:
        raise ValueError("p must be prime grater than 2")

    if legendre_symbol(n, p) == -1:
        raise ValueError("no integer solutions exist")

    if p % 4 == 3:
        r = pow(n, (p + 1) // 4, p)
        res = set()
        res.add(r)
        res.add(p - r)
        return res

    # Step 1.
    temp = p - 1
    s = 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    q = temp

    # Step 2.
    z = get_random_non_quadratic_residue(p)

    # Step 3.
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    # Step 4.
    while True:
        if t % p == 1:
            res = set()
            res.add(r)
            res.add(p - r)
            return res

        # searches the least i, 0 < i < M, such that t^(2^i) = 1 (mod p)
        t2 = pow(t, 2, p)
        for i in range(1, m):
            if t2 % p == 1:
                break
            t2 = t2 * t2

        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        r = (r * b) % p
        c = pow(b, 2, p)
        t = (t * (b ** 2)) % p
