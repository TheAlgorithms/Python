"""
Author Suvan Banerjee (@suvanbanerjee)
Date: 2023-02-10
Description: This program calculates the future value of money based on the present
value, inflation rate, and number of years.

--------------------------------------------
In economics, inflation is a general increase of the prices. This is usually measured
using the consumer price index (CPI).When the general price level rises, each unit of
 currency buys fewer goods and services; consequently, inflation corresponds
to a reduction in the purchasing power of money.

Source: https://en.wikipedia.org/wiki/Inflation

"""

import doctest


def calculate_future_value(
    present_value: float, inflation_rate: float, years: int
) -> float:
    """Calculates the future value of money"""
    future_value = present_value * (1 + inflation_rate / 100) ** years
    return future_value


def main():
    print("Inflation Calculator")
    print("=" * 20)
    present_value = float(input("Enter the present value of money: $"))
    inflation_rate = float(input("Enter the annual inflation rate (as a percentage): "))
    years = int(input("Enter the number of years: "))

    future_value = calculate_future_value(present_value, inflation_rate, years)

    print(
        f"The future value of ${present_value:.2f} after {years} years, with an annual inflation rate of {inflation_rate}%, will be ${future_value:.2f}"
    )


if __name__ == "__main__":
    doctest.testmod()
    main()
