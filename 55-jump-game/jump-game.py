class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        maxReachable = 0
        n = len(nums) - 1
        i = 0

        while i < n:
            if i > maxReachable:
                return False
            reachable = i + nums[i]
            maxReachable = max(maxReachable,reachable)
            i += 1
        
        if maxReachable >= n:
            return True
        else:
            return False

        