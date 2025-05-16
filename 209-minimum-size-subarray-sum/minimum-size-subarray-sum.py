class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        sub = 0
        leng = float('inf')

        while r < n:
            sub = sub + nums[r]
            while target <= sub:
                leng = min(leng,1+r-l)
                sub -= nums[l]
                l += 1
            r += 1

        if leng == float('inf'):
            return 0
        else:
            return leng