class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev1 = nums[0]
        prev2 = 0

        for i in range(2,n+1):
            current = max(prev1,prev2+nums[i-1])

            prev2 = prev1
            prev1 = current
        
        return prev1