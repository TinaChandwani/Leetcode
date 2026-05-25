class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(idx,curr,res):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(idx,n+1):
                curr.append(i)
                backtrack(i + 1,curr,res)
                curr.pop()

            return res
        
        return backtrack(1,[],[])

