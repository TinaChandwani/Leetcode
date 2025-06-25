class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = float("-inf")
        
        while i < j:
            area = (j-i) * min(height[i],height[j])
            maxArea = max(maxArea,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea