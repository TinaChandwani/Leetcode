class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Quickselect finds the k-th element by order without fully sorting.
        continues into the one side that could still contain the answer.
        average time is O(n)

        but if we keep picking bad pivots the time complexity will go upto O(n^2)
        I will assume pivot to the first element

        # Dutch National Flag
            1. t < pivot , t
        '''
        if not nums or k <= 0 or k > len(nums):
            return -1
        t = len(nums) - k

        start = 0
        end = len(nums) - 1
        while start <= end:
            m = (start + end) // 2
            pivot = nums[m]
            small_end = start
            current = start
            large_end = end
            while current <= large_end:
                if nums[current] < pivot:
                    nums[current],nums[small_end] = nums[small_end],nums[current]
                    current += 1
                    small_end += 1
                elif nums[current] == pivot:
                    current += 1
                else:
                    nums[current],nums[large_end] = nums[large_end],nums[current]
                    large_end -= 1
        
            if t < small_end:
                # Shrink to left side
                end = small_end - 1
            elif t > large_end:
                start = large_end + 1
            else:
                return nums[t]
            