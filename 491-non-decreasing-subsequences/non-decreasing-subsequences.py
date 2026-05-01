class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx,curr,res):
            if len(curr) >= 2:
                res.add(tuple(curr))

            
            for i in range(idx,len(nums)):
                if len(curr) == 0 or nums[i] >= curr[-1]:
                    curr.append(nums[i])
                    backtrack(i + 1,curr,res)
                    curr.pop()
            
            return list(res)
        
        return backtrack(0,[],set())
                