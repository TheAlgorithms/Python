"""
By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13
We can see that the 6th prime is 13. What is the Nth prime number?
"""


def is_prime(num, arr):
    for i in arr:
        if num % i == 0:
            return False
    return True


def solution(n):
    """Returns the n-th prime number.
    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(50)
    229
    >>> solution(100)
    541
    """
    x = 3
    primes = [2]
    while True:
        if is_prime(x, primes):
            primes.append(x)
        if len(primes) >= n:
            return primes[n - 1]
        x += 2


if __name__ == "__main__":
    print(solution(int(input().strip())))
