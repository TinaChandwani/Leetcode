class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        profit = 0


        def helper(nums,memo,n):
            if n >= len(nums):
                return 0
            
            if n in memo:
                return memo[n]
            
            profit = max(helper(nums,memo,n+1), helper(nums,memo,n+2) + nums[n])
            memo[n] = profit
            return profit
        
        return helper(nums,memo,0)
        

