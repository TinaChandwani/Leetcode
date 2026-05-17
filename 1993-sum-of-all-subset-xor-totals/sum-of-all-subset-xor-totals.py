class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(idx,curr,res):
            res.append(curr[:])

            for i in range(idx,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr,res)
                curr.pop()
            return res
        
        ans = backtrack(0,[],[])
        print(ans)
        total = 0

        for j in ans:
            xor = 0
            for ele in j:
                xor ^= ele
            total += xor
        
        return total
        