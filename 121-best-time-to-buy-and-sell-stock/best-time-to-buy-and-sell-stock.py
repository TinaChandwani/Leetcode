class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        n = len(prices)
        maxProfit = 0
        
        while j < n and i < n:
            profit = prices[j] - prices[i]
            maxProfit = max(maxProfit,profit)
            if prices[j] <= prices[i]:
                i = j   
            j += 1
        
        return maxProfit