class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = 0
        n = len(nums) - 1
        i = 0

        while i <= n:
            if i > maxReachable:
                return False
            reachable = i + nums[i]
            maxReachable = max(maxReachable,reachable)
            i += 1
        
        return True

        