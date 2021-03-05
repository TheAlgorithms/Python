# Python program to show the usage of Fermat's little theorem in a division
# According to Fermat's little theorem, (a / b) mod p always equals
# a * (b ^ (p - 2)) mod p
# Here we assume that p is a prime number, b divides a, and p doesn't divide b
# Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem


def binary_exponentiation(a, n, mod):

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
