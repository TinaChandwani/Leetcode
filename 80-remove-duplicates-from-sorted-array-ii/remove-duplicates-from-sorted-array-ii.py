class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 2
        j = 2
        n = len(nums)

        while j <= n - 1:
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i 
