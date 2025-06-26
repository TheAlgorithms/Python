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

The straight-line method is the simplest and most widely used.
This method calculates depreciation by spreading the cost evenly
over the asset's useful life.

The following formula shows how to calculate the yearly depreciation expense:

- annual depreciation expense =
    (purchase cost of asset - residual value) / useful life of asset(years)

Further information on:
https://en.wikipedia.org/wiki/Depreciation

The function, straight_line_depreciation, returns a list of
the depreciation expenses over the given period.
"""


def straight_line_depreciation(
    useful_years: int,
    purchase_value: float,
    residual_value: float = 0.0,
) -> list[float]:
    """
    Calculate the depreciation expenses over the given period,
     using the straight-line method
    :param useful_years: Number of years the asset will be used
    :param purchase_value: Purchase expenditure for the asset
    :param residual_value: Residual value of the asset at the end of its useful life
    :return: A list of annual depreciation expenses over the asset's useful life
    >>> straight_line_depreciation(10, 1100.0, 100.0)
    [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
    >>> straight_line_depreciation(6, 1250.0, 50.0)
    [200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
    >>> straight_line_depreciation(4, 1001.0)
    [250.25, 250.25, 250.25, 250.25]
    >>> straight_line_depreciation(11, 380.0, 50.0)
    [30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0]
    >>> straight_line_depreciation(1, 4985, 100)
    [4885.0]
    """

    if not isinstance(useful_years, int):
        raise TypeError("Useful years must be an integer")

    if useful_years < 1:
        raise ValueError("Useful years cannot be less than 1")

    if not isinstance(purchase_value, (float, int)):
        raise TypeError("Purchase value must be numeric")

    if not isinstance(residual_value, (float, int)):
        raise TypeError("Residual value must be numeric")

    if purchase_value < 0.0:
        raise ValueError("Purchase value cannot be less than zero")

    if purchase_value < residual_value:
        raise ValueError("Purchase value cannot be less than residual value")

    # Calculate annual depreciation expense
    depreciable_cost = purchase_value - residual_value
    annual_depreciation_expense = depreciable_cost / useful_years

    # List of annual depreciation expenses
    list_of_depreciation_expenses = []
    accumulated_depreciation_expense = 0.0
    for period in range(useful_years):
        if period != useful_years - 1:
            accumulated_depreciation_expense += annual_depreciation_expense
            list_of_depreciation_expenses.append(annual_depreciation_expense)
        else:
            depreciation_expense_in_end_year = (
                depreciable_cost - accumulated_depreciation_expense
            )
            list_of_depreciation_expenses.append(depreciation_expense_in_end_year)

    return list_of_depreciation_expenses


def declining_balance_depreciation(
    useful_years: int,
    purchase_value: float,
    residual_value: float = 0.0,
) -> list[float]:
    """
     Calculate the depreciation expenses over the given period,
      using the declining balance method
    :param useful_years: Number of years the asset will be used
    :param purchase_value: Purchase expenditure for the asset
    :param residual_value: Residual value of the asset at the end of its useful life
    :return: A list of annual depreciation expenses over the asset's useful life,
    rounded to the nearest cent

    >>> declining_balance_depreciation(10,1100.0,100.0)
    [234.53, 184.52, 145.18, 114.23, 89.87, 70.71, 55.64, 43.77, 34.44, 27.1]
    >>> declining_balance_depreciation(6,1250.0,50.0)
    [519.0, 303.51, 177.49, 103.8, 60.7, 35.5]
    >>> declining_balance_depreciation(4,1001.0)
    [1001.0, 0.0, 0.0, 0.0]
    >>> declining_balance_depreciation(11,380.0,50.0)
    [63.98, 53.21, 44.25, 36.8, 30.6, 25.45, 21.17, 17.6, 14.64, 12.17, 10.12]
    >>> declining_balance_depreciation(1,4985,100)
    [4885.0]
    """

    if not isinstance(useful_years, int):
        raise TypeError("Useful years must be an integer")

    if useful_years < 1:
        raise ValueError("Useful years cannot be less than 1")

    if not isinstance(purchase_value, (float, int)):
        raise TypeError("Purchase value must be numeric")

    if not isinstance(residual_value, (float, int)):
        raise TypeError("Residual value must be numeric")

    if purchase_value < 0.0:
        raise ValueError("Purchase value cannot be less than zero")

    if purchase_value < residual_value:
        raise ValueError("Purchase value cannot be less than residual value")

    depreciation_rate = 1 - ((residual_value / purchase_value) ** (1 / useful_years))
    book_value = purchase_value

    list_of_depreciation_expenses = []

    for _ in range(1, useful_years + 1):
        new_book_value = book_value * (1 - depreciation_rate)
        list_of_depreciation_expenses.append(round(book_value - new_book_value, 2))
        book_value = new_book_value

    return list_of_depreciation_expenses


def sum_of_years_digits_depreciation(
    useful_years: int,
    purchase_value: float,
    residual_value: float = 0.0,
) -> list[float]:
    """
     Calculate the depreciation expenses over the given period,
      using the sum of years' digits method
    :param useful_years: Number of years the asset will be used
    :param purchase_value: Purchase expenditure for the asset
    :param residual_value: Residual value of the asset at the end of its useful life
    :return: A list of annual depreciation expenses over the asset's useful life,
    rounded to the nearest cent

    >>> sum_of_years_digits_depreciation(10,1100.0,100.0)
    [181.82, 163.64, 145.45, 127.27, 109.09, 90.91, 72.73, 54.55, 36.36, 18.18]
    >>> sum_of_years_digits_depreciation(6,1250.0,50.0)
    [342.86, 285.71, 228.57, 171.43, 114.29, 57.14]
    >>> sum_of_years_digits_depreciation(4,1001.0)
    [400.4, 300.3, 200.2, 100.1]
    >>> sum_of_years_digits_depreciation(11,380.0,50.0)
    [55.0, 50.0, 45.0, 40.0, 35.0, 30.0, 25.0, 20.0, 15.0, 10.0, 5.0]
    >>> sum_of_years_digits_depreciation(1,4985,100)
    [4885.0]
    """

    if not isinstance(useful_years, int):
        raise TypeError("Useful years must be an integer")

    if useful_years < 1:
        raise ValueError("Useful years cannot be less than 1")

    if not isinstance(purchase_value, (float, int)):
        raise TypeError("Purchase value must be numeric")

    if not isinstance(residual_value, (float, int)):
        raise TypeError("Residual value must be numeric")

    if purchase_value < 0.0:
        raise ValueError("Purchase value cannot be less than zero")

    if purchase_value < residual_value:
        raise ValueError("Purchase value cannot be less than residual value")

    digits_sum = useful_years * (useful_years + 1) // 2

    list_of_depreciation_expenses = []

    for i in range(1, useful_years + 1):
        depreciation_value = (
            (useful_years - (i - 1)) / digits_sum * (purchase_value - residual_value)
        )
        list_of_depreciation_expenses.append(round(depreciation_value, 2))

    return list_of_depreciation_expenses


if __name__ == "__main__":
    import doctest

    doctest.testmod()
