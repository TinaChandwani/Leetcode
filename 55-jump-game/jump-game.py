class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums) - 1
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest,i+nums[i])
        
        if farthest >= n:
            return True
        else:
            return False