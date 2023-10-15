"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock's price for all n days.

The span Si of the stock's price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of the stock
on the current day is less than or equal to its price on the given day.
"""


def calculation_span(price: list[float]):
    """
       Calculate the span values for a given list of stock prices.
       Args:
           price (list): List of stock prices.
       Returns:
       >>> price = [10, 4, 5, 90, 120, 80]
       >>> calculation_span(price)
       [1, 1, 2, 4, 5, 6]
       >>> price = [100, 50, 60, 70, 80, 90]
       >>> calculation_span(price)
       [1, 1, 2, 3, 4, 5]
       >>> price = [5, 4, 3, 2, 1]
       >>> calculation_span(price)
       [1, 1, 2, 3, 4]
       >>> price = [1, 2, 3, 4, 5]
       >>> calculation_span(price)
       [1, 2, 3, 4, 5]
       >>> price = [10, 20, 30, 40, 50]
       >>> calculation_span(price)
       [1, 2, 3, 4, 5]
        """
    n = len(price)
    st = [0]
    s = [0] * n
    s[0] = 1
    for i in range(1, n):
        while len(st) > 0 and price[st[0]] <= price[i]:
            st.pop()
        s[i] = i + 1 if len(st) <= 0 else (i - st[0])
    return s


price = [10, 4, 5, 90, 120, 80]
S = calculation_span(price)
print(S)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
