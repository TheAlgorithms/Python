"""
Project Euler Problem 95: https://projecteuler.net/problem=95

Amicable Chains

The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and
the sum of the proper divisors of 284 is 220, forming a chain of two numbers.
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains.
For example, starting with 12496, we form a chain of five numbers:
    12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with
no element exceeding one million.

Solution is doing the following:
- Get relevant prime numbers
- Iterate over product combination of prime numbers to generate all non-prime
  numbers up to max number, by keeping track of prime factors
- Calculate the sum of factors for each number
- Iterate over found some factors to find longest chain
"""

from math import isqrt, prod


def sum_primes(primes_degrees: dict[int, int], num: int) -> int:
    """
    Calculates the sum of factors from all prime exponents.

    >>> sum_primes(primes_degrees={2: 1, 3: 1}, num=6)
    6
    """
    return prod((prime ** (degree + 1) - 1) // (prime - 1) for prime, degree in primes_degrees.items()) - num


def generate_primes(n: int):
    """
    Calculates the list of primes up to and including n.

    >>> generate_primes(6)
    [2, 3, 5]
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, isqrt(n) + 1):
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


def multiply(chain, primes, prime, prev_n, n_max, prev_sum, primes_d):
    """
    Run over all prime combinations to generate non-prime numbers.

    >>> multiply([None] * 3, {2}, 2, 1, 2, 0, {})
    """

    number = prev_n * prime
    primes_d[prime] = primes_d.get(prime, 0) + 1
    if prev_n % prime != 0:
        new_sum = prev_sum * (prime + 1) + prev_n
    else:
        new_sum = sum_primes(primes_d, number)
    chain[number] = new_sum
    for p in primes:
        if p >= prime:
            number_n = p * number
            if number_n > n_max:
                break
            multiply(chain, primes, p, number, n_max, new_sum, primes_d.copy())


def find_longest_chain(chain, n_max):
    """
    Finds the smallest element and length of longest chain

    >>> find_longest_chain([0, 0, 0, 0, 0, 0, 6], 6)
    (6, 1)
    """

    length_max = 0
    elem_max = 0
    for i in range(2, len(chain)):
        start = i
        length = 1
        el = chain[i]
        visited = {i}
        while el > 1 and el <= n_max and el not in visited:
            length += 1
            visited.add(el)
            el = chain[el]

        if el == start and length > length_max:
            length_max = length
            elem_max = start

    return elem_max, length_max


def solution(n_max: int = 1000000) -> int:
    """
    Runs the calculation for numbers <= n_max.

    >>> solution(10)
    6
    >>> solution(200000)
    12496
    """

    primes = generate_primes(n_max)
    chain = [0] * (n_max + 1)
    for p in primes:
        if p * p > n_max:
            break
        multiply(chain, primes, p, 1, n_max, 0, {})

    chain_start, _ = find_longest_chain(chain, n_max)
    return chain_start


if __name__ == "__main__":
    print(f"{solution() = }")
