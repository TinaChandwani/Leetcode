class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Basic Approach:
        1. Find k (which is minimum in rotated sorted array)
        2) Apply Binary Search from [l:k][k:r] 
        '''
        def findk(l,r):
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l
        
        def bs(l,r):
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        
        n = len(nums)
        left = 0
        right = n - 1
        k = findk(left,right)
        a = bs(left,k)
        b = bs(k,right)
        if a != -1:
            return a
        elif b != -1:
            return b
        else:
            return -1