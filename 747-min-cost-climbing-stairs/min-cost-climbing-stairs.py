class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Overall Flow is -> you want to reach i step, what is the minimum cost to reach there
        So Basically , Min (cost to reach i-1 step + cost of i-1 step, cost to reach i-2 step + cost of i-2 step)
        Base Case -> if step == 0 or 1 return 0 [cause the problem allows us to start at step 0 or 1 without paying any cost]
        '''
        def helper(step):
            if step == 0 or step == 1:
                return 0
            
            if step in memo:
                minCost = memo[step]
            else:
                minCost = min(helper(step-1) + cost[step-1],helper(step-2) + cost[step-2])
                memo[step] = minCost

            return minCost

        n = len(cost)
        memo = {}
        return helper(n)