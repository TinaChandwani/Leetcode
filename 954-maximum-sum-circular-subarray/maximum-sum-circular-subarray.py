class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        The Basic idea is => Total Sum - Global Minimum
        '''
        if len(nums) == 1:
            return nums[0]
        gMin = nums[0]
        gMax = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        total = nums[0]

        for i in nums[1:]:
            total += i
            currMax = max(i,currMax + i)
            gMax = max(gMax,currMax)
            currMin = min(i,currMin + i)
            gMin = min(gMin,currMin)

        if gMax < 0:
            return gMax
        else:
            return max(total-gMin,gMax)