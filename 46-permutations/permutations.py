class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtracking template:
        Choose / Explore
        go Deeper / backtrack
        unchoose or revert back to the state of previous step
        '''
        ans = []
        n = len(nums)
        
        def backtrack(start,nums):
            if start == n:
                ans.append(nums.copy())
                return
            for i in range(start,n):
                nums[start],nums[i] = nums[i],nums[start]
                backtrack(start + 1,nums)
                nums[start],nums[i] = nums[i],nums[start]
        backtrack(0,nums)
        return ans