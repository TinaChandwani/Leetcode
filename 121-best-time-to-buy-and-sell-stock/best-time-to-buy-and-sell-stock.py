class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        r = 0
        n = len(prices)
        diff = 0

        while r < n:
            while stack and stack[-1] > prices[r]:
                stack.pop()
            if not stack:
                stack.append(prices[r])
            else:
                diff = max(diff, prices[r] - stack[-1])
            r += 1
        
        return diff