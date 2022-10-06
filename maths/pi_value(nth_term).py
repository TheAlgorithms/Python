from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 1000
# max possible digits = 1000


def pi_d(n_d: int) -> Decimal:
    """
    Calculate the value of pi till n-digits before decimal
    >>> pi_d(0)
    None
    >>> pi_d(10)
    3.1415926536
    >>> pi_d(30)
    3.141592653589734311542867450467
    >>> pi_d(3000)
    Traceback (most recent call last):
    ...
    decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]
    """
    numerator = Decimal(0)
    denominator = Decimal(0)
    result = Decimal(0)

    for k in range(n_d):

        numerator = ((-1) ** k) * (factorial(6 * k)) * (13591409 + 54510134 * k)

        denominator = factorial(3 * k) * ((factorial(k)) ** 3) * (640320 ** (3 * k))

        result += Decimal(numerator) / Decimal(denominator)
        result *= 12 / Decimal(640320**1.5)
        result = result**-1

        return round(result, n_d)
    return result


if __name__ == "__main__":
    num = int(input("\nEnter the num of digits (0-999): "))
    final_result = pi_d(num)
    print(f"Values of pi to the {num} decimal places is :\n\n   {final_result}\n")
