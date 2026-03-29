class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_most(l,r):
            while l <= r:
                m = l + (r-l) // 2
                if nums[m] >= target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
            return l
        
        def right_most(l,r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
            return r
        
        i = left_most(0,len(nums)-1)
        j = right_most(0,len(nums)-1)
        
        if i <= j and nums[j] == target:
            return [i,j]

        return [-1,-1]