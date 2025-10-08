import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Basically add in the heap here do not let it go more than k
        self.heap = []
        self.k = k
        for i in nums:
            heapq.heappush(self.heap,i)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

        

    def add(self, val: int) -> int:
        # This addds the new score and returns the highest element always
       
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap,val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)