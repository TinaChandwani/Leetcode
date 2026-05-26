class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        
        def backtrack(curr,res):
            if len(curr) == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            

            for i in range(len(nums)):
                if i in seen:
                    continue

                curr.append(nums[i])
                seen.add(i)
                backtrack(curr,res)
                curr.pop()
                seen.remove(i)
            
            return res
        
        return backtrack([],[])