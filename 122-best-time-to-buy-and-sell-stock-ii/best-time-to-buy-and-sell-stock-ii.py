class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        total = 0
        n = len(prices)

        for r in range(1,n):
            if prices[l] < prices[r]:
                # profit
                diff = prices[r] - prices[l]
                total += diff
                l += 1
            else:
                l = r
        
        return total
