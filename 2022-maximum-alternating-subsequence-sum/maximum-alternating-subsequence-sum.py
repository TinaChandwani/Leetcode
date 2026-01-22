class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * 2 for _ in range(n+1)]
        def solve(n,flag):
            if n >= len(nums):
                return 0
            if memo[n][flag] == -1:
                skip = solve(n+1,flag)
                val = nums[n]
                if flag == 1:
                    val = -val
                    take = val + solve(n+1,0)
                else:
                    take = val + solve(n+1,1)
                memo[n][flag] =  max(skip,take)
            return memo[n][flag]
        return solve(0,0)
