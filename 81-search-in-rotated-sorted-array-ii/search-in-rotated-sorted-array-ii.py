class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        Same as search in rotated sorted array
        just skip duplicates => imp part
        '''
        def bs(l,r):
            while l <= r:
                m = l + (r-l) // 2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        def findPivot(l,r):
            while l < r:
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                m = l + (r-l) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return r
        
        pivot = findPivot(0,len(nums)-1)
        first_half = bs(0,pivot-1)
        second_half = bs(pivot,len(nums)-1)

        return (first_half or second_half)