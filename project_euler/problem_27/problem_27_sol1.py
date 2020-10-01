"""
Euler discovered the remarkable quadratic formula:
n2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 412 + 41 + 41 is clearly divisible by 41.
The incredible formula  n2 − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79 and
1601, is −126479.
Considering quadratics of the form:
n² + an + b, where |a| &lt; 1000 and |b| &lt; 1000
where |n| is the modulus/absolute value of ne.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.
"""

import math


def is_prime(k: int) -> bool:
    """
    Determine if a number is prime
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    if k < 2 or k % 2 == 0:
        return False
    elif k == 2:
        return True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2):
            if k % x == 0:
                return False
    return True


def solution(a_limit: int, b_limit: int) -> int:
    """
    >>> solution(1000, 1000)
    -59231
    >>> solution(200, 1000)
    -59231
    >>> solution(200, 200)
    -4925
    >>> solution(-1000, 1000)
    0
    >>> solution(-1000, -1000)
    0
    """
    longest = [0, 0, 0]  # length, a, b
    for a in range((a_limit * -1) + 1, a_limit):
        for b in range(2, b_limit):
            if is_prime(b):
                count = 0
                n = 0
                while is_prime((n ** 2) + (a * n) + b):
                    count += 1
                    n += 1
                if count > longest[0]:
                    longest = [count, a, b]
    ans = longest[1] * longest[2]
    return ans


if __name__ == "__main__":
    print(solution(1000, 1000))
