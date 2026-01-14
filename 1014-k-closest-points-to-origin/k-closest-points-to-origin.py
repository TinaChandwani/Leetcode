class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        We have to implement here Max heap (which is negative of min heap)
        '''
        heap = [] # store heap, distance, x,y

        for i,j in points:
            distance = i**2 + j**2
            heapq.heappush(heap,(-distance,i,j))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[k,l] for _,k,l in heap]