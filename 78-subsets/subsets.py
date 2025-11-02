class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def backtrack(start):
            ans.append(path.copy())
            for i in range(start,n):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans
        