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


def power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    else:
        return base * power(base, (exponent - 1))


if __name__ == "__main__":
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))

    result = power(base, abs(exponent))
    if exponent < 0:
        newResult = 1 / result
        print("{} to the power of {}: {}".format(base, exponent, newResult))
    else:
        print("{} to the power of {}: {}".format(base, exponent, result))
