# ---------------------------------------------------------------
# Title: Stock Buy and Sell - Max One Transaction Allowed
#
# Problem:
# Given an array prices[] representing the price of a stock on each day,
# find the maximum profit achievable by performing at most one transaction.
# (You must buy before you sell.)
#
# Example:
# Input: prices = [7, 10, 1, 3, 6, 9, 2]
# Output: 8   (Buy at 1, Sell at 9)
#
# Approach:
# We traverse the list once, keeping track of:
#   - min_price_so_far: The lowest price encountered so far.
#   - max_profit: The maximum profit seen so far.
#
# For each price:
#   - Compute potential profit = current_price - min_price_so_far.
#   - Update max_profit if this profit is greater than the previous.
#   - Update min_price_so_far if a smaller price is found.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------------

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculate the maximum profit from at most one buy-sell transaction.

    Parameters:
        prices (List[int]): List of stock prices per day.

    Returns:
        int: Maximum profit possible. Returns 0 if no profit is possible.

    Doctests:
    >>> max_profit([7, 10, 1, 3, 6, 9, 2])
    8
    >>> max_profit([7, 6, 4, 3, 1])
    0
    >>> max_profit([1, 3, 6, 9, 11])
    10
    """
    if not prices or len(prices) < 2:
        return 0

    min_price_so_far = prices[0]
    max_profit_val = 0

    for price in prices[1:]:
        min_price_so_far = min(min_price_so_far, price)
        max_profit_val = max(max_profit_val, price - min_price_so_far)

    return max_profit_val



# ---------------------------------------------------------------
# Example Usage (For quick testing)
# ---------------------------------------------------------------
if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print("Stock Prices:", prices)
    print("Maximum Profit:", max_profit(prices))  # Expected Output: 8
