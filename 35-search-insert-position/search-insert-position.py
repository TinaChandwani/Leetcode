class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # iterative
        l = 0
        n = len(nums)
        r = n - 1
        while r >= l:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l