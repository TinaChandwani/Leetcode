class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i,curr,res):
            res.append(curr[:])
            
            if i == len(nums):
                return
            
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                print(curr)
                backtrack(j + 1,curr,res)
                curr.pop()
            
            return res
        
        return backtrack(0,[],[])