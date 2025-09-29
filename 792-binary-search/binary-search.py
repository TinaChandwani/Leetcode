class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #iterative
        n = len(nums)
        l = 0
        r = n - 1
        while r >= l:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1
        