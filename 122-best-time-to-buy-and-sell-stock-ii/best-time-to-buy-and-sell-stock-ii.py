class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) - 1
        i = 0
        max_profit = 0

        while i < n:
            if prices[i] <= prices[i+1]:
                profit = prices[i+1] - prices[i]
                max_profit += profit
            i += 1
        return max_profit

       