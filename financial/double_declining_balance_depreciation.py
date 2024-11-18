"""
In accounting, depreciation refers to the decreases in the value
of a fixed asset during the asset's useful life.
When an organization purchases a fixed asset,
the purchase expenditure is not recognized as an expense immediately.
Instead, the decreases in the asset's value are recognized as expenses
over the years during which the asset is used.

The following methods are widely used
for depreciation calculation in accounting:
- Straight-line method
- Diminishing balance method
- Units-of-production method

The diminishing balance method, which is also called declining balance method,
calculates the depreciation expense by multiplying the asset's book value by
depreciation rate. The diminishing balance method is used when it is needed
to recognize larger declines in the asset value during earlier years
of the useful life.

Double-declining balance method is the widely used diminishing balance method.
This method uses a depreciation rate which is twice larger than the rate
used in straight-line method. The depreciation process stops when
the book value of the asset becomes lower than its residual value
or when the asset's useful life ends.

The following formula shows how to calculate the annual depreciation expense:
- annual depreciation expense =
    book value of asset * depreciation rate =
    (purchase cost of asset - accumulated depreciation expenses) * depreciation rate


Further information on:
https://en.wikipedia.org/wiki/Depreciation
https://www.investopedia.com/terms/d/double-declining-balance-depreciation-method.asp

The function, double_declining_depreciation, returns a list of
the depreciation expenses over the given period
when double-declining-method is applied.

For the practical application, double_declining_depreciation function will
allow values with less than 3 decimal places for purchase value and residual
value arguments.
"""


def double_declining_depreciation(
    useful_years: int, purchase_value: float, residual_value: float = 0.0
) -> list[float]:
    """
    Calculate the depreciation expenses over the given period
    :param useful_years: Number of years the asset will be used
    :param purchase_value: Purchase expenditure for the asset
    :param residual_value: Residual value of the asset at the end of its useful life
    :return: A list of annual depreciation expenses over the asset's useful life

    Examples:
    >>> double_declining_depreciation(1, 500.0)
    [500.0]
    >>> double_declining_depreciation(1, 500.0, 100.0)
    [400.0]
    >>> double_declining_depreciation(3, 1000.0, 100.0)
    [666.67, 222.22, 11.11]
    >>> double_declining_depreciation(5, 1000.0, 100.0)
    [400.0, 240.0, 144.0, 86.4, 29.6]
    >>> double_declining_depreciation(8, 2000.0)
    [500.0, 375.0, 281.25, 210.94, 158.2, 118.65, 88.99, 266.97]
    >>> double_declining_depreciation(10, 1000.0, 100.0)
    [200.0, 160.0, 128.0, 102.4, 81.92, 65.54, 52.43, 41.94, 33.55, 34.22]

    """

    if not isinstance(useful_years, int):
        raise TypeError("Useful years must be an integer")

    if useful_years < 1:
        raise ValueError("Useful years cannot be less than 1")

    if not isinstance(purchase_value, (float, int)):
        raise TypeError("Purchase value must be numeric")

    if "." in (purchase_value_str := str(purchase_value)):
        purchase_value_str_split = purchase_value_str.split(".")
        decimal_places = purchase_value_str_split[1]
        if len(decimal_places) > 2:
            raise ValueError("Purchase value must not exceed two decimal places")

    if purchase_value < 0.0:
        raise ValueError("Purchase value cannot be less than zero")

    if not isinstance(residual_value, (float, int)):
        raise TypeError("Residual value must be numeric")

    if "." in (residual_value_str := str(residual_value)):
        residual_value_str_split = residual_value_str.split(".")
        decimal_places = residual_value_str_split[1]
        if len(decimal_places) > 2:
            raise ValueError("Residual value must not exceed two decimal places")

    if purchase_value < residual_value:
        raise ValueError("Purchase value cannot be less than residual value")

    # Calculate depreciation rate
    straight_line_depreciation_rate = 1 / useful_years
    double_declining_depreciation_rate = straight_line_depreciation_rate * 2

    book_value = purchase_value

    # List of annual depreciation expenses
    list_of_depreciation_expenses = []
    for period in range(useful_years):
        depreciation_expense_by_rate = round(
            book_value * double_declining_depreciation_rate, 2
        )

        if (
            period == useful_years - 1
            or residual_value > book_value - depreciation_expense_by_rate
        ):
            depreciation_expense = round(book_value - residual_value, 2)
            list_of_depreciation_expenses.append(depreciation_expense)
        else:
            depreciation_expense = depreciation_expense_by_rate
            book_value -= depreciation_expense
            list_of_depreciation_expenses.append(depreciation_expense)

    return list_of_depreciation_expenses


if __name__ == "__main__":
    user_input_useful_years = int(input("Please Enter Useful Years:\n > "))
    user_input_purchase_value = float(input("Please Enter Purchase Value:\n > "))
    user_input_residual_value = float(input("Please Enter Residual Value:\n > "))
    print(
        double_declining_depreciation(
            user_input_useful_years,
            user_input_purchase_value,
            user_input_residual_value,
        )
    )
