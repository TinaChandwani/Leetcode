class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            diff = max(diff,prices[i] - min_price)
        return diff