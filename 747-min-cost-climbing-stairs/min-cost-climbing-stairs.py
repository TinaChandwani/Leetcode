class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def solve(i):
            if i >= len(cost):
                return 0
            if i not in memo:
                minCost = min(solve(i+2),solve(i+1))
                take = cost[i] + minCost
                memo[i] = take
            return memo[i]
        return min(solve(0),solve(1))