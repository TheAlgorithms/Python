"""
    Starting with 1 and spiralling anticlockwise in the following way, 
    a square spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along 
    the bottom right diagonal, but what is more interesting is 
    that 8 out of the 13 numbers lying along both 
    diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

    If one complete new layer is wrapped around the spiral 
    above, a square spiral with side length 9 will be formed. 
    If this process is continued, what is the side length of the square spiral for 
    which the ratio of primes along both diagonals first falls below 10%?

    problem link: https://projecteuler.net/problem=58
"""


def isPrime(n) -> bool:
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


"""
    Instead of calculation all numbers we are only calculating the sides of the square. 
    we find these numbers by adding to the last digit we had, 
    for example 9 the current side length
    minus 1. For example:

    Side length = 5, Last digit = 9
    9 + 4 = 13, 13 + 4 = 17, 17 + 4 = 21, 21 + 4 = 25.

    So the digits on the diagonal axis are (13,17,21,25)
    and we check those to see if they are prime numbers
"""


def calculateNextPrimes(lastDigit, sideLength) -> int:
    step = sideLength - 1
    currentDigit = lastDigit
    primes = 0
    for i in range(4):
        currentDigit = currentDigit + step
        if isPrime(currentDigit):
            primes += 1

    return primes


def solution() -> int:
    primes = 3
    nonprimes = 1
    currentDigit = 9
    side = 5

    while (primes / (primes + nonprimes)) * 100 > 10:
        currentPrimes = calculateNextPrimes(currentDigit, side)
        primes += currentPrimes
        nonprimes += 4 - currentPrimes
        currentDigit = currentDigit + 4 * (side - 1)

        side += 2

    return side - 2


if __name__ == "__main__":
    print(f"{solution() = }")
