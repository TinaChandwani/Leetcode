class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(idx,curr,res):
            res.append(curr[:])

            if idx == len(nums):
                return

            visit = set()

            for j in range(idx,len(nums)):
                if nums[j] not in visit:
                    curr.append(nums[j])
                    backtrack(j + 1, curr, res)
                    curr.pop()
                    visit.add(nums[j])
                    
            
            return res
        
        return backtrack(0,[],[])