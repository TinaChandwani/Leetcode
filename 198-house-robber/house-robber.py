class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Top Down (recursion + memoization)
        '''
        self.robDict = {}
        def solve(nums,i):
            if i >= len(nums):
                return 0
            if i in self.robDict:
                return self.robDict[i]
            else:
                steal = nums[i] + solve(nums,i+2)
                skip = solve(nums,i+1)
                self.robDict[i] = max(steal,skip)
                return self.robDict[i]
        return solve(nums,0)