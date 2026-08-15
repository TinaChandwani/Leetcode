class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        n = len(prices)

        while r < n:
            diff = prices[r] - prices[l]
            maxP = max(maxP,diff)
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return maxP
