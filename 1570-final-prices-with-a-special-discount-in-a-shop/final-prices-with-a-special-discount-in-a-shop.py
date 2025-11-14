class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
        Basically you need to find the next smaller element
        '''
        n = len(prices)
        nse = [0] * n
        stack = []
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(prices[i])
        
        print(f'nse {nse}')
        
        for j in range(n):
            ans[j] = prices[j] - nse[j]
        
        return ans
        