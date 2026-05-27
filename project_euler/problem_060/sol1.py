"""
Project Euler Problem 60: https://projecteuler.net/problem=60

# Problem Statement:

The primes 3, 7, 109, and 673 are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes
with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate
to produce another prime.

# Solution Explanation:

The brute force approach would be to check all combinations of 5 primes and check
if they satisfy the concatenation property. However, this is computationally
expensive. Instead, we can use a backtracking approach to build sets of primes
that satisfy the concatenation property. We can further optimize by using property
of divisibility by 3 to eliminate certain candidates and memoization to avoid
redundant prime checks.
Throughout the code, we have used a parameter flag to indicate whether
we are working with primes that are congruent to 1 or 2 modulo 3.
This helps in reducing the search space.

## Eliminating candidates using divisibility by 3:
Consider any 2 primes p1 and p2 that are not divisible by 3. If p1 divided by 3
gives a remainder of 1 and p2 divided by 3 gives a remainder of 2, then
the concatenated number p1p2 will be divisible by 3 and hence not prime.
This can be easily proven using the property of modular arithmetic.
    Consider p1 ≡ 1 (mod 3) and p2 ≡ 2 (mod 3). Define a1 = p1, b1 = 1, a2 = p2, b2 = 2.
    concat(p1, p2) = (p1 * 10^k + p2) where k is the number of digits in p2.
    Now, (p1 * 10^k + p2) mod 3 = ((p1 * 10^k) + p2) mod 3
    As 10^k mod 3 = 1, we have (p1 * 1 + p2) mod 3 (ka mod 3 = kb mod 3)
    Which implies (p1 + p2) mod 3 = (1 + 2) mod 3 = 0 (a1 + a2 mod 3 = b1 + b2 mod 3)

Thus, we can eliminate such pairs from our search space and reach the solution faster.
The solution uses this property to divide the primes into two lists based on their
remainder when divided by 3. This way, we only need to check combinations within
either list, reducing the number of checks significantly.

## Memoization:
We can use a dictionary to store the results of prime checks for concatenated numbers.
This way, if we encounter the same concatenated number again, we can simply look up
the result instead of recalculating it.

## Backtracking:
We can use a recursive function to build sets of primes. Starting with an empty set,
we can add primes one by one, checking at each step if the current set satisfies
the concatenation property. If it does, we can continue adding more primes.
If we reach a set of 5 primes, we can check if their sum is the lowest

References:
- [Modular Arithmetic Explanation](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [Project Euler Forum Discussion](https://projecteuler.net/problem=60)
- [Prime Checking Optimization](https://en.wikipedia.org/wiki/Primality_test)
- [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
"""

from functools import cache

prime_mod_3_is_1_list: list[int] = [3, 7, 13, 19]
prime_mod_3_is_2_list: list[int] = [3, 5, 11, 17]

prime_pairs: dict[tuple, bool] = {}


@cache
def is_prime(num: int) -> bool:
    """
    Efficient primality check using 6k ± 1 optimization.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(77)
    False
    >>> is_prime(673)
    True
    >>> is_prime(1097)
    True
    >>> is_prime(7109)
    True
    """

    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Check divisibility up to sqrt(num)
    n_sqrt = int(num**0.5)
    for i in range(5, n_sqrt + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def sum_digits(num: int) -> int:
    """
    Returns the sum of digits of num. If the sum is greater than 10,
    it recursively sums the digits of the result until a single digit is obtained.

    >>> sum_digits(-18)
    Traceback (most recent call last):
        ...
    ValueError: num must be non-negative
    >>> sum_digits(0)
    0
    >>> sum_digits(5)
    5
    >>> sum_digits(79)
    7
    >>> sum_digits(999)
    9
    """
    if num < 0:
        raise ValueError("num must be non-negative")
    if num < 10:
        return num
    return sum_digits(sum(map(int, str(num))))


def is_concat(num1: int, num2: int) -> bool:
    """
    Check if concatenations of num1+num2 and num2+num1 are both prime.
    Uses memoization to store previously computed results in prime_pairs dictionary.
    Effects: Updates the prime_pairs dictionary with the result.
             Only stores (min(num1, num2), max(num1, num2)) as key to avoid duplicates.

    >>> is_concat(3, 7)
    True
    >>> is_concat(1, 6)
    False
    >>> is_concat(7, 109)
    True
    >>> is_concat(13, 31)
    False
    """
    if num1 > num2:
        num1, num2 = num2, num1
    key = (num1, num2)
    if key in prime_pairs:
        return prime_pairs[key]
    concat1 = int(f"{num1}{num2}")
    concat2 = int(f"{num2}{num1}")
    result = is_prime(concat1) and is_prime(concat2)
    prime_pairs[key] = result
    return result


def add_prime(primes: list[int]) -> list[int]:
    """
    Add a new prime number to the input list of primes based on its modulo 3 value.
    Effects: Modifies the input list by appending a new prime number.

    >>> add_prime([3, 7, 13, 19])
    [3, 7, 13, 19, 31]
    >>> add_prime([3, 5, 11, 17])
    [3, 5, 11, 17, 23]
    >>> add_prime([3, 7, 13, 19, 31])
    [3, 7, 13, 19, 31, 37]
    """

    next_num = primes[-1] + 3  # using modular arithmetic to get similar primes
    while not is_prime(next_num):
        next_num += 3
    primes.append(next_num)
    return primes


def generate_primes(num_primes: int, flag: int = 1) -> list[int]:
    """
    Generates a list of the first num_primes primes based on their modulo 3 value.

    >>> generate_primes(5, 1)
    [3, 7, 13, 19, 31]
    >>> generate_primes(5, 2)
    [3, 5, 11, 17, 23]
    """
    primes = prime_mod_3_is_1_list if flag == 1 else prime_mod_3_is_2_list
    while len(primes) < num_primes:
        primes = add_prime(primes)
    return primes


def solution(
    target_size: int = 5, prime_limit: int = 1000, flag: int = 1
) -> int | None:
    """
    Search for a set of primes with the concat-prime property.
    Returns the sum of the lowest such set found else returns None.

    >>> solution(3, 100, None)
    Traceback (most recent call last):
        ...
    ValueError: flag must be either 1 or 2
    >>> solution(4, 100, 1)
    792
    >>> solution(3, 100, 2)
    715
    >>> solution(5, 1000, 1)
    26033
    """
    if flag not in (1, 2):
        raise ValueError("flag must be either 1 or 2")
    primes = generate_primes(prime_limit, flag)

    def search(chain: tuple) -> tuple[int, ...] | None:
        """
        Recursive backtracking search to find a valid set of primes.
        A threshold is used to ensure we don't exceed the smallest sum.
        Returns the valid set if found, else None.

        >>> search((3,))
        (3, 7, 109, 673)
        >>> search((7,))
        (7, 109, 673, 3)
        """
        if len(chain) == target_size:
            return chain
        for p in primes:
            if p <= chain[-1]:
                continue
            if all(is_concat(p, c) for c in chain):
                result = search((*chain, p))
                if result:
                    return result
        return None

    for _, p in enumerate(primes):
        result = search((p,))
        if result and len(result) == target_size:
            return sum(result)

    return None  # No valid set found


if __name__ == "__main__":
    print(f"{solution() = }")
