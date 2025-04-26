class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        count= 1
        

        def minCost(cost,step,memo,count):
            if step == 0 or step == 1:
                return 0
            
            if step in memo:
                return memo[step]
            
            count = min(minCost(cost,step-1,memo,count) + cost[step-1],minCost(cost,step-2,memo,count)+  cost[step-2])
            memo[step] = count
            return count
        
        return minCost(cost,len(cost),memo,count) 
