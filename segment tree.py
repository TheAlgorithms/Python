"""
Square root convergents
url: https://projecteuler.net/problem=57
"""


def square_root_convergents():
    """Returns the number of fractions
         where the numerator has more digits than the denominator.
    >>> square_root_convergents()
    153
    """
    n1 = 1
    n2 = 1
    result = 0
    for x in range(1, 1001):
        numerator = n1 + n2 * 2
        denominator = n1 + n2

        if len(str(numerator)) > len(str(denominator)):
            result += 1

        n1 = numerator
        n2 = denominator

    return result


if __name__ == "__main__":
    print(square_root_convergents())
