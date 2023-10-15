"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock's price for all n days.

The span Si of the stock's price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of the stock
on the current day is less than or equal to its price on the given day.
"""


def calculation_span(price, s):
    """
       Calculate the span values for a given list of stock prices.
       Args:
           price (list): List of stock prices.
           s (list): List to store the span values.
       Returns:
           None
       >>> price = [10, 4, 5, 90, 120, 80]
       >>> S = [0 for i in range(len(price) + 1)]
       >>> calculation_span(price, S)
       >>> S
       [1, 1, 2, 4, 5, 6, 0]
       >>> price = [100, 50, 60, 70, 80, 90]
       >>> S = [0 for i in range(len(price) + 1)]
       >>> calculation_span(price, S)
       >>> S
       [1, 1, 2, 3, 4, 5, 0]
       >>> price = [5, 4, 3, 2, 1]
       >>> S = [0 for i in range(len(price) + 1)]
       >>> calculation_span(price, S)
       >>> S
       [1, 1, 2, 3, 4, 0]
       >>> price = [1, 2, 3, 4, 5]
       >>> S = [0 for i in range(len(price) + 1)]
       >>> calculation_span(price, S)
       >>> S
       [1, 2, 3, 4, 5, 0]
       >>> price = [10, 20, 30, 40, 50]
       >>> S = [0 for i in range(len(price) + 1)]
       >>> calculation_span(price, S)
       >>> S
       [1, 2, 3, 4, 5, 0]
        """
    n = len(price)
    st = []
    st.append(0)
    s[0] = 1
    for i in range(1, n):
        while len(st) > 0 and price[st[0]] <= price[i]:
            st.pop()
        s[i] = i + 1 if len(st) <= 0 else (i - st[0])


def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price) + 1)]

calculation_span(price, S)

print_array(S, len(price))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
