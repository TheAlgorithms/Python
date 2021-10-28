# Primality Testing with the Rabin-Miller Algorithm

import random

from maths.prime_check import prime_check


def rabinMiller(num: int) -> bool:
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def generateLargePrime(keysize: int = 1024) -> int:
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if prime_check(num):
            return num


if __name__ == "__main__":
    num = generateLargePrime()
    print(("Prime number:", num))
    print(("isPrime:", prime_check(num)))
