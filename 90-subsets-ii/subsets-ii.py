class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        n = len(nums)

        def backtrack(start):
            if start == n:
                ans.append(path.copy())
                return 
            # Include
            path.append(nums[start])
            backtrack(start+1)
            path.pop()
            # Exclude
            j = start + 1
            while j < n and nums[j] == nums[start]:
                j += 1
            backtrack(j)
        backtrack(0)
        return ans
        