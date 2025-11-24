"""
An ordinary annuity means making or requiring payments at the end
of each term during a given period.
For example, if the given period is 3 terms long and the payment
for each term is $1000, then the cash flow is as follows:

    0: no payment --- 1: $1000 --- 2: $1000 --- 3: $1000

The function, get_ordinary_annuity_future_value, calculates the future value of
the given ordinary annuity. In the example above, the function should return
the sum of each payment's future value at the end of term 3,
which means the sum is returned as soon as the last payment is made.

More info on: https://www.investopedia.com/retirement/calculating-present-and-future-value-of-annuities

This function can help to understand how much you will receive
if you make a regular deposit at the end of each term
for saving with a fix period and interest rate.
"""


def get_ordinary_annuity_future_value(
    term_payment: float, number_of_payments: int, term_interest_rate: float
) -> float:
    """
    Calculate the future value of the given ordinary annuity
    :param term_payment: payment made at the end of each term
    :param number_of_payments: the number of payments
    :param term_interest_rate: the interest rate for each term
    :return: the future value (maturity value) of the given ordinary annuity

    Examples:
    >>> round(get_ordinary_annuity_future_value(500, 10, 0.05), 2)
    6288.95
    >>> round(get_ordinary_annuity_future_value(1000, 10, 0.05), 2)
    12577.89
    >>> round(get_ordinary_annuity_future_value(1000, 10, 0.10), 2)
    15937.42
    >>> round(get_ordinary_annuity_future_value(1000, 20, 0.10), 2)
    57275.0
    """

    annuity_factor = (
        ((1 + term_interest_rate) ** number_of_payments) - 1
    ) / term_interest_rate
    future_value = term_payment * annuity_factor
    return future_value


if __name__ == "__main__":
    user_input_amount = float(input("How much money will be deposited each term?\n> "))
    user_input_payment_number = int(input("How many payments will be made?\n> "))
    term_interest_rate = float(input("What is the interest rate per term?\n> "))
    print(
        get_ordinary_annuity_future_value(
            user_input_amount, user_input_payment_number, term_interest_rate
        )
    )
