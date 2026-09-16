class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum_profit = 0
        for price in prices:
            minimum = min(minimum, price)
            profit = price - minimum
            maximum_profit = max(maximum_profit, profit)
        return maximum_profit