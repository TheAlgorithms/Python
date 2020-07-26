"""
        == Finding Exponent using Recursion ==
        i/p -->
        Enter the base: 3
        Enter the exponent: 4
        o/p -->
        3 to the power of 4: 81
        i/p -->
        Enter the base: 2
        Enter the exponent: 0
        o/p -->
        2 to the power of 0: 1
"""


def power(n: int, p: int) -> int:
    if p == 0:
        return 1
    else:
        return n * power(n, (p - 1))


if __name__ == "__main__":
    n = int(input("Enter the base: "))
    p = int(input("Enter the exponent: "))

    result = power(n, abs(p))
    if p < 0:
        newResult = 1 / result
        print("{} to the power of {}: {}".format(n, p, newResult))
    else:
        print("{} to the power of {}: {}".format(n, p, result))
