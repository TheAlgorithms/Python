'''
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

'''

import doctest

def calculate_future_value(present_value : float, inflation_rate : float , years : int) -> float:
    """
    Calculate the future value of money considering inflation.

    Args:
        present_value (float): The present value of money.
        inflation_rate (float): The annual inflation rate as a percentage.
        years (int): The number of years into the future.

    Returns:
        float: The future value of money adjusted for inflation.

    Formula:
    Future Value = Present Value * (1 + Inflation Rate/100)^Years

    >>> calculate_future_value(1000, 2, 5)
    1104.0808032
    >>> calculate_future_value(5000, 3.5, 10)
    7052.993803105605
    >>> calculate_future_value(10000, 1.5, 20)
    13468.550065500534
    """

    future_value = present_value * (1 + inflation_rate/100)**years
    return future_value

def main() -> None:
    print("Inflation Calculator")
    print("="*20)
    present_value = float(input("Enter the present value of money: $"))
    inflation_rate = float(input("Enter the annual inflation rate (as a percentage): "))
    years = int(input("Enter the number of years: "))

    future_value = calculate_future_value(present_value, inflation_rate, years)

    print(f"The future value of ${present_value:f} after {years} years, with an annual \
inflation rate of {inflation_rate}%, will be ${future_value:f}")

if __name__ == "__main__":
    doctest.testmod()