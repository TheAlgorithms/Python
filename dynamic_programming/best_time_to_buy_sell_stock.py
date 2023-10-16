#############################
# Author: yash kesharwani
# File: best_time_to_buy_sell_stock.py
# comments: This program output the
# best time to buy and sell stock with fees
#############################
from typing import List


class Solution:
    def solve(
        self, prices: List[int], index: int, fee: int, buy: int, dp: List[List[int]]
    ) -> int:
        """
        Calculate the maximum profit with the given parameters.

        :param prices: List of prices for each day.
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

    def maxprofit(self, prices: List[int], fee: int) -> int:
        """
        Calculate the maximum profit achievable when buying and
        selling stocks with a fee.

        :param prices: List of stock prices for each day.
        :param fee: Transaction fee.
        :return: Maximum profit achievable.
        """
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        return self.solve(prices, 0, fee, 1, dp)


def main():
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
    main()
