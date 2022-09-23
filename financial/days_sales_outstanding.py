"""
Days Sales Outstanding (DSO)
Days Sales Outstanding  =
    (Accounts Receivable / Total Credit Sales)
    *
    Number of Days
Investopedia Article: https://www.investopedia.com/terms/d/dso.asp

DSO is the average number of days that receivables remain outstanding.
Usually viewed in context over a period of time.
For example, tracking DSO month over month.
"""


def days_sales_outstanding(
    accounts_receivable: float, total_credit_sales: float, number_of_days: int
) -> float:
    """
    Formula to calculate Days Sales Outstanding:
    Days Sales Outstanding  =
        (Accounts Receivable / Total Credit Sales)
        *
        Number of Days
    Accounts Receivable = Outstanding invoices
    Total Credit Sales = Total sales made on credit
    Number of Days = The number of days comparing
    >>> days_sales_outstanding(200000,1200000,365)
    60.83333333333333
    >>> days_sales_outstanding(90000,100578,90)
    80.53451052914156
    >>> days_sales_outstanding(200000,1200000,-5)
    Traceback (most recent call last):
        ...
    ValueError: -5 must be greater than 0
    """
    if number_of_days <= 0:
        raise ValueError(f"{number_of_days} must be greater than 0")
    return (accounts_receivable / total_credit_sales) * number_of_days


if __name__ == "__main__":
    import doctest

    doctest.testmod()
