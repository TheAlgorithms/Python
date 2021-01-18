"""
Project Euler Problem 203: https://projecteuler.net/problem=203

The binomial coefficients (n k) can be arranged in triangular form, Pascal's
triangle, like this:
                            1
                        1       1
                    1		2       1
                1		3		3       1
            1		4		6		4		1
        1		5		10		10		5		1
    1		6		15		20		15		6		1
1		7		21		35		35		21		7		1
                        .........

It can be seen that the first eight rows of Pascal's triangle contain twelve
distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n.
Of the twelve distinct numbers in the first eight rows of Pascal's triangle,
all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers
in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of
Pascal's triangle.

References:
- https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""

import math
from typing import List, Set


def get_pascal_triangle_unique_coefficients(depth: int) -> Set[int]:
    """
    Returns the unique coefficients of a Pascal's triangle of depth "depth".

    The coefficients of this triangle are symmetric. A further improvement to this
    method could be to calculate the coefficients once per level. Nonetheless,
    the current implementation is fast enough for the original problem.

    >>> get_pascal_triangle_unique_coefficients(1)
    {1}
    >>> get_pascal_triangle_unique_coefficients(2)
    {1}
    >>> get_pascal_triangle_unique_coefficients(3)
    {1, 2}
    >>> get_pascal_triangle_unique_coefficients(8)
    {1, 2, 3, 4, 5, 6, 7, 35, 10, 15, 20, 21}
    """
    coefficients = {1}
    previous_coefficients = [1]
    for step in range(2, depth + 1):
        coefficients_begins_one = previous_coefficients + [0]
        coefficients_ends_one = [0] + previous_coefficients
        previous_coefficients = []
        for x, y in zip(coefficients_begins_one, coefficients_ends_one):
            coefficients.add(x + y)
            previous_coefficients.append(x + y)
    return coefficients


def get_primes_squared(max_number: int) -> List[int]:
    """
    Calculates all primes between 2 and round(sqrt(max_number)) and returns
    them squared up.

    >>> get_primes_squared(2)
    []
    >>> get_primes_squared(4)
    [4]
    >>> get_primes_squared(10)
    [4, 9]
    >>> get_primes_squared(100)
    [4, 9, 25, 49]
    """
    max_prime = round(math.sqrt(max_number))
    non_primes = set()
    primes = []
    for num in range(2, max_prime + 1):
        if num in non_primes:
            continue

        counter = 2
        while num * counter <= max_prime:
            non_primes.add(num * counter)
            counter += 1

        primes.append(num ** 2)
    return primes


def get_squared_primes_to_use(
    num_to_look: int, squared_primes: List[int], previous_index: int
) -> int:
    """
    Returns an int indicating the last index on which squares of primes
    in primes are lower than num_to_look.

    This method supposes that squared_primes is sorted in ascending order and that
    each num_to_look is provided in ascending order as well. Under these
    assumptions, it needs a previous_index parameter that tells what was
    the index returned by the method for the previous num_to_look.

    If all the elements in squared_primes are greater than num_to_look, then the
    method returns -1.

    >>> get_squared_primes_to_use(1, [4, 9, 16, 25], 0)
    -1
    >>> get_squared_primes_to_use(4, [4, 9, 16, 25], 0)
    1
    >>> get_squared_primes_to_use(16, [4, 9, 16, 25], 1)
    3
    """
    idx = max(previous_index, 0)

    while idx < len(squared_primes) and squared_primes[idx] <= num_to_look:
        idx += 1

    if idx == 0 and squared_primes[idx] > num_to_look:
        return -1

    if idx == len(squared_primes) and squared_primes[-1] > num_to_look:
        return -1

    return idx


def get_squarefree(
    unique_coefficients: Set[int], squared_primes: List[int]
) -> Set[int]:
    """
    Calculates the squarefree numbers inside unique_coefficients given a
    list of square of primes.

    Based on the definition of a non-squarefree number, then any non-squarefree
    n can be decomposed as n = p*p*r, where p is positive prime number and r
    is a positive integer.

    Under the previous formula, any coefficient that is lower than p*p is
    squarefree as r cannot be negative. On the contrary, if any r exists such
    that n = p*p*r, then the number is non-squarefree.

    >>> get_squarefree({1}, [])
    set()
    >>> get_squarefree({1, 2}, [])
    set()
    >>> get_squarefree({1, 2, 3, 4, 5, 6, 7, 35, 10, 15, 20, 21}, [4, 9, 25])
    {1, 2, 3, 5, 6, 7, 35, 10, 15, 21}
    """

    if len(squared_primes) == 0:
        return set()

    non_squarefrees = set()
    prime_squared_idx = 0
    for num in sorted(unique_coefficients):
        prime_squared_idx = get_squared_primes_to_use(
            num, squared_primes, prime_squared_idx
        )
        if prime_squared_idx == -1:
            continue
        if any(num % prime == 0 for prime in squared_primes[:prime_squared_idx]):
            non_squarefrees.add(num)

    return unique_coefficients.difference(non_squarefrees)


def solution(n: int = 51) -> int:
    """
    Returns the sum of squarefrees for a given Pascal's Triangle of depth n.

    >>> solution(1)
    0
    >>> solution(8)
    105
    >>> solution(9)
    175
    """
    unique_coefficients = get_pascal_triangle_unique_coefficients(n)
    primes = get_primes_squared(max(unique_coefficients))
    squarefrees = get_squarefree(unique_coefficients, primes)
    return sum(squarefrees)


if __name__ == "__main__":
    print(f"{solution() = }")
