# Python program to show the usage of Fermat's little theorem in a division
# According to Fermat's little theorem, (a / b) mod p always equals
# a * (b ^ (p - 2)) mod p
# Here we assume that p is a prime number, b divides a, and p doesn't divide b
# Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem


def binary_exponentiation(a: int, n: float, mod: int) -> int:
    """
    Compute (a^n) % mod using binary exponentiation.

    Args:
        a: Base number
        n: Exponent
        mod: Modulus

    Returns:
        Result of (a^n) % mod

    >>> binary_exponentiation(2, 10, 1000)
    24
    >>> binary_exponentiation(5, 3, 13)
    8
    >>> binary_exponentiation(10, 0, 7)
    1
    >>> binary_exponentiation(3, 4, 5)
    1
    """
    if n == 0:
        return 1

    elif n % 2 == 1:
        return (binary_exponentiation(a, n - 1, mod) * a) % mod

    else:
        b = binary_exponentiation(a, n / 2, mod)
        return (b * b) % mod


# a prime number
p = 701

a = 1000000000
b = 10

# using binary exponentiation function, O(log(p)):
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p)

# using Python operators:
print((a / b) % p == (a * b ** (p - 2)) % p)
