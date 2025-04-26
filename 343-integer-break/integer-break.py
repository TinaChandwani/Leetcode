class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        output = 1
        if n == 2:
            return 1
        if n == 3:
            return 2

        def helper(n):
            if n <= 3:
                return n
            
            if n in memo:
                return memo[n]

            if n % 2 == 0:
                output = max(helper(n//2) * helper(n//2),helper(n//2 + 1) * helper(n//2 - 1))
            else:
                output = max(helper(n//2 + 2) * helper(n//2 - 1),helper(n//2 + 1) * helper(n//2 ))

            memo[n] = output
            return output
        
        return helper(n)