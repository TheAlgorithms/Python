"""
Project Euler Problem 124: https://projecteuler.net/problem=124

Ordered Radicals

"""

from numpy import sqrt


def generate_primes(n: int) -> list[int]:
    """
    Calculates the list of primes up to and including n.

    >>> generate_primes(6)
    [2, 3, 5]
    """

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n + 1)) + 1):
        if primes[i]:
            j = i * i
            while j <= n:
                primes[j] = False
                j += i
    primes_list = []
    for i in range(2, len(primes)):
        if primes[i]:
            primes_list += [i]
    return primes_list


def generate_n(factors: list[int], n_max: int, n: int, res: set[int]):
    """
    Generates all numbers n that can be constructed out of 'factors', with any
    multiplicity, but that do no exceed 'n_max'.

    >>> generate_n([2], 10, 1, set())
    """

    if len(factors) == 0:
        return
    fac = factors[0]
    factors_new = factors[1:]
    while n <= n_max:
        generate_n(factors_new, n_max, n, res)
        res.add(n)
        n *= fac
    return


def generate_rads(
    factors_all: list[int], n_max: int, n: int, res: dict, factors_prev: list[int]
):
    """
    Generates all rads and associated factors, e.g., rad = factor_1 * ... * factor_k.
    Output is stored in 'res' dict argument.

    >>> generate_rads([2], 10, 1, {}, [])
    """

    for i in range(len(factors_all)):
        f = factors_all[i]
        n_new = n * f
        if n_new > n_max:
            return
        # factors_new = factors_prev + [f]
        factors_new = [*factors_prev, f]
        res[n_new] = factors_new
        generate_rads(factors_all[(i + 1) :], n_max, n_new, res, factors_new)
    return


def solution(n_max: int = 100000, k: int = 10000) -> int:
    """
    Loops over sorted 'rads' and generates all numbers 'n' for rad.
    Keeps track of total number of n, and when k falls inside some rad,
    it sorts all 'n' for it and picks up associated n.

    >>> solution(10, 6)
    9
    >>> solution(10, 9)
    7
    """

    if k == 1:
        return 1

    primes = generate_primes(n_max)
    tot = 1
    rads_d: dict[int, list[int]] = {}
    factor_prev: list[int] = []
    generate_rads(primes, n_max, 1, rads_d, factor_prev)
    rads = sorted(rads_d)

    for r in rads:
        facts = rads_d[r]
        res: set[int] = set()
        generate_n(facts, n_max, r, res)
        res_len = len(res)
        if tot + res_len >= k:
            return sorted(res)[k - tot - 1]
        tot += res_len
    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
