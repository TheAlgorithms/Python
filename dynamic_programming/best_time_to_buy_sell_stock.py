#############################
# Author: yash kesharwani
# File: best_time_to_buy_sell_stock.py
# comments: This program output the
# best time to buy and sell stock with fees
#############################
import doctest


class Solution:
    def solve(self, prices, index, fee, buy, dp):
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

    def maxprofit(self, prices, fee):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        return self.solve(prices, 0, fee, 1, dp)


def main():
    ## This is the function for taking input and output ##
    prices = list(map(int, input("Enter the list of prices: ").split()))
    fee = int(input("Enter the transaction fee: "))

    s = Solution()
    max_profit = s.maxprofit(prices, fee)

    print("Maximum profit:", max_profit)


if __name__ == "__main__":
    doctest.testmod()
    main()
