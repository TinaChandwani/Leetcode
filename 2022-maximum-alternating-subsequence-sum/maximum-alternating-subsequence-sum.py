class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        Bottom Up Approach
        '''
        n = len(nums)
        dp = [[0,0] for _ in range(n+1)]
        even,odd = 0,1
        dp[0][even] = 0
        dp[0][odd] = nums[0]
        for i in range(1,n):
            dp[i][even] = max(dp[i-1][odd] - nums[i],dp[i-1][even])
            dp[i][odd] = max(dp[i-1][even] + nums[i],dp[i-1][odd])
        return max(dp[n-1][even],dp[n-1][odd])