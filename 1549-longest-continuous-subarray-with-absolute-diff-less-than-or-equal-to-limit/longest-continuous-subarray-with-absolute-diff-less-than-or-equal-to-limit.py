class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        For any subarray you want to check the validity:
        I need to it's min and max element
        Once i find it's difference and if that is within limits then
        for all the elements present in the subarray the diff will be
        in limits
        We can use heap to get the smallest and maximum in O(1) 
        Min Heap => {element, idx}
        Max Heap => {element, idx}
        l,r => Sliding Window
        '''
        minHeap = []
        maxHeap = []
        l = 0
        r = 0
        n = len(nums)
        size = 0

        while r < n:
            heapq.heappush(minHeap,(nums[r],r))
            heapq.heappush(maxHeap,((-1 * nums[r]),r)) 
     
            while (-maxHeap[0][0]) - minHeap[0][0] > limit:
                l += 1

                while minHeap[0][1] < l:
                    heapq.heappop(minHeap)

                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)


            size = max(size,r-l+1) 
            r += 1

        return size   
