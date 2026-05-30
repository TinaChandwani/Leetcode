class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def solve(l,r):
            if l > r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]

            if s[l] != s[r]:
                left =  solve(l,r-1)
                right = solve(l+1,r)
                res = 1 + min(left,right)
            else:
                res = solve(l+1,r-1)
            
            memo[(l,r)] = res
            return res
        
        return solve(0,len(s)-1)