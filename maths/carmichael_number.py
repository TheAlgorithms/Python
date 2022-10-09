"""
== Carmichael Numbers ==
A number n is said to be a Carmichael number if it satisfies the following modular arithmetic condition:

    power(b, n-1) MOD n = 1,
    for all b ranging from 1 to n such that b and
    n are relatively prime, i.e, gcd(b, n) = 1

Examples of Carmichael Numbers: 561, 1105, ...
https://en.wikipedia.org/wiki/Carmichael_number
"""


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def power(x, y, mod):
    if y == 0:
        return 1
    temp = power(x, y // 2, mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


def isCarmichaelNumber(n):
    b = 2
    while b < n:

        if gcd(b, n) == 1:

            if power(b, n - 1, n) != 1:
                return False
        b = b + 1
    return True


if __name__ == "__main__":
    print("Program to check whether a number is a Carmichael Numbers or not...")
    number = int(input("Enter number: ").strip())
    print(
        f"{number} is {'' if isCarmichaelNumber(number) else 'not '}a Carmichael Number."
    )
