class Solution:
    def __init__(self):
        self.mem = defaultdict()
    def climbStairs(self, n: int) -> int:
        # Recursion without Memoisation -> Time Limit Exceeded
        # if n == 0 or n == 1:
        #     return 1
        
        # return (self.climbStairs(n-1) + self.climbStairs(n-2))

        # Recursion with Memoisation

        if n == 0 or n == 1:
            return 1
        
        if n in self.mem:
            return self.mem[n]
        
        self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.mem[n]