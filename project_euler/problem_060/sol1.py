"""
Project Euler Problem 60: https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to
produce another prime.

On the algorithm:
- Generate PRIMES_SIZE primes
- Iterate through the primes, starting from the smallest available. On the top-level of
the recursion, generate a list of primes that can be concatenated to the current prime.
This list will be used for the next recursive calls.
- Find all matches for that prime and store them in a list that will be used for the
next recursive calls
- Test matches for the next recursive calls, register the smallest sum found
- Concatenation is done with arithmetic operations. String processing is generally
slower.
"""
import collections.abc
import math
from time import time

PRIMES_SIZE = 1.2e3
COUNTER = True


def get_order(n: int) -> int:
    """
    Get the order of a number n, in order to facilitate concatenation.
    get_order(n) = x -> 10^x <= n < 10^(x+1)

    >>> get_order(1)
    0
    >>> get_order(10)
    1
    >>> get_order(12345)
    4
    """

    return int(math.log(n, 10))


def test_concatenate(num1: int, num2: int) -> bool:
    """
    Test if two numbers concatenate to form a prime, for both possible arrangements.
    Use arithmetic operations to concatenate.

    >> test_concatenate(3, 7)
    True
    >>> test_concatenate(2, 10)
    False
    >>> test_concatenate(673, 109)
    True
    """

    if not is_prime(num1 * 10 ** (get_order(num2) + 1) + num2):
        return False

    if not is_prime(num2 * 10 ** (get_order(num1) + 1) + num1):
        return False

    return True


def is_prime(n) -> bool:
    """
    Simple prime test

    >>> is_prime(2)
    True
    >>> is_prime(100000007)
    True
    >>> is_prime(10000007)
    False
    """
    for divider in range(2, int(n**0.5) + 1):
        if int(n) % divider == 0:
            return False
    return True


def prime_generator() -> collections.abc.Iterator[int]:
    """
    Custom prime generator for primes used in this problem
    Skip 2 and 5: no primes end with 2 or 5 except for 2 and 5, so they're not useful
    for this problem

    >>> [[next(x) for _ in range(5)] for x in [(prime_generator())]][0]
    [3, 7, 11, 13, 17]
    """

    local_output: int = 3
    yield local_output
    local_output = 5

    while True:
        local_output += 2
        if is_prime(local_output):
            yield local_output


def solution_helper(
    depth: int, start_idx: int, to_test: list[int], matches: list[int]
) -> list[int]:
    """
    Recursive helper function for solution(), search for more primes from
    matches[start_idx:] that can be concatenated to all primes from to_test until
    recursion reaches depth 0. Return the list of primes if a solution is found, False
    otherwise.

    >>> solution_helper(depth=3, start_idx=1, to_test=[3],matches=[3, 7, 100, 109, 673])
    [3, 7, 109, 673]
    >>> solution_helper(depth=2, start_idx=0, to_test=[7], matches=[10, 20, 30, 40, 50])
    []
    """

    if depth == 0:
        return to_test

    for i in range(start_idx, len(matches)):
        # Test all previous matches:
        passes = True
        for j in range(len(to_test)):
            if not test_concatenate(matches[i], to_test[j]):
                passes = False
                break
        if not passes:
            continue
        if output := solution_helper(depth - 1, i + 1, to_test + [matches[i]], matches):
            return output
    return []


def solution(n_primes: int = 5) -> int:
    """
    This function behaves similarly to solution_helper, but it is not recursive and
    defines some variables that are used in the recursive calls. It also defines a list
    of matches for every prime it tests, optimizing search time.

    >>> solution(n_primes=2)
    14
    >>> solution(n_primes=3)
    405
    >>> solution(n_primes=4)
    3146
    """

    # Generate primes and start variables
    start = time()
    generator: collections.abc.Iterator[int] = prime_generator()
    primes: list[int] = []
    output: int = int(5e4)  # initialize with theoretical max value
    for _ in range(int(PRIMES_SIZE)):
        primes.append(next(generator))
    if COUNTER:
        print(f"{int(PRIMES_SIZE)} primes generated in {time() - start}s")

    # Main loop
    limit = output ** (1 / n_primes) * n_primes
    for i in range(len(primes)):
        # Break main loop if the current minimal number is larger than the nth root
        # of the current output times n, with n being the amount of primes searched.
        # The reason for this is to reduce the search space with a reasonable upper
        # bound. Analysis with lower values for n_primes shows that this is a valid
        # optimization.
        if primes[i] > limit:
            break

        # Iterate larger primes, store in matches. This should optimize the nested loops
        matches: list[int] = []
        prime: int = primes[i]
        for j in range(i + 1, len(primes)):
            if test_concatenate(prime, primes[j]):
                matches.append(primes[j])

        # Match every candidate with every other candidate until 5 are found
        if found := solution_helper(
            depth=n_primes - 1, start_idx=+1, to_test=[prime], matches=matches
        ):
            output = min(output, sum(found))

    if COUNTER:
        print(f"Done ({time() - start}s)")
    return output


if __name__ == "__main__":
    print(f"{solution(4) = }")
