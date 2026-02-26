class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Whenever your currSum goes negative -> reset to zero
        MaxSum = max(MaxSum,currSum)
        '''
        currSum = nums[0]
        maxSum = nums[0]
        n = len(nums)

        for i in range(1,n):
            currSum = max(nums[i],nums[i] + currSum)
            maxSum = max(maxSum,currSum)
            if currSum < 0:
                currSum = 0
        return maxSum
            

        