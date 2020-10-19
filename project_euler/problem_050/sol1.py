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


def binary_search(arr, left, right, element):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return binary_search(arr, left, mid - 1, element)
        else:
            return binary_search(arr, mid + 1, right, element)
    else:
        return -1


def sieve(limit):
    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(limit ** 0.5 + 1), 2):
        index = i * 2
        while index < limit:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, limit, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def solution(limit: int = 1000000) -> int:
    primes = sieve(limit)

    length = 0

    largest = 0

    lastj = primes_size = len(primes)

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
    return largest


if __name__ == "__main__":
    print(f"{solution()}")
