"""
Given a list of stock prices calculate the maximum profit that can be made from a
single buy and sell of one share of stock.  We only allowed to complete one buy
transaction and one sell transaction but must buy before we sell.

Example : prices = [7, 1, 5, 3, 6, 4]
max_profit will return 5 - which is by buying at price 1 and selling at price 6.

This problem can be solved using the concept of "GREEDY ALGORITHM".

We iterate over the price array once, keeping track of the lowest price point
(buy) and the maximum profit we can get at each point.  The greedy choice at each point
is to either buy at the current price if it's less than our current buying price, or
sell at the current price if the profit is more than our current maximum profit.
"""


def max_profit(prices: list[int]) -> int:
    """
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit: int = 0

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)

    return max_profit


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(max_profit([7, 1, 5, 3, 6, 4]))
