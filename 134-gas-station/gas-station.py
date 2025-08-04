class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We need to return -1 if total gas < total cost
        # no need to loop through the whole of array since it especially says it will only have one unique solution
        totalGas = 0
        totalCost = 0

        for i in gas:
            totalGas += i
        for j in cost:
            totalCost += j
        if totalGas < totalCost:
            return - 1
        
        start = 0
        currGas = 0
        n = len(gas)

        for i in range(n):
            currGas += (gas[i] - cost[i])
            if currGas < 0:
                start = i + 1
                currGas = 0
        return start
