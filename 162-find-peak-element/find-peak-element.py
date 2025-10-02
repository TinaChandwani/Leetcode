class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Basically to Solve in O(log n ) time:
        1) We first find m
        2) if nums[m] > nums[m+1] : then m has reached peak so the peak element would be in the left half of the array
        3) else : The peak is in right half of the array
        4) Repeat everything and return index
        '''
        l = 0 
        n = len(nums)
        if n == 1:
            return 0
        r = n - 1
        while r > l:
            m = (l+r) // 2
            if nums[m] > nums[m+1]:
                # Search in the left half
                r = m
            else:
                # # Search in the right half
                l = m + 1
        return l
        