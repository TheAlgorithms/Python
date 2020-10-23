import random

from .binary_exp_mod import bin_exp_mod


# This is a probabilistic check to test primality, useful for big numbers!
# if it's a prime, it will return true
# if it's not a prime, the chance of it returning true is at most 1/4**prec
def is_prime(n, prec=1000):
    """
    >>> from .prime_check import prime_check
    >>> all(is_prime(i) == prime_check(i) for i in range(1000))
    True
    """
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    # this means n is odd
    d = n - 1
    exp = 0
    while d % 2 == 0:
        d /= 2
        exp += 1

    # n - 1=d*(2**exp)
    count = 0
    while count < prec:
        a = random.randint(2, n - 1)
        b = bin_exp_mod(a, d, n)
        if b != 1:
            flag = True
            for i in range(exp):
                if b == n - 1:
                    flag = False
                    break
                b = b * b
                b %= n
            if flag:
                return False
            count += 1
    return True


if __name__ == "__main__":
    n = abs(int(input("Enter bound : ").strip()))
    print("Here's the list of primes:")
    print(", ".join(str(i) for i in range(n + 1) if is_prime(i)))
