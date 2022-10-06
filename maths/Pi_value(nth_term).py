from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 1000
# max possible digits = 1000



def pi_d(n_d) -> float:

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

if __name__ == "__main__":
    num = int(input("\nEnter the num of digits (0-999): "))
    if num < 1000:
        final_result = pi_d(num)
        print(f"Values of pi to the {num} decimal places is :\n\n   {final_result}\n")
    else:
        print("Enter a value between 0 - 999")
