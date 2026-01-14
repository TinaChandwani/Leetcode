import heapq
class KthLargest:
    '''
    Heap :
    log(N) => Insertions and deletions
    It is complete binary tree
    To build a heap => O(N)

    For this problem the complexity is :
    Insertions => Mlog(k) where M is number of add calls
    Deletions => Nlog(k) where N is len(nums) 
    '''

    def __init__(self, k: int, nums: List[int]):
        # Create a heap with size = k
        self.heap = []
        self.k = k

        for i in nums:
            heapq.heappush(self.heap,i)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0] :
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)