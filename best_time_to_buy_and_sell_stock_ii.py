class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index, price in enumerate(prices):
            if index > 0 and prices[index - 1] < price:
                profit += price - prices[index - 1]
        return profit
