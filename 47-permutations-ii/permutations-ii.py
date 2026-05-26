class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        Instead of numbers, use indices for the seen set to find the permutations
        '''
        seen = set()
        nums.sort()
        
        def backtrack(curr,res):
            if len(curr) == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in seen:
                    continue
                    

                curr.append(nums[i])
                seen.add(i)
                backtrack(curr,res)
                curr.pop()
                seen.remove(i)
            
            return res
        
        return backtrack([],[])