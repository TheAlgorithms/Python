"""
Author  : Yash Kesharwani
Date    : October 8, 2023

This is a pure Python implementation of Dynamic Programming solution to the
Best time to Buy and Sell Stock with
transaction fee.

The problem is :
You are given an array prices where prices[i] is the price of a given stock
on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve.
You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.
"""


class MaxProfitWithFee:
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
        for sub in dp:
            sub.fill(-1)
        return self.solve(prices, 0, fee, 1, dp)


# Main function to take input and print output
if __name__ == "__main__":
    prices = list(map(int, input("Enter the prices: ").split()))
    fee = int(input("Enter the fee: "))

    solution = MaxProfitWithFee()
    result = solution.maxprofit(prices, fee)

    print("Maximum Profit:", result)
