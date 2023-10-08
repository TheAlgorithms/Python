"""
Given a list of coin denominations and an amount,
this program calculates the minimum number of coins needed to make up that amount.

Example :
coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000],
amount = 121, 
The minimum number of coins would be 3 (100 + 20 + 1).

This problem can be solved using the concept of "GREEDY ALGORITHM".

We start with the largest denomination of coins and use as many of those,
as possible before moving to the next largest denomination.
This process continues until the entire amount has been made up of coins.
"""

def min_coins(coins : list[int], amount : int = 0) -> tuple:
    """
    >>> min_coins([1, 2, 5, 10, 20, 50, 100, 500, 2000],121)
    (3, [100, 20, 1])
    >>> min_coins([1, 2, 5, 10, 20, 50, 100],343)
    (7, [100, 100, 100, 20, 20, 2, 1])
    >>> min_coins([1,2,5,10],0)
    (0, [])
    """
    coins.sort(reverse=True)
    count : int = 0
    coins_list : list[int] = []
    for coin in coins:
        if coin <= amount:
            while coin <= amount:
                count += 1
                coins_list.append(coin)
                amount -= coin

    return count, coins_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    print(f"{min_coins([1, 2, 5, 10, 20, 50, 100, 500, 2000],121)}")
    
