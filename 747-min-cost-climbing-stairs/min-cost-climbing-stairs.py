class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Bootom Up Approach
        '''
        n = len(cost)
        if n == 1:
            return cost[0]
        dp = [0] * (n+1)
        dp[1] = cost[0]
        for i in range(2,n+1):
            dp[i] = cost[i-1] + min(dp[i-1],dp[i-2])
        return min(dp[n],dp[n-1])
        