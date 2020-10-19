"""
https://projecteuler.net/problem=50
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive
primes?
"""
import time


def binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, right, x)
    else:
        return -1


# prime numbers upto 1 million
def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def solution(limit: int = 1000000) -> int:
    start = time.time()

    primes = sieve(limit)

    length = 0

    largest = 0

    # max value of the j variable(second for loop)
    lastj = primes_size = len(primes)

    # two for loops using binSearch to optimize
    for i in range(lastj):
        for j in range(i + length, lastj):
            sol = sum(primes[i:j])
            if sol < limit:
                if binary_search(primes, 0, primes_size - 1, sol) != -1:
                    length = j - i
                    largest = sol
            else:
                lastj = j + 1
                break
    end = time.time()

    return largest


if __name__ == "__main__":
    print(f"{solution() = }")
