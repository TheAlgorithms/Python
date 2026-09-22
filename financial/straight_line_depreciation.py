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
    Calculate the depreciation expenses over the given period
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


if __name__ == "__main__":
    user_input_useful_years = int(input("Please Enter Useful Years:\n > "))
    user_input_purchase_value = float(input("Please Enter Purchase Value:\n > "))
    user_input_residual_value = float(input("Please Enter Residual Value:\n > "))
    print(
        straight_line_depreciation(
            user_input_useful_years,
            user_input_purchase_value,
            user_input_residual_value,
        )
    )
