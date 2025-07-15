class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxInd = 0
        n = len(nums) - 1
        if n == 0:
            return True
        for i in range(n):
            if i > maxInd:
                return False
            maxInd = max(maxInd,i + nums[i])
        if maxInd >= n :
            return True
        else:
            return False
        
        