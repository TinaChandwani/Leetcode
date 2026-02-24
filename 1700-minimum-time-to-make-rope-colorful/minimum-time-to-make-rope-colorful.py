class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        n = len(neededTime)
        ops = 0 
        
        while i+1 < n:
            if colors[i] == colors[i+1]:
                if neededTime[i] < neededTime[i+1]:
                    ops += neededTime[i]
                else:
                    ops += neededTime[i+1]
                    neededTime[i+1] = neededTime[i]
            i += 1
        return ops


