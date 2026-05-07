class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(idx,curr,res):
            res.append(curr[:])
            
            dup = set()

            for i in range(idx,len(nums)):
                if nums[i] not in dup:
                    curr.append(nums[i])
                    backtrack(i+1,curr,res)
                    curr.pop()
                    dup.add(nums[i])
            
            return res
        
        return backtrack(0,[],[])