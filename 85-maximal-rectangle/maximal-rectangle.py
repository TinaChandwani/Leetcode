class Solution:
    def calculateArea(self,nums):
        s1 = []
        s2 = []
        maxArea = 0
        n = len(nums)
        pse = [-1 for i in range(n)]
        nse = [n for _ in range(n)]
        
        for i in range(n):
            while s1 and nums[s1[-1]] >= nums[i]:
                s1.pop()
            
            if s1:
                pse[i] = s1[-1]
            
            s1.append(i)
        
        for j in range(n-1,-1,-1):
            while s2 and nums[s2[-1]] >= nums[j]:
                s2.pop()
            
            if s2:
                nse[j] = s2[-1]
            
            s2.append(j)
        
        for k in range(n):
            area = nums[k] * (nse[k] - pse[k] - 1)
            maxArea = max(maxArea,area)

        return maxArea        

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix) , len(matrix[0])
        height = [0] * cols
        res = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "0":
                    height[j] = 0
                else:
                    height[j] += int(matrix[i][j])
            
            res = max(res,self.calculateArea(height))
        
        return res
