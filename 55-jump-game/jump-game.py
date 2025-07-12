class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # farthest = 0
        # n = len(nums) - 1
        # for i in range(n):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest,i+nums[i])
        
        # if farthest >= n:
        #     return True
        # else:
        #     return False


        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True