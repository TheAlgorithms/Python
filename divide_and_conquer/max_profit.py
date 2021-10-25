"""
Given a list representing the price of a stock each day,
figure out the max profit you could have made for the alloted time.
For example, a stock opens at the following values for each day:

[100, 105, 97, 200, 150]

So, your max profit would be $103, as you bought on the 3rd day at $97 and sold the next day at $200.
This is a divide and conquer algorithim that can find a solution in O(nlogn) time.
"""

def price_to_profit(lst):
    """
    Given a list of stock prices like the one above,
    return a list of of the change in value each day.
    The list of the profit returned from this function will be our input in max_profit.

    >>> price_to_profit([100, 105, 97, 200, 150])
    [0, 5, -8, 103, -50]
    >>> price_to_profit([205, 199, 188, 220, 235, 280, 301])
    [0, -6, -11, 32, 15, 45, 21]
    """
    profit = [lst[i+1] - lst[i] for i in range(len(lst) - 1)]
    profit.insert(0, 0)
    return profit

def max_profit(lst: list[int], left: int = 0, right: int = None): # O(nLogn)
    """
    Given a list of the change in price of a stock (Taken from price_to_profit())
    Return our max profit if:
    - Can only buy and sell once each.
    - Sell must be after the buy.

    >>> max_profit([0, 5, -8, 103, -50])
    103
    >>> max_profit([0, -1, 3, 4, -5, 9, -2])
    11
    >>> max_profit([0, 6, 3, 2, 1])
    12
    """
    # Check if a value for the right point of the list is provided, if not set it as our right-most index.
    if right == None:
        right = len(lst) - 1

    # Our base case: If our list is one value, return that profit value.
    if right == left:
        return lst[0]

    # Find the middle of the list to divide at:
    mid = (left + right) // 2

    # Divide and Conquer:
    max_profit_left = max_profit(lst, left, mid) # find max profit in the left-hand sublist
    max_profit_right = max_profit(lst, mid+1, right) # find the max profit in right-hand sublist
    max_profit_crossing = _max_profit_crossing(lst, left, right, mid) # find the max profit that crosses form the left to right (requires a helper function)

    # Combine: Return our best profit out of the profits we have gathered from our sublists and center point
    if max_profit_left >= max_profit_right and max_profit_left >= max_profit_crossing:
        return max_profit_left
    elif max_profit_right >= max_profit_left and max_profit_right >= max_profit_crossing:
        return max_profit_right
    else:
        return max_profit_crossing

def _max_profit_crossing(lst: list[int], left: int, right: int, mid: int): # O(n)
    """
    Our helper function to max_profit().
    Requires O(n) time and space as it iterates through our left and right sublists to find the best price.
    """
    left_sum = 0
    total = 0
    # Starting from the middle, find the best price moving left.
    for i in range(mid, left - 1, -1):
        total += lst[i]
        if total > left_sum:
            left_sum = total

    right_sum = 0
    total = 0
    # Starting from just after the middle, find the best price as we iterate to the right.
    for j in range(mid+1, right+1):
        total += lst[j]
        if total > right_sum:
            right_sum = total
    
    # Return the sum of our best prices in either sublist:
    return left_sum + right_sum

if __name__ == "__main__":
    import doctest

    doctest.testmod()
