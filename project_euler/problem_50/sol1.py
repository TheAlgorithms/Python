"""
Consecutive prime sum
Problem 50: https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below 1 million, can be written as the sum of the most consecutive primes?
"""


def solution(n: int = 10 ** 6) -> int:
    """
    Returns solution to problem.

    Algorithm:
    1. Construct a "Sieve of Eratosthenes" to get all primes till n
    (This will also serve as O(1) primality check later)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode

    2. Now make the largest size window and slide over primes,
    until we encounter the sum of slide being a prime.

    >>> solution(100)
    41

    >>> solution(1000)
    953
    """

    if n < 1:
        raise ValueError("Please enter an integer greater than 0")

    sieve = [True] * n
    primes = []
    # Creation of Sieve
    for number in range(2, n):
        if sieve[number]:
            primes.append(number)
            for multiple in range(number * number, n, number):
                sieve[multiple] = False

    # Cumulative sum of primes for efficiency when calculating sum over window
    cumulative_sum = [2]
    for i in range(1, len(primes)):
        cumulative_sum.append(cumulative_sum[i - 1] + primes[i])

    # Find size of largest window with smallest primes adding to more than million
    largest_size = 0
    while cumulative_sum[largest_size] < n:
        largest_size += 1

    for size in range(largest_size, 1, -1):
        for start in range(0, len(primes) - size + 1):
            # Sum over window of size 'size' from index 'start'
            prime_sum = (
                cumulative_sum[start + size - 1] - cumulative_sum[start] + primes[start]
            )

            if prime_sum < n and sieve[prime_sum]:
                return prime_sum


if __name__ == "__main__":
    print(solution())
