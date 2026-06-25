class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = [-1] * n
        stack = []
        res = 0

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        nse = [n] * n
        s2 = []

        for j in range(n-1,-1,-1):
            while s2 and heights[j] <= heights[s2[-1]]:
                s2.pop()
            if s2:
                nse[j] = s2[-1]
            s2.append(j)
        
        for k in range(n):
            area = heights[k] * (nse[k] - pse[k] - 1)
            res = max(res,area)
        
        return res