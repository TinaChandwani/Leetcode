class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i = i + 1
                j = j + 1
                k = k + 1
            else:
                del nums[j]
        
        return k