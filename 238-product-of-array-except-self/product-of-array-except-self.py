class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * (n)
        prefix = 1
        postfix = 1

        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        for j in range(n-1,-1,-1):
            output[j] *= postfix
            postfix *= nums[j]
        return output