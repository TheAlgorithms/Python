"""
Project Euler 60
https://projecteuler.net/problem=60



The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the
result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a
set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

"""

from math import sqrt

pairs: list[str] = []
minimum_sum = 0
primes: list[int] = []


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).
    A number is prime if it has exactly two factors: 1 and itself.

    Taken from /maths/prime_check.py

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(87)
    False
    >>> is_prime(563)
    True
    >>> is_prime(2999)
    True
    >>> is_prime(67483)
    False
    """

    # precondition
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must been an int and positive"

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
        return False

    # All primes number are in format of 6k +/- 1
    for i in range(5, int(sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def combiner(i, length):
    """
    This function goes through all the combinations of the primes list in
    ascending order, and finds pairs that satisfy the question until the
    minimum_sum is low enough that it can stop and the minimum_sum is the minimum.
    """

    global pairs, minimum_sum
    j = i  # local variable j retains the original index

    if len(pairs) == length:  # if it is one of the pairs we want
        s = sum(int(x) for x in pairs)
        if s < minimum_sum:
            minimum_sum = s
        primes.insert(i, pairs.pop(-1))
        return True

    while i < len(primes):
        for prime in pairs:
            if not is_prime(int(prime + primes[i])):
                break
            if not is_prime(int(primes[i] + prime)):
                break
        else:
            pairs.append(primes.pop(i))
            if not combiner(i, length):
                return False

        if pairs:
            i += 1

    if primes:
        if j + len(pairs) - 1 != 0:
            primes.insert(j, pairs.pop(-1))
            return True
        else:
            if int(pairs.pop(-1)) > minimum_sum / (
                2 * 10 ** (length - 2)
            ):  # works for most test cases
                return False
            return True


def solution(n=5, limit=10000):
    """
    The function returns the lowest sum for a set of n primes (n > 1) for which
    any two primes concatenate to produce another prime.

    Limit is the maximum number of natural numbers to be checked up to.


    >>> solution(2,10)
    10
    >>> solution(3,100)
    107
    >>> solution(4,1000)
    792
    """

    global minimum_sum, primes, pairs
    primes = []
    pairs = []
    for i in range(1, limit + 1):
        if is_prime(i):
            primes.append(str(i))
    minimum_sum = limit * 5
    combiner(0, n)
    return minimum_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{solution() = }")
