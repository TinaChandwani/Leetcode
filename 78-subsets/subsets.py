class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx,curr,res):
            res.append(curr[:])
            
            
            for i in range(idx,len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr, res)
                curr.pop()
            
            return res
        
        return backtrack(0,[],[])

        