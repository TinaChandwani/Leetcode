class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def solve(l,r):
            if l == r:
                return 1
            if l > r :
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            i = l + 1
            while i <= r and s[i] == s[l]:
                i += 1
            if i > r:
                return 1
            basic = 1 + solve(i,r)
            la = float('inf')
            for j in range(i,r + 1):
                if s[l] == s[j]:
                    cmplx = solve(i,j-1) + solve(j,r)
                    la = min(la, cmplx)
            
            memo[l,r] = min(basic,la)
            return memo[l,r]
        
        return solve(0,len(s)-1)
                    