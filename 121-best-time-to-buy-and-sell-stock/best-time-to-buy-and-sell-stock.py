class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices)
        maxProfit = 0
        for j in range(1,n):
            proft = prices[j]-prices[i]
            maxProfit = max(maxProfit,proft)
            if prices[i] >= prices[j]:
                i = j
        return maxProfit
