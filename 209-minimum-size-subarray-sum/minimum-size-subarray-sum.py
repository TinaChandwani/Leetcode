class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        minLength = float('inf')
        add = 0

        while r < n:
            add += nums[r]
            while add >= target:
                minLength = min(minLength,r-l+1)
                add -= nums[l]
                l += 1
            r += 1

        if minLength == float('inf'):
            return 0
        else:
            return minLength    