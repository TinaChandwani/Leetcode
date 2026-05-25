class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        def backtrack(curr,res):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                curr.append(nums[i])
                seen.add(nums[i])
                backtrack(curr, res)
                curr.pop()
                seen.remove(nums[i]) 
            
            return res
        
        return backtrack([],[])