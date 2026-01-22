class Solution:
    def houseRobberI(self,nums):
        self.numsDict = {}
        def solve(n):
            if n >= len(nums):
                return 0
            if n not in self.numsDict:
                steal = nums[n] + solve(n+2)
                skip = solve(n+1)
                self.numsDict[n] = max(steal,skip)
            return self.numsDict[n]
        return solve(0)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        steal = self.houseRobberI(nums[:-1])
        skip = self.houseRobberI(nums[1:])
        return max(steal,skip)
        

    