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

from math import isqrt


def generate_primes(max_num: int) -> list[int]:
    """
    Calculates the list of primes up to and including `max_num`.

    >>> generate_primes(6)
    [2, 3, 5]
    """
    are_primes = [True] * (max_num + 1)
    are_primes[0] = are_primes[1] = False
    for i in range(2, isqrt(max_num) + 1):
        if are_primes[i]:
            for j in range(i * i, max_num + 1, i):
                are_primes[j] = False

    return [prime for prime, is_prime in enumerate(are_primes) if is_prime]


def multiply(
    chain: list[int],
    primes: list[int],
    min_prime_idx: int,
    prev_num: int,
    max_num: int,
    prev_sum: int,
    primes_degrees: dict[int, int],
) -> None:
    """
    Run over all prime combinations to generate non-prime numbers.

    >>> chain = [0] * 3
    >>> primes_degrees = {}
    >>> multiply(
    ...     chain=chain,
    ...     primes=[2],
    ...     min_prime_idx=0,
    ...     prev_num=1,
    ...     max_num=2,
    ...     prev_sum=0,
    ...     primes_degrees=primes_degrees,
    ... )
    >>> chain
    [0, 0, 1]
    >>> primes_degrees
    {2: 1}
    """

    min_prime = primes[min_prime_idx]
    num = prev_num * min_prime

    min_prime_degree = primes_degrees.get(min_prime, 0)
    min_prime_degree += 1
    primes_degrees[min_prime] = min_prime_degree

    new_sum = prev_sum * min_prime + (prev_sum + prev_num) * (min_prime - 1) // (
        min_prime**min_prime_degree - 1
    )
    chain[num] = new_sum

    for prime_idx in range(min_prime_idx, len(primes)):
        if primes[prime_idx] * num > max_num:
            break

        multiply(
            chain=chain,
            primes=primes,
            min_prime_idx=prime_idx,
            prev_num=num,
            max_num=max_num,
            prev_sum=new_sum,
            primes_degrees=primes_degrees.copy(),
        )


def find_longest_chain(chain: list[int], max_num: int) -> int:
    """
    Finds the smallest element of longest chain

    >>> find_longest_chain(chain=[0, 0, 0, 0, 0, 0, 6], max_num=6)
    6
    """

    max_len = 0
    min_elem = 0
    for start in range(2, len(chain)):
        visited = {start}
        elem = chain[start]
        length = 1

        while elem > 1 and elem <= max_num and elem not in visited:
            visited.add(elem)
            elem = chain[elem]
            length += 1

        if elem == start and length > max_len:
            max_len = length
            min_elem = start

    return min_elem


def solution(max_num: int = 1000000) -> int:
    """
    Runs the calculation for numbers <= `max_num`.

    >>> solution(10)
    6
    >>> solution(200000)
    12496
    """

    primes = generate_primes(max_num)
    chain = [0] * (max_num + 1)
    for prime_idx, prime in enumerate(primes):
        if prime**2 > max_num:
            break

        multiply(
            chain=chain,
            primes=primes,
            min_prime_idx=prime_idx,
            prev_num=1,
            max_num=max_num,
            prev_sum=0,
            primes_degrees={},
        )

    return find_longest_chain(chain=chain, max_num=max_num)


if __name__ == "__main__":
    print(f"{solution() = }")
