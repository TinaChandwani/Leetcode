class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Bottom Up Approach
        '''
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n+1) 
        dp[1] = nums[0]
        for i in range(2,n+1):
            steal = nums[i-1] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal,skip)
        return dp[n]