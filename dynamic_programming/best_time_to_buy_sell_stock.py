#############################
# Author: yash kesharwani
# File: best_time_to_buy_sell_stock.py
# comments: This program output the
# best time to buy and sell stock with fees
#############################
# from typing import list


import unittest

# from typing import list


class Solution:
    def solve(
        self, prices: list[int], index: int, fee: int, buy: int, dp: list[list[int]]
    ) -> int:
        """
        Calculate the maximum profit with the given parameters.

        :param prices: list of prices for each day.
        :param index: Current day index.
        :param fee: Transaction fee.
        :param buy: Buy or sell flag (1 for buy, 0 for sell).
        :param dp: Memoization table.
        :return: Maximum profit achievable.
        """
        if index >= len(prices):
            return 0
        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0
        if buy == 1:
            profit = max(
                -prices[index] + self.solve(prices, index + 1, fee, 0, dp),
                self.solve(prices, index + 1, fee, 1, dp),
            )
        else:
            profit = max(
                (prices[index] + self.solve(prices, index + 1, fee, 1, dp)) - fee,
                self.solve(prices, index + 1, fee, 0, dp),
            )

        dp[index][buy] = profit
        return profit

    def maxprofit(self, prices: list[int], fee: int) -> int:
        """
        Calculate the maximum profit achievable when buying
        and selling stocks with a fee.
        :param prices: list of stock prices for each day.
        :param fee: Transaction fee.
        :return: Maximum profit achievable.
        Example:
        >>> s = Solution()
        >>> s.maxprofit([1, 3, 2, 8, 4, 9], 2)
        8
        >>> s.maxprofit([1, 4, 3, 6, 8, 2, 7], 3)
        6
        """
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        return self.solve(prices, 0, fee, 1, dp)


class TestSolution(unittest.TestCase):
    def test_maxprofit(self):
        s = Solution()

        # Test case 1: Example input
        # Test case 1: Example input
        prices1 = [1, 3, 2, 8, 4, 9]
        fee1 = 2
        assert s.maxprofit(prices1, fee1) == 8  # Use assert instead of self.assertEqual

        # Test case 2: Another example
        prices2 = [1, 4, 3, 6, 8, 2, 7]
        fee2 = 3
        assert s.maxprofit(prices2, fee2) == 6


def main() -> None:
    """
    This is the function for taking input and output.
    """
    prices = list(map(int, input("Enter the list of prices: ").split()))
    fee = int(input("Enter the transaction fee: "))

    s = Solution()
    max_profit = s.maxprofit(prices, fee)

    print("Maximum profit:", max_profit)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    unittest.main()
