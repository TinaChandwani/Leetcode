class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx,curr,res):
            if len(curr) >= 2:
                res.append(curr[:])
            
            dup = set()
            
            for i in range(idx,len(nums)):
                if (len(curr) == 0 or nums[i] >= curr[-1]) and nums[i] not in dup:
                    curr.append(nums[i])
                    backtrack(i + 1,curr,res)
                    curr.pop()
                    dup.add(nums[i])
            
            return res
        
        return backtrack(0,[],[])
                