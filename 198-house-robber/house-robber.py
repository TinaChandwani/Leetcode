class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Constant Space complexity 
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        prevPrev = 0
        prev = nums[0]
        for i in range(2,n+1):
            steal = nums[i-1] + prevPrev
            skip = prev
            temp = max(steal,skip)
            prevPrev = prev
            prev = temp
        return prev