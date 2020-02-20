# This theorem states that the number of prime factors of n
# will be approximately log(log(n)) for most natural numbers n

import math


def exactPrimeFactorCount(n):
    """
    >>> exactPrimeFactorCount(51242183)
    3
    """
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n = int(n / 2)
    # the n input value must be odd so that
    # we can skip one element (ie i += 2)

    i = 3

    while i <= int(math.sqrt(n)):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n = int(n / i)
        i = i + 2

    # this condition checks the prime
    # number n is greater than 2

    if n > 2:
        count += 1
    return count


if __name__ == "__main__":
    n = 51242183
    print(f"The number of distinct prime factors is/are {exactPrimeFactorCount(n)}")
    print("The value of log(log(n)) is {:.4f}".format(math.log(math.log(n))))

    """
    The number of distinct prime factors is/are 3
    The value of log(log(n)) is 2.8765
    """
