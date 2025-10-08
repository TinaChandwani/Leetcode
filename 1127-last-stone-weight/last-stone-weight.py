import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 0:
            return 0
        if n == 1:
            return stones[0]
        heap = []
        k = 2
        for i in range(n):
            heapq.heappush(heap,(stones[i],i))
            if len(heap) > k:
                heapq.heappop(heap)
        first,fir_i = heapq.heappop(heap)
        second,second_i = heapq.heappop(heap)
        if first == second:
            # Always delete the larger element first 
            i1,i2 = max(fir_i,second_i), min (fir_i,second_i)
            del stones[i1]
            del stones[i2]

        else:
            stones[second_i] = second - first
            del stones[fir_i]
        
        return self.lastStoneWeight(stones)

