class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        This is version of Kadane's Algorithm
        There are two ways by which we could get the answer -> with circular array OR Not overlapping
        So the idea is => Total Sum = Max Sum of subarray + Min Sum of subarray
        Ans would be max(MaxSum of array using Kadane's, Total Sum - Min Sum of subarray)
        '''
        currMax = nums[0]
        maxSum = nums[0]
        currMin = float('inf')
        total_sum = sum(nums)
        minSum = float('inf')
        n = len(nums)

        for i in range(1,n):
            currMax = max(nums[i],nums[i]+currMax)
            maxSum = max(maxSum,currMax)
            currMin = min(nums[i],nums[i]+currMin)
            minSum = min(minSum,currMin)
        ans = max(maxSum,total_sum - minSum)
        return ans   
        