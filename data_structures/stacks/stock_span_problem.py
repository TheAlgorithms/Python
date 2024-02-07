"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock's price for all n days.

The span Si of the stock's price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of the stock
on the current day is less than or equal to its price on the given day.
"""


def calculation_span(price: list[float]) -> list[float]:
    """
    Calculate the span values for a given list of stock prices.
    Args:
        price (list): List of stock prices.
    Returns:
    >>> price = [10, 4, 5, 90, 120, 80]
    >>> calculation_span(price)
    [1.0, 1.0, 2.0, 4.0, 5.0, 1.0]
    >>> price = [100, 50, 60, 70, 80, 90]
    >>> calculation_span(price)
    [1.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    >>> price = [5, 4, 3, 2, 1]
    >>> calculation_span(price)
    [1.0, 1.0, 1.0, 1.0, 1.0]
    >>> price = [1, 2, 3, 4, 5]
    >>> calculation_span(price)
    [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> price = [10, 20, 30, 40, 50]
    >>> calculation_span(price)
    [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> calculation_span(price=[100, 80, 60, 70, 60, 75, 85])
    [1.0, 1.0, 1.0, 2.0, 1.0, 4.0, 6.0]
    """
    n = len(price)
    st = [0]
    s = [1.0]
    for i in range(1, n):
        while st and price[st[-1]] <= price[i]:
            st.pop()
        s.append(float(i - st[-1] if st else i + 1))
        st.append(i)
    return s


price = [10.0, 4.0, 5.0, 90.0, 120.0, 80.0]
S = calculation_span(price)
print(S)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
