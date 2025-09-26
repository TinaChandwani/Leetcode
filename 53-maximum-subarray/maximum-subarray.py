class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_arr = 0
        max_arr = nums[0]

        for i in nums:
            sum_arr += i
            max_arr = max(sum_arr,max_arr)
            if sum_arr < 0:
                sum_arr = 0
        return max_arr