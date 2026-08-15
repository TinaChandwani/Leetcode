class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        maxJ = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > maxJ:
                break
            jump = i + nums[i]
            maxJ = max(maxJ,jump)
            if maxJ >= last:
                return True
        
        return False