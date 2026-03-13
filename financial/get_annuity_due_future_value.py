"""
An annuity due means making or requiring payments at the beginning
of each term during a given period.
For example, if the given period consists of 3 terms and the payment
for each term is $1000, then the cash flow is as follows:

    0: $1000 --- 1: $1000 --- 2: $1000 --- 3: no payment

The following function, get_annuity_due_future_value, gives the future value of
the given annuity due. In the example above, the function should return
the sum of each payment's future value at the end of term 3.

More info on: https://www.investopedia.com/retirement/calculating-present-and-future-value-of-annuities

This function can help to understand how much you will receive
if you make a regular deposit at the beginning of each term
for saving with a fix period and interest rate.
"""


def get_annuity_due_future_value(
    term_payment: float, number_of_payments: int, term_interest_rate: float
) -> float:
    """
    Calculate the future value of the given annuity due
    :param term_payment: payment made at the beginning of each term
    :param number_of_payments: the number of payments
    :param term_interest_rate: the interest rate for each term
    :return: the future value (maturity value) of the given annuity due

    Examples:
    >>> round(get_annuity_due_future_value(500, 10, 0.05), 2)
    6603.39
    >>> round(get_annuity_due_future_value(1000, 10, 0.05), 2)
    13206.79
    >>> round(get_annuity_due_future_value(1000, 10, 0.10), 2)
    17531.17
    >>> round(get_annuity_due_future_value(1000, 20, 0.10), 2)
    63002.5
    """

    annuity_factor = (
        ((1 + term_interest_rate) ** number_of_payments) - 1
    ) / term_interest_rate
    future_value = term_payment * annuity_factor * (1 + term_interest_rate)
    return future_value


if __name__ == "__main__":
    user_input_amount = float(input("How much money will be deposited each term?\n> "))
    user_input_payment_number = int(input("How many payments will be made?\n> "))
    term_interest_rate = float(input("What is the interest rate per term?\n> "))
    print(
        get_annuity_due_future_value(
            user_input_amount, user_input_payment_number, term_interest_rate
        )
    )
