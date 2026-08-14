class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        i = 0
        j = 1

        while j <= n - 1:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        
        return i + 1