from typing import List


class StockBuySell:
    def __init__(self, prices: List[int]):
        self.prices = prices

    def max_profit_type1(self) -> int:
        if not self.prices:
            return 0

        min_price = self.prices[0]
        max_profit = 0

        for price in self.prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

    def max_profit_type2(self) -> int:
        if not self.prices:
            return 0

        max_profit = 0

        for i in range(1, len(self.prices)):
            if self.prices[i] > self.prices[i - 1]:
                max_profit += self.prices[i] - self.prices[i - 1]

        return max_profit


prices_type = [7, 1, 5, 3, 6, 4]
# Example usage for Type 1: Single day to buy one stock and a different day in the future to sell that stock
trader_type1 = StockBuySell(prices_type)
max_profit_type1 = trader_type1.max_profit_type1()
print("Maximum profit (Type 1):", max_profit_type1)

# Example usage for Type 2: Hold at most one share of the stock at any time
trader_type2 = StockBuySell(prices_type)
max_profit_type2 = trader_type2.max_profit_type2()
print("Maximum profit (Type 2):", max_profit_type2)
