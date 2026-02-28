class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        If the total kamai >= total karch ==> guranteed you will get an ans
            -> That is why you just need to iterate once
        '''
        if sum(cost) > sum(gas):
            return -1
        
        total_gas = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            # check if i can go the next gas station or not
            if total_gas < cost[i]:
                total_gas = 0
                start = i + 1
            else:
                total_gas = total_gas - cost[i]
        
        return start
            