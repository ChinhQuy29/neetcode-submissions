class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - buy)
            buy = min(buy, price)
        return max_profit