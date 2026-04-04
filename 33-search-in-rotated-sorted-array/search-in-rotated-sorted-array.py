class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Find the minimum element in the array => pivot
        do different binary search
        (0,pivot) (pivot + 1, len(nums)-1)
        '''
        def b_s(l,r):
            while l <= r:
                m = l + (r-l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        def min(l,r):
            while l < r:
                m = l + (r-l) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return r  
        
        min_element = min(0,len(nums)-1)
        first_half = b_s(0,min_element - 1)
        second_half = b_s(min_element,len(nums)-1)

        if first_half == -1 and second_half == -1:
            return -1
        elif first_half == -1:
            return second_half
        else:
            return first_half