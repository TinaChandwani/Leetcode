class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Our range is [1,n]
        First check if 1 is present or not in nums :
            If it is not present that 1 will always be the answer
        '''
        # First check if it contains 1 or not and convert <= 0 and > n to 1
        n = len(nums)
        containsOne = False
        for i in range(n):   
            if nums[i] == 1:
                containsOne = True
            elif nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if containsOne == False:
            return 1
        
        for k in range(n):
            num = abs(nums[k])
            idx = num - 1
            if nums[idx] > 0:
                nums[idx] = nums[idx] * -1
        
        # check if nums[idx] is positive
        for j in range(n):
            if nums[j] > 0:
                return j + 1
        return n + 1
