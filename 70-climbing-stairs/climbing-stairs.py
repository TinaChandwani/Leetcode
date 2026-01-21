class Solution:
    def climbStairs(self, n: int) -> int:
        self.memDict = {}
        def solve(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in self.memDict:
                return self.memDict[n]
            else:
                a = solve(n-1) + solve(n-2)
                self.memDict[n] = a
            return self.memDict[n]
        return solve(n)