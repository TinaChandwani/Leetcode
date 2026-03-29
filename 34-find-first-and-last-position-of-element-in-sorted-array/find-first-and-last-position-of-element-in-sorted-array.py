class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        def left_most(idx): 
            while idx > 0 and nums[idx - 1] == target:
                idx -= 1
            return idx
        
        def right_most(idx):
            while idx < len(nums) - 1 and nums[idx + 1] == target:
                idx += 1
            return idx
        
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                i = left_most(m)
                j = right_most(m)
                return [i,j]
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return [-1,-1]